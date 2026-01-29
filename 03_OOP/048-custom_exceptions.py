"""
Docstring for 03_OOP.048-custom_exceptions

Exercise: Implementing Custom Exception Handling in Python

In this exercise, custom exception classes are created to handle application-specific error conditions that cannot be adequately represented by built-in Python exceptions.

The objective of this task is to design meaningful and descriptive error types by defining custom exceptions that inherit from the base Exception class. These exceptions are raised when invalid conditions occur, such as incorrect user input, insufficient resources, or logical rule violations.

The program demonstrates how to raise custom exceptions in controlled situations and handle them gracefully using structured try / except blocks. This approach improves error clarity, program robustness, and overall maintainability by separating application-level errors from system-level exceptions.

Key objectives of this exercise:

Define custom exception classes for domain-specific errors

Raise meaningful exceptions using the raise statement

Handle custom exceptions with structured try / except blocks

Improve code reliability and readability through explicit error handling
"""
from dataclasses import dataclass



class InvalidAgeError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass


@dataclass
class CreateAccount:
    user_name: str
    user_age: int
    user_email: str
    user_password: str

    def validate_age(self):
        if self.user_age <= 0:
            raise InvalidAgeError("User age cannot be zero or a negative number.")

    def validate_email(self):
        if "@" not in self.user_email:
            raise InvalidEmailError("User email is not valid.")

    def validate_password(self):
        if len(self.user_password) < 8:
            raise InvalidPasswordError("User password must contain at least 8 characters.")

    def validate_all(self):
        self.validate_age()
        self.validate_email()
        self.validate_password()


user_1 = CreateAccount("user1", 15, "user@gmail.com", "123456789")

# user_1.validate_all()

user_2 = CreateAccount("user2", "15", "user@gmail.com", "123456789")

# user_2.validate_all()

user_3 = CreateAccount("user2", 15, "user$gmail.com", "123456789")

# user_3.validate_all()

user_4 = user_2 = CreateAccount("user2", 15, "user@gmail.com", "123")

# user_4.validate_all()