def repeat_output(times):
    """Decorator factory: repeats the output 'times' times"""
    def decorator_func(initial_func):
        def wrapper_func(*args, **kwargs):
            for i in range(times):
                result = initial_func(*args, **kwargs)
            return result  # return last result
        return wrapper_func
    return decorator_func

@repeat_output(4)
def greet(name):
    print(f"Hello, {name}!")
    return f"Hello, {name}!"

@repeat_output(2)
def add(a, b):
    print(f"Sum: {a + b}")
    return a + b

greet("Alice")
add(3, 4)