from Library import LibraryItem
from unittest.mock import MagicMock


def test_library_item_exists():
    new_item = LibraryItem()
    assert new_item is not None


def test_library_item_process_method_exists():
    new_item = LibraryItem()
    new_item.process = MagicMock(wraps=new_item.process)
    new_item.process()
    new_item.process.assert_called()
