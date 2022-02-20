import pytest
from LibraryItem import LibraryItem
from Book import Book
from Magazine import Magazine
from unittest.mock import MagicMock


def test_library_item_exists():
    new_item = LibraryItem("13")
    assert new_item is not None


def test_library_item_process_method_exists():
    new_item = LibraryItem("13")
    new_item.process = MagicMock(wraps=new_item.process)
    new_item.process()
    new_item.process.assert_called()


def test_library_item_process_calls_accept():
    new_item = LibraryItem("13")
    new_item.accept = MagicMock(wraps=new_item.accept)
    new_item.process()
    new_item.accept.assert_called()


def test_library_item_has_item_code():
    new_item = LibraryItem("13")
    assert new_item._item_code == "13"


def test_book_item_checks_item_code_when_processing():
    book = Book("B12")
    book.check_item_code = MagicMock(wraps=book.check_item_code)
    book.process()
    book.check_item_code.assert_called()


def test_book_item_check_raises_error_when_code_not_B():
    book = Book("A12")
    with pytest.raises(ValueError):
        book.process()


def test_magazine_item_check_raises_error_when_code_not_M():
    mag = Magazine("B12")
    with pytest.raises(ValueError):
        mag.process()
