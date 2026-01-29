"""
Docstring for 03_OOP.047-dataclass_example

Exercise: Using Python Dataclasses for Data Modeling

In this exercise, a data-oriented class is implemented using Python’s @dataclass decorator to simplify class creation and improve code readability.

The goal of this task is to design a clean and efficient data model by defining class attributes without manually writing boilerplate methods such as __init__, __repr__, and __eq__. The dataclass decorator automatically generates these methods, allowing the developer to focus on the data structure itself.

This exercise demonstrates how dataclasses can be used to represent structured data objects such as students, employees, or products, while supporting object initialization, comparison, and readable string representation with minimal code.

Key objectives of this exercise:

Define a data model using the @dataclass decorator

Automatically generate initialization and comparison methods

Create and manipulate multiple instances of the class

Improve code clarity and maintainability using modern Python features

"""



from dataclasses import dataclass

@dataclass
class Car:
    model: str
    year: int
    is_stock: bool
    engine_type: str
    
    


chevrolet = Car("Corvette C8", 2023, False, "V8")

print(chevrolet.model)

@dataclass
class Product:
    product_id: int
    product_name: str
    product_count: int
    product_price: float


