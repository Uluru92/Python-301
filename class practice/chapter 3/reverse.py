class NotReverse:
    def __init__(self,data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index += 1
        return self.data[self.index-1]
    
Jorddy = NotReverse("Jorddy")
 
for char in Jorddy: # iter & next... makes the objet iterable...
    print(char)

print("\nNow lets make it Reverse:\n")

class Reverse:
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index =  self.index-1
        return self.data[self.index]

Jorddy = Reverse("Jorddy") # Make a class Reverse called Jorddy
for char in Jorddy: # iter & next... makes the objet iterable and its own iterator... the thing is we modidy this methods to go throught in reverse
    print(char)

print("\nNow lets use a built in function: reversed:\n")

for char in reversed("Jorddy"):
    print(char)

print("\nNow lets use a GENERATOR:\n")

def ReverseGenerater(data):
    for i in range(len(data)-1,-1,-1):
        yield data[i] # if we use return instead of yield... it will capture the last char and returns in that moment... that's the key in using yield, that it will go thorugh all the chars and then return the whole

for i in ReverseGenerater("Jorddy"):
    print(i)

