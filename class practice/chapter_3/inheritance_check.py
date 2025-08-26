class Class1:
   def __init__(self):
     self.x = 5

class Class2(Class1):
   def __init__(self):
     self.y = 1

b = Class2()
print(b.y + b.x)
