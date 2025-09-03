# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def decorator_censor_specific_word(*args):
    """Decorator factory that censors given words + default ones"""
    def decorator_quotes(func):
        def wrapper(text):
            CENSOR_WORDS = [ 
            "bitch", 
            "damn", 
            "hell", 
            "bastard", 
            "douche", 
            "asshole", 
            "jackass"
            ]
            result_text = func(text)
            for arg in args:
                result_text = result_text.replace(arg, "****")
            for word in CENSOR_WORDS:
                result_text = result_text.replace(word, "****")
            return result_text
        return wrapper
    return decorator_quotes

@decorator_censor_specific_word("shoot", "crap")
def say_something(text):
    return text

print(say_something("You are a jackass and full of crap!"))
print(say_something("Hello you damn bastard son of a bitch, please go to hell you douche damn asshole"))