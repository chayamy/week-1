"""""
ex3- print stars
"""

stars = int(input("please enter a number "))
mon = 0
noS = stars-1
numStars = 1
j = 0

for i in range(1, stars+1):

    while j < noS:
        print(f" ", end="")
        j += 1
    noS -= 1
    j = 0

    while mon < numStars:
        print(f"*", end="")
        mon += 1
    numStars += 2
    print()
    mon = 0
