from pathlib import Path
import ast
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
TESTS = ROOT / "tests"


def module_name(path):
    rel = path.relative_to(ROOT).with_suffix("")
    return ".".join(rel.parts)


def changed_files():
    base = os.getenv("BASE_SHA")
    head = os.getenv("HEAD_SHA")

    if base and head:
        cmd = ["git", "diff", "--name-only", "-z", base, head]
    else:
        cmd = ["git", "diff", "--name-only", "-z", "HEAD~1", "HEAD"]

    try:
        result = subprocess.run(
            cmd, cwd=ROOT, capture_output=True, text=True, check=True
        )
        return [x for x in result.stdout.split("\0") if x]
    except Exception:
        return []


def imports_in(path):
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except Exception:
        return set()

    found = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for item in node.names:
                found.add(item.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            found.add(node.module)

    return found


def build_reverse_graph():
    reverse = {}

    for path in SRC.glob("*.py"):
        mod = module_name(path)

        for imported in imports_in(path):
            if imported == mod:
                continue

            if imported.startswith("src."):
                target = imported
            else:
                target = "src." + imported.split(".")[0]

            if (SRC / (target.replace("src.", "") + ".py")).exists():
                reverse.setdefault(target, set()).add(mod)

    return reverse


def dependent_modules(changed_modules):
    reverse = build_reverse_graph()
    impacted = set(changed_modules)
    queue = list(changed_modules)

    while queue:
        current = queue.pop()

        for dep in reverse.get(current, set()):
            if dep not in impacted:
                impacted.add(dep)
                queue.append(dep)

    return impacted


def test_imports(path):
    return imports_in(path)


def select_tests(files):
    normalized = {
        p.replace("\\", "/").lstrip("./")
        for p in files
    }

    if not normalized:
        return ["tests"], "No changed files; running full suite."

    source_changes = []

    for item in normalized:
        if item.startswith("src/") and item.endswith(".py"):
            source_changes.append(item)
        else:
            return [
                "tests"
            ], f"{item} is not safely routable; running full suite."

    changed_modules = {
        "src." + Path(item).stem
        for item in source_changes
    }

    impacted = dependent_modules(changed_modules)

    chosen = set()

    for test in TESTS.glob("test_*.py"):
        imports = test_imports(test)

        if any(
            mod in imports or mod.replace("src.", "") in imports
            for mod in impacted
        ):
            chosen.add(str(test.relative_to(ROOT)))

    if not chosen:
        return ["tests"], "No test mapping found; running full suite."

    return sorted(chosen), "Selected tests from the dependency impact graph."


def main():
    files = changed_files()
    tests, reason = select_tests(files)

    print(" ".join(tests))
    print(f"# {reason}", file=sys.stderr)

    if files:
        print(
            "# Changed: " + ", ".join(files),
            file=sys.stderr
        )


if __name__ == "__main__":
    main()
    