from datetime import *
import os

os.system("cls")
def reminder_app():
    print("Hello my friend ... Welcome to My Reminder :)")
    print("Are you ready for do your works on time? ")
    print(f"Today: {str(datetime.now()).split(".")[0]}")
    print("===============")
    user_input_task = str(input("TASK name to REMIND: "))
    user_input_date = str(input("Enter DATE (Year-Month-Day (Ex. 2026-10-19)) you want to remind it: "))
    user_input_time = str(input("Enter Time (Hour-Minute-Second (Ex. 21-13-55)) you want to remind it: "))
    user_year, user_month, user_day = user_input_date.split("-")
    user_hour,user_minute, user_second = user_input_time.split("-")
    print("===============")
    mydate = datetime.now()
    now_date = str(mydate).split(" ")[0]
    year, month, day = now_date.split("-")
    now_time = str(mydate).split(" ")[-1].split(".")[0]
    hour, minute, second = now_time.split(":")
    now_datetime = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), 0)
    user_datetime = datetime(int(user_year), int(user_month), int(user_day), int(user_hour), int(user_minute), int(user_second), 0)
    print(f"Today: {now_datetime}")
    print(f"Your date to set: {user_datetime}")
    print("===============")
    if user_datetime == now_datetime:
        print("============== REMIND ==============")
        print(f"TASK: {user_input_task}")
        print("It's time to do your task.....")
    else:
        print(f"Task: {user_input_task}")
        print(user_datetime - now_datetime)
    
reminder_app()
