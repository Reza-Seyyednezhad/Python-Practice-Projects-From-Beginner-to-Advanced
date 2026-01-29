# Implemented property setters to validate and control attribute values in an object-oriented class.

class User:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self , new_age):
        if not isinstance(new_age, int):
            raise ValueError("Age must be integer number ...")
        
        if new_age < 0 or new_age > 120:
            raise ValueError("Age range must between 0 and 120 ...")
        
        self._age = new_age

Reza = User(20)

print(Reza.age)

Reza.age = -25

print(Reza.age)