def decorator_repeat_twice(init_func):
    def wrapper():
        result = init_func()
        print(result)
        print(result)
        return result
    return wrapper

@decorator_repeat_twice
def say_hello():
    return "Hello!"

@decorator_repeat_twice
def apples():
    return "apples"

@decorator_repeat_twice
def sum():
    x = int(input("number #1:" ))
    y = int(input("number #2:" ))
    z = f"{x} + {y} = {x+y}"
    return z

say_hello()
apples()
sum()