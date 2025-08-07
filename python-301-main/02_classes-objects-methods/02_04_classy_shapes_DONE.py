# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

class rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area_perimeter(self):
        surface = self.length * self.width
        perimeter = self.length*2+self.width*2
        print(f'\nThe area of the rectangule is: {surface} m2')
        print(f'The perimeter of the rectangule is: {perimeter} m\n')
        pass

class circle():
    def __init__(self,radius):
        self.radius = radius
    
    def area_perimeter(self):
        surface = 3.1415*self.radius*self.radius
        perimeter = 2*3.1415*self.radius
        print(f'\nThe area of the circle is: {surface} m2')
        print(f'The perimeter of the circle is: {perimeter} m\n')
        pass


# Lets create some objects with these shapes...!
door = rectangle(2,6)
pizza = circle(3)

# Lets use polymorphism for these shapes...! 
door.area_perimeter()
pizza.area_perimeter()