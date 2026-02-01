# “Used type hints to clarify function contracts and improve code readability and maintainability.”

def multi(num1: float, num2: float) -> float:
    return num1 * num2



def library_management_system(book_id: str, book_title: str, book_author: str, book_year: int, book_is_available: bool) -> dict:
    book_data: dict = {
        "book_id": book_id,
        "book_title": book_title,
        "book_author": book_author,
        "book_year": book_year,
        "book_is_available": book_is_available
    }
    
    return book_data



def add_book_to_library(library: list, book_info: dict) -> list:
    library.append(book_info)
    return library