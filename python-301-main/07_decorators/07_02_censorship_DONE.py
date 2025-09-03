# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

def decorator_quotes(func):
    """A decorator that censors potentially offensive words from a text"""
    def wrapper(text):
        CENSOR_WORDS = [ 
        "shoot", 
        "bitch", 
        "damn", 
        "crap", 
        "hell", 
        "bastard", 
        "douche", 
        "asshole", 
        "jackass", 
        "son of a bitch"
        ]
        result_text = func(text)
        for word in CENSOR_WORDS:
            result_text = result_text.replace(word, "****")
        return result_text
    return wrapper

@decorator_quotes
def say_something(text):
    return text

print(say_something("You are a jackass and full of crap!"))