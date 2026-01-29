class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    
    def show_info(self):
        print(f"Hello {self.name}\nyou have {self.age} years old and \nYour id number is {self.id}")
        

Person_1 = Person("Reza", 25, 123456789)
# Person_1.show_info()

Person_2 = Person("Abolfazl", 24, 987654321)
# Person_2.show_info()

Person_3 = Person("Meysam", 25, 159376482)
# Person_3.show_info()