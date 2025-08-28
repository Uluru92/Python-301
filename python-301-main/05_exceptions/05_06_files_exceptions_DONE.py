# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?

# 1) Solution
with open("books\war_and_peace.txt",'r', encoding="utf-8") as f:
    war_and_peace_variable = f.read()

# 2) Solution
with open("books\crime_and_punishment.txt",'w', encoding="utf-8") as f:
    empty_variable = ""
    f.write(empty_variable)

# 3) Solution

# war_and_peace.txt
try:
    with open("books\war_and_peace.txt",'r', encoding="utf-8") as f:
        first_char_war_and_peace = f.read()[0]

except Exception as e:
    print(f"There was an error, information: {e}")

else: 
    print(f"First character of war and peace: {first_char_war_and_peace}")

# pride_and_prejudice.txt
try:
    with open("books\pride_and_prejudice.txt",'r', encoding="utf-8") as f:
        first_price_and_prejudice = f.read()[0]

except Exception as e:
    print(f"There was an error, information: {e}")

else: 
    print(f"First character of war and peace: {first_price_and_prejudice}")

# crime_and_punishment.txt
try:
    with open("books\crime_and_punishment.txt",'r', encoding="utf-8") as f:
        first_char_crime_and_punishment = f.read()[0]

except IndexError as e:
    print(f"Ups... seems like the .txt is empty, error information: {e}")

except:
    print(f"There was an error, information: {e}")

else: 
    print(f"First character of war and peace: {first_char_crime_and_punishment}")

