from LibraryItem import LibraryItem
from Book import Book
from Magazine import Magazine
from Video import Video

# check that valid and invalid item pairs work as expected
b1 = Book("B12")
b2 = Book("A12")
# b1.process()
# b2.process() # will cause exception

m2 = Magazine("M12")
m1 = Magazine("B12")
# m1.process() # will cause exception
# m2.process()

v1 = Video("V1")
v2 = Video("S2")
v1.process()
# v2.process() # will cause exception
