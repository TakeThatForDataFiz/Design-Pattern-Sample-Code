from LibraryItem import LibraryItem


class Magazine(LibraryItem):
    def check_item_code(self):
        if self._item_code[0] != "M":
            raise ValueError("Invalid Code for Magazine")
        else:
            print("Value Code accepted")

    def clean(self):
        print("The Magazine has been cleaned specially")
