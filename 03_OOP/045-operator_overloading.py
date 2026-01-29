#  Implemented custom operator overloading to allow arithmetic and comparison operations between class instances.

class Employee:
    def __init__(self, age , salary):
        self._age = age
        self._salary = salary
        

    def __add__(self, other):
        return Employee((self._age + other._age)/2, self._salary + other._salary)
    
    def __eq__(self, other):
        return self._age == other._age and self._salary == other._salary
    
    def __str__(self):
        return f"({self._age}, {self._salary})"
    
user_1 = Employee(28, 12600)
user_2 = Employee(32, 29000)

summation_12 = user_1 + user_2

print(summation_12)

print(user_1 == user_2)

user_3 = Employee(28, 12600)
user_4 = Employee(28, 29000)

summation_34 = user_3 + user_4

print(summation_34)

print(user_3 == user_4)