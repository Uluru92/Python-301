# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

# Solution

class Car():
    def __init__(self,model:str,year:int,max_speed:int):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def acelerate(self):
        self.max_speed = self.max_speed + 5
        return self.max_speed
    
    def __str__(self):
        return (
            f'\n- Details of this car -'
            f'\nModel: {self.model}'
            f'\nYear: {self.year}'
            f'\nMax speed: {self.max_speed} km/h\n'
        ) 
    pass

car_1 = Car("Nissan", 1992, 120)
car_2 = Car("Toyota", 1998, 135)
car_3 = Car("Jaguar", 2023, 310)

print(car_1, car_2, car_3)

# Lets accelerate these cars...

car_1.acelerate() # max speed to 125
car_1.acelerate() # max speed to 130
car_1.acelerate() # max speed to 135
car_1.acelerate() # max speed to 140

car_2.acelerate() # max speed to 140

car_3.acelerate() # max speed to 315

print(car_1, car_2, car_3)