
"""""
ex2- check if the numbers is sum
"""

d1 = int(input("enter num 1 "))
d2 = int(input("enter num 2 "))
d3 = int(input("enter num 3 "))

if d1+d2 == d3 or d1+d3 == d2 or d2+d3 == d1:
    print("yes the num is sum!")
else:
    print("no the num is not sum :(")
