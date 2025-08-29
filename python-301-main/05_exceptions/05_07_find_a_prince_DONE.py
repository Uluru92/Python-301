# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

import string

class PrinceException(Exception):
    pass

# war_and_peace.txt
try:
    with open("books\war_and_peace.txt",'r', encoding="utf-8") as f:
        text = f.read()
        words = text.split()

    for index,word in enumerate(words[:100], start=1):
        if word.strip(string.punctuation).lower() == 'prince':
            raise PrinceException(f"Word '{word}' found at position {index} in the book Was and Peace!")

except PrinceException as e:
    print(f"Caught an exception: {e}")

# pride_and_prejudice.txt
try:
    with open("books\pride_and_prejudice.txt",'r', encoding="utf-8") as f:
        text = f.read()
        words = text.split()

    for index,word in enumerate(words[:100], start=1):
        if word.strip(string.punctuation).lower() == 'prince':
            raise PrinceException(f"Word '{word}' found at position {index} in the book Pride and Prejudice!")

except PrinceException as e:
    print(f"Caught an exception: {e}")

# crime_and_punishment.txt
try:
    with open("books\crime_and_punishment_copy.txt",'r', encoding="utf-8") as f:
        text = f.read()
        words = text.split()

    for index,word in enumerate(words[:100], start=1):
        if word.strip(string.punctuation).lower() == 'prince':
            raise PrinceException(f"Word '{word}' found at position {index} in the book Crime and Punishment!")

except PrinceException as e:
    print(f"Caught an exception: {e}")