"""""
ex3- print stars
"""

stars = int(input("please enter a number "))
mon = 0

for i in range(1,stars+1):

    while mon < i:
        print(f"*", end="")
        mon += 1

    print()
    mon = 0
