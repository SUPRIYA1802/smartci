import pytest
from src.inventory import Inventory


def test_add_stock():
    i = Inventory()
    i.add_stock('pen', 10)
    assert i.stock['pen'] == 10


def test_remove_stock():
    i = Inventory()
    i.add_stock('pen', 10)
    i.remove_stock('pen', 3)
    assert i.stock['pen'] == 7


def test_remove_too_much():
    i = Inventory()
    i.add_stock('pen', 5)
    with pytest.raises(ValueError):
        i.remove_stock('pen', 10)