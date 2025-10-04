# Write a unittest test suite in `test_mymath.py`
# for the `subtract_divide()` function shown below.
# Check for more instructions in `test_mymath.py`

class CustomZeroDivsionError(Exception):
    pass

def subtract_divide(dividend, x, y):
    try:
        z = x - y
        return dividend / z
    except ZeroDivisionError:
        raise CustomZeroDivsionError(f"This won't work because {x} - {y} = 0.")
    
# example of result 
print(subtract_divide(5,4,2))

