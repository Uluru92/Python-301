def add_message_from(name):    
    def decorator_func_with_argument(initial_func):
        def wrapper_func(*args):
            print(f"{name} picked some ")
            return initial_func(*args)
        return wrapper_func
    return decorator_func_with_argument

@add_message_from("Zeek")
def prettify(msg):
    print(msg)

@add_message_from("Nature")
def feed(carbs, protein):
    print(f"{carbs} and {protein}")

prettify("flowers for you")
feed("bread", "lentils")