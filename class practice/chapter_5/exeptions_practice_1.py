class AgeBelowZeroError(Exception): pass

while True:
    try:
        age = int(input("Age: "))
        if age < 0:
            raise AgeBelowZeroError()
    except ValueError:
        print("Please enter a numeric value.")
    except AgeBelowZeroError:
        print(65, "asd", age) # You can pass a number, an string and even 
    else:
        print(f"Congratulations, you're {age} years old!")
