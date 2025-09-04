# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import time

def decorator_time_it(init_func):
    def wrapper():
        start = time.time()   
        result = f"{init_func()}"
        end = time.time() 
        text = f"Result: {result}\nStart time: {start}\nEnd time: {end}\nDuration: {round(end-start,2)} seconds\n"
        return print(text)
    return wrapper

@decorator_time_it
def sum():
    x = int(input("number #1:" ))
    y = int(input("number #2:" ))
    z = f"{x} + {y} = {x+y}"
    return z

@decorator_time_it
def say_hello():
    return "Hello!"

sum()
say_hello()