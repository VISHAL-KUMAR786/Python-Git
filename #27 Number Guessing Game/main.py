import random

main = random.randint(0,100)

noChance = 9

print("Welcome to Number Guess Game 🎮🎳🎲🏓🏸🕹🎴♣🏏🏐🏑🏒🎱🃏")
# print(main)
while noChance:
    n = int(input("Enter a number"))
    if n == main :
        print("you won 🥇")
        break
    elif n < main :
        print("You guess too low ")
        print("try again")
    else :
        print("You guess too high ")
        print("try again")
    noChance -=1