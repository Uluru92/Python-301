import time

def decorator_time_it(init_func):
    def wrapper():
        start = time.time()
        end = time.time()
        text = f"{init_func()} - start time: {start} - end time: {end}"
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
