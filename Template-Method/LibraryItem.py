
import abc


class LibraryItem:
    __metaclass__ = abc.ABCMeta

    def __init__(self, item_code):
        self._item_code = item_code

    def process(self):
        self.accept()
        self.clean()
        self.check_item_code()
        self.store()

    def accept(self):
        print("The item has been accepted into the store")

    @abc.abstractmethod
    def clean(self):
        return

    @abc.abstractmethod
    def check_item_code(self):
        return

    def store(self):
        print("The Item has been stored")
