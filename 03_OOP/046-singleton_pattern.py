# Implemented Singleton Design Pattern to ensure a single shared instance for global configuration management.

"""
Docstring for 03_OOP.046-singleton_pattern

Exercise: Implementing the Singleton Design Pattern in Python

In this exercise, a Singleton class is implemented to ensure that only one instance of the class can exist throughout the entire application lifecycle.

The purpose of this implementation is to control object creation and provide a single, globally accessible instance. This design pattern is especially useful in scenarios such as configuration managers, logging systems, database connections, or any shared resource that must be centralized.

The class overrides the object creation process to check whether an instance has already been created. If an instance already exists, the existing object is returned instead of creating a new one. Otherwise, a new instance is created and stored for future use.

This implementation guarantees that all variables referencing this class will point to the same object in memory, ensuring consistency and efficient resource management across the application.

Key objectives of this exercise:

Prevent multiple instances of a class from being created

Provide a single shared instance across the entire program

Demonstrate understanding of object-oriented design patterns

Apply controlled instance creation using class-level attributes
"""

class Singleton:
    _instance = None  

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()

print(a is b)   # True