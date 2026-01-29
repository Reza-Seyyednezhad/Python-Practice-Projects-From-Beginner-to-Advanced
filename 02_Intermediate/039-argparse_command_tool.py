import argparse
import os
os.system("cls")

def get_args():
    parser =  argparse.ArgumentParser(description="Math Operating between two number")
    parser.add_argument('--firstNumber',default=0, type=float, help="First Number")
    parser.add_argument('--secondNumber',default=0, type=float, help="Second Number")
    parser.add_argument("Operate", type=str, help="Operate Symbol (+,-,*,/)")

    return parser.parse_args()

def simple_calc(arg):
    num1 = arg.firstNumber
    num2 = arg.secondNumber
    
    if arg.Operate == "+":
        print(f"{num1} + {num2} = {num1 + num2}") 
    elif arg.Operate == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif arg.Operate == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    else:
        if num2 == 0:
            print(f"Cannot Division to Zero, Please Write Float Number, Not 0")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")


if __name__ == "__main__":
    args = get_args()
    simple_calc(arg=args)

