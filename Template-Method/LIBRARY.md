# Library

A library rents out Books, Magazines, and Videos. The returning process is slightly different for each
kind of item.

# Return Process

1. Accept Item
2. Clean Item (Different for each type of item)
3. Check Item Code (Different for each type of item)
4. Store

# Motivation for Using Template Method Pattern

The Library can save time by using the template method. The structure of the return process is maintained
for every item. However, the slight variations can be implemented within the sub-classes for each item.
