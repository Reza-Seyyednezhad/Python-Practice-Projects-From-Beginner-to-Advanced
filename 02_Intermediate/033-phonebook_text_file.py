import json

def phonebook_text_file():
    with open(r'./files/phonebook_text_file.json', 'r+') as JsonPreData:
        getData = json.load(JsonPreData)
    userInput = str(input("Phone Book App. \n1.\tCreate(c)\n2.\tRead(r)\n3.\tUpdate(u)\n4.\tDelete(d)\nWhat is your Purpose? "))
    if userInput == "c":
        while True:
            print("Create new member (if you finish, just type 'exit' in username input)")
            username = str(input("Enter username: "))
            if username == "exit":
                break
            else:
                number = str(input("Enter number: "))
                if username == "" and number == "":
                    print("Username or User Number cannot be empty...")
                    break
                getData[username] = number
                with open(r'./files/phonebook_text_file.json', 'w') as SetNewJasonData:
                    SetNewJasonData.writelines(json.dumps(getData))
    elif userInput == "r":
        with open(r'./files/phonebook_text_file.json', 'r+') as ReadJsonData:
            getData = json.load(ReadJsonData)
            print(getData)
    elif userInput == "u":
        username = str(input("Enter username (if username does not exist, then we added to phone book as a new member): "))
        updated_number = str(input("Enter number: "))
        if updated_number == "":
            print("Username or User Number cannot be empty...")
        else:
            with open(r'./files/phonebook_text_file.json', 'r+') as UpdateJsonData:
                getData = json.load(UpdateJsonData)
            getData[username] = updated_number
            with open(r'./files/phonebook_text_file.json', 'w') as SetNewJasonData:
                SetNewJasonData.writelines(json.dumps(getData))
    elif userInput == "d":
        username = str(input("Enter username (if username does not exist, we delete no member): "))
        if username == "":
            print("You delete no user...")
        else:
            with open(r'./files/phonebook_text_file.json', 'r+') as UpdateJsonData:
                getData = json.load(UpdateJsonData)
            del getData[username]
            with open(r'./files/phonebook_text_file.json', 'w') as SetNewJasonData:
                SetNewJasonData.writelines(json.dumps(getData))
    else:
        print("Something went wrong.")

phonebook_text_file()