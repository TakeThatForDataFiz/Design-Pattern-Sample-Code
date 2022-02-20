from LibraryItem import LibraryItem


class Video(LibraryItem):

    def check_item_code(self):
        if self._item_code[0] != 'V':
            raise ValueError("Invalid Code for Video")

    def clean(self):
        print("The Video has been specially cleaned")
