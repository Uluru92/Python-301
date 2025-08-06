# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

# Solution

class DoctorForm:
    """Doctor's form."""
    def __init__(self, name:str, age:int, weight:int, height:int, new_patient:bool):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.new_patiend = new_patient

    def __str__(self):
        first_time = "Yes" if self.new_patiend == True else self.new_patiend == "No"
        return f"\nPatient name: {self.name}\nAge: {self.age} years\nWeight: {self.weight} kg\nHeight: {self.height} cm\nNew patient: {first_time}\n"

Jorddy = DoctorForm("Jorddy", 33, 65, 171, True)
Ryan = DoctorForm("Ryan", 45, 75, 178, False)

print(Jorddy)
print(Ryan)