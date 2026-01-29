class Bank_Account:
    def __init__(self, name:str, username:str, password:str, account_value:float):
        self.name = name
        self.username = username
        self.password = password
        self.account_value = account_value
    
    def Show_info(self):
        print(f"Hello {self.name}, \nYou have {self.account_value}$ in your account.")
    
    def Deposit(self):
        print(f"You have {self.account_value}$ in your account.")
        user_deposit_value = float(input(f"How much do you want deposit into your account? "))
        user_password_auth = str(input(f"Enter your password: "))
        if user_password_auth == self.password:
            self.account_value += user_deposit_value
            print(f"Deposit Successful, You have {self.account_value}$ in your account.")
        else:
            print("Password is wrong.")
    
    def Harvest(self):
        print(f"You have {self.account_value}$ in your account.")
        user_harvest_value = float(input(f"How much do you want harvest from your account? "))
        if user_harvest_value > self.account_value:
            print("You don't have enough money in your account.")
        else:
            user_password_auth = str(input(f"Enter your password: "))
            if user_password_auth == self.password:
                self.account_value -= user_harvest_value
                print(f"Harvest Successful, You have {self.account_value}$ in your account.")
            else:
                print("Password is wrong.")

user_1 = Bank_Account("Reza", "reza_seyyed", "123456789", 1250)
# user_1.Show_info()

# user_1.Deposit()

# user_1.Harvest()