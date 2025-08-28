# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

while True:
    try:
        integer_ = int(input("Please input an integer: "))

    except ValueError as e:
        print(f"Your input is not an integer... error: {e}")

    else:
        input_type = str(type(integer_))
        print(f"Your {integer_} is an {input_type}")
        break