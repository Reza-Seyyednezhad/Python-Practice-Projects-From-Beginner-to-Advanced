def palindrome_checker(text:str):
    return text == text[::-1]
print(palindrome_checker("radar"))
