"""
Docstring for 03_OOP.049-save_objects_to_json

Exercise: Saving and Loading Python Objects to JSON Files

In this exercise, Python dataclasses are used to implement a simple system for saving and loading objects to and from JSON files.

The program defines two separate classes: one responsible for serializing Python dictionaries into JSON format and storing them in a file, and another responsible for reading JSON files and deserializing their contents back into Python objects. This separation of concerns improves code clarity and maintainability.

The implementation demonstrates how to use the built-in json module to convert structured data into JSON strings and persist them on disk, as well as how to safely load and parse JSON data from external files.

Key objectives of this exercise:

Serialize Python objects into JSON format

Save structured data into external JSON files

Load and deserialize JSON data back into Python dictionaries

Apply dataclasses to organize file handling logic

Practice clean separation between saving and loading responsibilities


"""



from dataclasses import dataclass
import json
@dataclass
class LoadJsonFile:
    json_file_url: str
    
    def extract_content(self):
        with open(self.json_file_url, "r") as f1:
            file_content = f1.read()
            json_file_content = json.loads(file_content)
        
        return json_file_content

@dataclass
class SaveObjectToJson:
    folder_url: str
    file_name: str
    file_content: dict
    
    def set_json_content(self):
        json_content = json.dumps(self.file_content)
        
        return json_content

    def save_json_file(self):
        url = f"{self.folder_url}/{self.file_name}.json"
        
        with open(url, "w+") as f1:
            f1.write(self.set_json_content())
    
    

# file_1 = LoadFile("./files/jsonFile.json")

# print(file_1.extract_content())


myDict = {
	"random": "38",
	"random float": "31.634",
	"bool": "true",
	"date": "1980-10-29",
	"regEx": "helloooooo to you",
	"enum": "online",
	"firstname": "Tierney",
	"lastname": "Bandeen",
	"city": "Bandung",
	"country": "Guyana",
	"countryCode": "TV",
}


Save_myDict_as_JSON = SaveObjectToJson("./files", "Example", myDict)

# Save_myDict_as_JSON.save_json_file()


LoadExampleJsonFile = LoadJsonFile("./files/Example.json")

# print(LoadExampleJsonFile.extract_content())
# print(LoadExampleJsonFile.extract_content()["firstname"])
