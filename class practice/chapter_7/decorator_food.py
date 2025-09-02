def decorator_food(initial_func):
    def wrapper_func():
        name = input("What is your name?: ")
        text = f"Here is some {initial_func()} for you {name}"
        return print(text)
    return wrapper_func

@decorator_food
def apples():
    return "apples"

@decorator_food
def pizza():
    return "pizza"

apples()
pizza()
