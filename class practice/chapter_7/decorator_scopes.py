def outer_func():
    msg = "Weeeeeekend!"
    def inner_func():
        print(msg)
    return inner_func

outer_func()()          # Output: Weeeeeekend!
say_wee = outer_func()
say_wee()               # Output: Weeeeeekend!

def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func

outer_func("Hello world!")()                # Output: Hello world!
say_hello_world = outer_func("Hey you!")    
say_hello_world()                           # Output: Hey you!