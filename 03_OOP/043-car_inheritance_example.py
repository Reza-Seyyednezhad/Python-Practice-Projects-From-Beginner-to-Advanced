class Car:
    def __init__(self, name:str, color:str, year:int, engine_type:str, type:str):
        self.name = name
        self.color = color
        self.year = year
        self.engine_type = engine_type
        self.type = type

class Micro(Car):
    def __init__(self, name:str, color:str, year:int, engine_type:str, type:str, model:str):
        self.model = model
        super().__init__(name, color, year, engine_type, type)
    
    def Display(self):
        print(f"Car Name: {self.name}, \nCar Model: {self.model}, \nCar Type: {self.type}, \nCar Engine Type: {self.engine_type}, \nCar Year: {self.year}, \nCar Color: {self.color},")

class CrossOver(Car):
    def __init__(self, name:str, color:str, year:int, engine_type:str, type:str, model:str):
        self.model = model
        super().__init__(name, color, year, engine_type, type)
    
    def Display(self):
        print(f"Car Name: {self.name}, \nCar Model: {self.model}, \nCar Type: {self.type}, \nCar Engine Type: {self.engine_type}, \nCar Year: {self.year}, \nCar Color: {self.color},")

matiz = Micro("matiz", "white", 2025, "V6", "Light Weight", "Micro")

# matiz.Display()

Santafe = CrossOver("Hyundai Santafe", "blue", 2020, "V8", "Off Road", "Cross Over")

# Santafe.Display()

class Coupe(Car):
    def __init__(self, name:str, color:str, year:int, engine_type:str, type:str, model:str, door:int):
        self.model = model
        self.door = door
        super().__init__(name, color, year, engine_type, type)
    
    def Display(self):
        print(f"Car Name: {self.name}, \nCar Model: {self.model}, \nCar Type: {self.type}, \nCar Engine Type: {self.engine_type}, \nCar Year: {self.year}, \nCar Color: {self.color}, \nCar Door: {self.door}")
        

Corvette = Coupe("Chevrolet Corvette C8", "yellow", 2024, "V8", "Sport", "Coupe", 2)

# Corvette.Display()