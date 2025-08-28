# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.

# SOLUTION:

list_ = ["hello world!"]

try:
    print(list_[1])
except IndexError as e:
    print(f"There is something wrong here...error: {e}")