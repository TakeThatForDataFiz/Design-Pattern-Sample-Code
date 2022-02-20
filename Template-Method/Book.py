from Library import LibraryItem


class Book(LibraryItem):

    def check_item_code(self):
        if self._item_code[0] != 'B':
            raise ValueError("Invalid Item Code for Book")
        else:
            print("Item code is valid for Book")

    def clean(self):
        print("Book has been cleaned properly")
