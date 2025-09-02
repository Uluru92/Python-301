def lowercase(func):
    """A decorator that avoids digital screaming."""
    def wrapper(text):
        initial_result = func(text)
        new_result = initial_result.lower()
        return new_result
    return wrapper

@lowercase
def say_something(text):
    return text

@lowercase
def hi_name(name):
    text = "Hello: "+ name
    return text

print(say_something("HEY WHAT'S UP?"))  # OUTPUT: hey what's up?
print(say_something(input("text something is CAPS: " )))  # what you write in lower
print(hi_name(input("Please insert your name: ")))