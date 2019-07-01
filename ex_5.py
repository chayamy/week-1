"""""
ex5- calculator
"""


def waiting_for_number(every):
    while True:
        try:
            return int(input(every))
        except ValueError:
            pass


def resul(num1, oper, num2):
    result = 0
    if oper == '+':
        result = num1 + num2
    elif oper == '*':
        result = num1 * num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '/':
        result = num1 / num2
    elif oper == '^':
        result = num1 ** num2
    else:
        raise ("oper Error")
    print(f"{num1} {oper} {num2} = {result}")


def waiting_for_number(every):
    while True:
        try:
            return int(input(every))
        except ValueError:
            pass


num1 = waiting_for_number("enter a number ")
oper = input("enter +, -, *, /, ^ ")
num2 = waiting_for_number("enter a number ")

try:
    resul(num1,oper,num2)
except Exception:
    print("Invalid operator!")
