def decorator_func(initial_func):
    def wrapper_func():
        text = input("Writhe something here: ")
        print(f"the wrapper function picked some... {text} and...")
        return initial_func()
    return wrapper_func


@decorator_func
def prettify():
    print("flowers for you")

prettify()
