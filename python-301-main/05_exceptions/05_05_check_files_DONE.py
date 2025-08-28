# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'

try:
    with open('integers.txt',"r",encoding="utf-8") as f:
        txt_content = f.read().splitlines()
    first_integer = int(txt_content[0])
    calculation = first_integer * 5

except IOError as e:
    print(f"IOError occurred: {e}")

except ValueError as e:
    print(f"ValueError occurred: {e}")

except Exception as e:
    print(f"There was an error: {e}")

else:
    print(f"The first integer multiplied by 5 equals: {calculation}")