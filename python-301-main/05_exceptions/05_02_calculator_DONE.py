# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.
while True:
    try:
        number_1 = int(input("number 1: "))
        number_2 = int(input("number 2: "))
        quotient = (number_1/number_2)
    except ZeroDivisionError as e:
        print(f"Brother, you can not divided anything by zero... error: {e}")
    except ValueError as e:
        print(f"Brother, please introduce only numbers!... error: {e}")
    else: 
        print(f"The result is {quotient}")
        break