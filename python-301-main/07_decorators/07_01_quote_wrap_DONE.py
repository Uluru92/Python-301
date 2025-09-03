# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

# Solution:

def decorator_quotes(func):
    """A decorator that wraps text output into quotes"""
    def wrapper(text):
        initial_result = func(text)
        new_result = f'"{initial_result}"'
        return print(new_result)
    return wrapper

@decorator_quotes
def say_something(text):
    return text

say_something("Hello world!")