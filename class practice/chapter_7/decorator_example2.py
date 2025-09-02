def say_hi():
    print("Hi.")

say_hi() # Output: Hi.

hey = say_hi

print(say_hi)       # Output: <function say_hi at 0x000001D3B0171440>
print(hey)          # Output: <function say_hi at 0x000001D3B0171440>
print(type(say_hi)) # Output: <class 'function'>
print(type(hey))    # Output: <class 'function'>

hey() # Output: Hi.

