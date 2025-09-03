# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate_with_symbol(symbol):    
    def decorator_text(initial_func):
        def wrapper_func(*args):
            decorated_text = (f"{symbol}"*50)+(f"\n{initial_func(*args)}\n")+(f"{symbol}"*50)
            return decorated_text
        return wrapper_func
    return decorator_text

@decorate_with_symbol("*")
def prettify(msg):
    return msg

@decorate_with_symbol("-")
def feed(carbs, protein):
    return f"{carbs} and {protein}"

print(prettify("Hello!"))
print(feed("beans","beef"))
