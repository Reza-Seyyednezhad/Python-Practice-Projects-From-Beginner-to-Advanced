"""
Docstring for 03_OOP.050-library_management_system

Mini Project: Library Management System
Design a small Library Management System using Python and Object-Oriented Programming.

Requirements:

Create a Book data class with the following attributes:
id (int)
title (str)
author (str)
is_available (bool)


Create a Library class that:
Stores a list of books
Can add a new book
Can remove a book by id
Can borrow a book (set is_available to False)
Can return a book (set is_available to True)
Can display all books


Implement custom exceptions:
BookNotFoundError
BookNotAvailableError
Save and load the library data into/from a JSON file.


This project practices:
dataclasses
custom exceptions
file handling with JSON
basic object-oriented design

"""