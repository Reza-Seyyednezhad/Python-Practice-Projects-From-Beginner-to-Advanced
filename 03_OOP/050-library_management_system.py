"""
Docstring for 03_OOP.050-library_management_system

Mini Project: Library Management System
Design a small Library Management System using Python and Object-Oriented Programming.

Requirements:

Create a Book data class with the following attributes:
id (str)
title (str)
author (str)
is_available (bool)


Create a Library class that:
Stores a list of books
Can add a new book
Can remove a book by name
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

from dataclasses import dataclass
import json
from random import sample
from time import sleep

class BookNotFoundError(Exception):
    pass

class BookNotAvailableError(Exception):
    pass

class BookAddedError(Exception):
    pass

class BookSearchError(Exception):
    pass

class BookRemoveError(Exception):
    pass

def generate_book_id():
    random_id_samples = sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 4)
    return "".join(random_id_samples)
      
def get_data_from_json_file():
    with open("./files/library-database.json", 'r') as f1:
        data:dict = json.loads(f1.read())
    return data
     
@dataclass
class SetBookInfo:
    book_title: str
    book_author: str
    book_isAvailable: str
        
        
    def add_book_info_to_data_dict(self):
        data = get_data_from_json_file()
        data[self.book_title] = {"ID": generate_book_id(), "Author": self.book_author, "Available": self.book_isAvailable}
        return data
    
    def update_database(self):
        data = self.add_book_info_to_data_dict()
        with open("./files/library-database.json", 'w') as f1:
            f1.write(json.dumps(data))

@dataclass
class RemoveBook:
    book_title:str
    
    def get_all_book_names_from_database(self):
        data = get_data_from_json_file()
        get_books_name = [book_name for book_name in data.keys()]
        return get_books_name
    
    def check_book_search_result_and_remove_book(self):
        book_names_list = self.get_all_book_names_from_database()
        if self.book_title in book_names_list:
            print(f"FINISH... \n{self.book_title} found in Book Lists...")
            data = get_data_from_json_file()
            print(f"{self.book_title}: \nBook ID: \t {data[self.book_title]["ID"]}\nBook Author: \t {data[self.book_title]["Author"]}\nBook Availability: \t {data[self.book_title]["Available"]}")
            question_for_removing = str(input(f"Do You Want to Remove <{self.book_title}> book (y/n): "))
            if question_for_removing == "y":
                del data[self.book_title]
                with open("./files/library-database.json", 'w') as f1:
                    f1.write(json.dumps(data))
            else:
                print("You Remove Nothing from Library")
        else:
            raise BookNotFoundError("404 NOT FOUND :)\nCannot found Book.")

        
@dataclass
class Book_Search:
    book_title: str
    
    
    def get_all_book_names_from_database(self):
        data = get_data_from_json_file()
        get_books_name = [book_name for book_name in data.keys()]    
        return get_books_name
    
    def check_book_search_result(self):
        book_names_list = self.get_all_book_names_from_database()
        if self.book_title in book_names_list:
            print(f"FINISH... \n{self.book_title} found in Book Lists...")
            data = get_data_from_json_file()
            print(f"Book Name: \t {self.book_title}\nBook ID: \t {data[self.book_title]["ID"]}\nBook Author: \t {data[self.book_title]["Author"]}\nBook Availability: \t {data[self.book_title]["Available"]}")
        else:
            raise BookNotFoundError("404 NOT FOUND :)\nCannot found Book.")
    
    
    def check_book_availability(self):
        book_names_list = self.get_all_book_names_from_database()
        if self.book_title in book_names_list:
            print(f"FINISH... \n{self.book_title} found in Book Lists...")
            data = get_data_from_json_file()
            if data[self.book_title]["Available"] == "True":
                print(f"{self.book_title} is Available... :)")
            else:
                raise BookNotAvailableError("SORRY! THE BOOK IS NOT AVAILABLE RIGHT NOW...")
        else:
            raise BookNotFoundError("404 NOT FOUND :)\nCannot found Book.")


def library_management_cli():
    while True:
        user_input_menu  = int(input("Enter one of these options: \n\t1. Add new book to library\n\t2. Remove Book from library \n\t3. Search book name \n\t4. Book Availability\n\nWhich one (Just Type Number 1 to 4): "))
        if user_input_menu == 1:
            print("ADD NEW BOOK TO LIBRARY SECTION")
            user_input_book_title = str(input("Enter Book Title: "))
            user_input_book_author = str(input("Enter Book Author(s): "))
            user_input_book_availability =  str(input("Enter Book Availability (True or False): "))
            try:
                user_new_book_add = SetBookInfo(user_input_book_title, user_input_book_author, user_input_book_availability)
                print(f"Your Data is: \n {user_new_book_add.add_book_info_to_data_dict()}")
                print(f"Adding New Book to Library... \n\tPlease Wait ...")
                sleep(2)
                user_new_book_add.update_database()
                print("Adding Progress Successful.")
                
            except:
                raise BookAddedError("Something went wrong...\n Cannot add book into library\n  Please try again later.")
            return True
        
        elif user_input_menu == 2:
            print("REMOVE BOOK FROM LIBRARY SECTION")
            user_input_book_title_to_remove = str(input("Enter Book Title to Search and Remove From Library: "))
            try:
                user_book_remove = RemoveBook(user_input_book_title_to_remove)
                print(f"You Search Book Name: {user_book_remove}\n\t Please Wait ...")
                sleep(2)
                print(f"Search Progress Done.")
                user_book_remove.check_book_search_result_and_remove_book()
                print("Removing Progress Successful.")
                
            except:
                raise BookRemoveError("Something went wrong...\n Cannot remove book from library\n  Please try again later.")
            
            return True
                
        elif user_input_menu == 3:
            print("SEARCHING BOOK FROM LIBRARY SECTION")
            user_input_book_name_to_search = str(input("Enter Book Title to Search: "))
            try:
                user_search_book_name = Book_Search(user_input_book_name_to_search)
                print(f"You Search Book Name: {user_input_book_name_to_search}\n\t Please Wait ...")
                sleep(2)
                print(f"Search Progress Done.")
                user_search_book_name.check_book_search_result()
                print("Searching Progress Successful.")
                
            except:
                raise BookSearchError("Something went wrong...\n Searching Progress Failed...\n  Please try again later.")
            
            return True
        
        
        elif user_input_menu == 4:
            user_input_book_name_availability = str(input(f"Enter Book Name to Check Availability: "))
            try:
                user_availability_book_name = Book_Search(user_input_book_name_availability)
                print(f"You Search Book Name for Availability: {user_availability_book_name}\n\t Please Wait ...")
                sleep(2)
                print(f"Progress Done.")
                user_availability_book_name.check_book_availability()
                print("Searching and Availability Progress Successful.")
                
            except:
                raise BookSearchError("Something went wrong...\n Searching Progress Fail...\n  Please try again later.")
            
            return True
                


if __name__ == "__main__":
    library_management_cli()
            
        