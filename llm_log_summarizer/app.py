import streamlit as st
from pathlib import Path

# -------------------------------
# Application Configuration
# -------------------------------

st.set_page_config(
    page_title="SmartCI Build Log Summarizer",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 SmartCI - Build Log Summarizer")

st.write(
    "Upload a build log or select a sample log "
    "to identify errors and generate a Root Cause Summary."
)

# -------------------------------
# Sample Logs Directory
# -------------------------------

BASE_DIR = Path(__file__).parent
SAMPLE_DIR = BASE_DIR / "sample_logs"

SAMPLE_DIR.mkdir(exist_ok=True)

# Create sample logs if missing
sample_data = {
    "python_error.log": """
Traceback (most recent call last):
ModuleNotFoundError: No module named 'pandas'
Build failed due to missing Python module.
""",

    "dependency_error.log": """
ERROR: Could not install required dependencies.
Package installation failed.
Dependency resolution error.
""",

    "build_failure.log": """
[ERROR] BUILD FAILURE
Tests failed during execution.
Compilation error detected.
Build terminated unsuccessfully.
"""
}

for filename, content in sample_data.items():
    file_path = SAMPLE_DIR / filename
    if not file_path.exists():
        file_path.write_text(content.strip(), encoding="utf-8")

# -------------------------------
# Root Cause Analysis
# -------------------------------

def generate_summary(log_text):

    text = log_text.lower()

    if "modulenotfounderror" in text:
        return (
            "Python dependency is missing.",
            "Install the missing module using pip.",
            "Check requirements.txt and install dependencies."
        )

    elif "filenotfounderror" in text:
        return (
            "Required file or directory was not found.",
            "Verify the file path and directory structure.",
            "Ensure the required file exists in the correct location."
        )

    elif "importerror" in text:
        return (
            "A Python module or function could not be imported.",
            "Check module installation and import statements.",
            "Reinstall the package if necessary."
        )

    elif "syntaxerror" in text:
        return (
            "Python syntax error detected.",
            "Correct the syntax in the affected Python file.",
            "Check indentation, brackets, and spelling."
        )

    elif "dependency" in text or "could not install" in text:
        return (
            "Dependency installation failed.",
            "Check package versions and dependency conflicts.",
            "Run pip install -r requirements.txt."
        )

    elif "build failure" in text or "build failed" in text:
        return (
            "Build process failed.",
            "Inspect build output and identify the failing component.",
            "Correct compilation or test errors and rerun the build."
        )

    elif "failed" in text or "error" in text:
        return (
            "Build or execution error detected.",
            "Inspect the error messages in the log.",
            "Correct the reported issue and rerun the process."
        )

    else:
        return (
            "No common error pattern detected.",
            "Review the complete build log.",
            "Check warnings and execution details for potential problems."
        )

# -------------------------------
# Sample Log Selection
# -------------------------------

sample_files = {
    "Python Error": "python_error.log",
    "Dependency Error": "dependency_error.log",
    "Build Failure": "build_failure.log"
}

st.subheader("1. Select Sample Log")

selected_sample = st.selectbox(
    "Select sample log",
    ["None"] + list(sample_files.keys())
)

log_text = ""

if selected_sample != "None":
    sample_path = SAMPLE_DIR / sample_files[selected_sample]

    if sample_path.exists():
        log_text = sample_path.read_text(encoding="utf-8")

# -------------------------------
# Upload Log File
# -------------------------------

st.subheader("2. Upload Build Log")

uploaded_file = st.file_uploader(
    "Upload your build log",
    type=["log", "txt"]
)

if uploaded_file is not None:
    log_text = uploaded_file.getvalue().decode(
        "utf-8", errors="replace"
    )

# -------------------------------
# Display Build Log
# -------------------------------

st.subheader("3. Build Log")

log_text = st.text_area(
    "Build log content",
    value=log_text,
    height=200
)

# -------------------------------
# Summarization
# -------------------------------

if st.button("Summarize", type="primary"):

    if not log_text.strip():
        st.warning("Please select or upload a build log.")

    else:
        root_cause, fix, recommendation = generate_summary(
            log_text
        )

        st.success("Log analysis completed successfully!")

        st.subheader("Root Cause Summary")
        st.write(root_cause)

        st.subheader("Suggested Fix")
        st.write(fix)

        st.subheader("Recommended Action")
        st.write(recommendation)

        st.subheader("Analysis Status")
        st.write("Build log analyzed successfully.")

# -------------------------------
# Footer
# -------------------------------

st.divider()

st.caption(
    "SmartCI | Automated Build Log Analysis "
    "| Rule-Based Summarization"
)
