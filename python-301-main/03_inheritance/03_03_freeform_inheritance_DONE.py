# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Male(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sex = "Male"
        self.age_category = "Adult"

class Female(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sex = "Female"
        self.age_category = "Adult"

class Girl(Female):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.age_category = "Under Age"

class Boy(Male):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.age_category = "Under Age"

# Lets create some humans:
human_1 = Male("Roberto", 64)
human_2 = Female("Maria", 84)
human_3 = Male("Jorddy", 33)
human_4 = Female("Carolina", 25)
human_5 = Female("Isabela", 34)
human_6 = Male("Josue", 8)
human_7 = Female("Jimena", 15)
human_8 = Female("Victoria", 5)
human_9 = Male("Brayan", 34)
human_10 = Female("Mariana", 3)
humans = [human_1, human_2, human_3, human_4, human_5, human_6, human_7, human_8, human_9, human_10]

# Lets create some girls and boys
boys = []
girls = []
for human in humans:
    if human.age < 18:
        human.age_category = "Under Age"
        if human.sex == "Female":
            girls.append(human)
        else:
            boys.append(human)

for girl in girls:
    print(f"{girl.name} is a {girl.age} years old in the {girl.age_category} category")

for boy in boys:
    print(f"{boy.name} is a {boy.age} years old in the {girl.age_category} category") 


