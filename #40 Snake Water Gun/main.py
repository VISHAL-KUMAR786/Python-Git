# snake water gun
import random

print("Welcome to snake-water-gun Game😊")
computers , xs = 0 , 0
chance = 10

while chance :
    l1 = ['S','W','G']
    computer = random.choice(l1)
    print("Press S for snake")
    print("Press W for water")
    print("Press G for gun")
    x = input()
    if x.lower() == 's':
        if computer.lower() == 'w':
            print("snake drink water, You Win 🎉")
            xs +=1 
        elif computer.lower() == 'g':
            print("Gun will kill the snake, Computer Win 🎊")
            computers +=1
        elif computer.lower() == 's':
            print('XXX-XXXX--Draw--XXXX-XXX')
    elif x.lower() == 'w':
        if computer.lower() == 's':
            print("Snake drinks the water, Computer Win 🎉")
            computers +=1
        elif computer.lower() == 'w':
            print('XXX-XXXX--Draw--XXXX-XXX')
        elif computer.lower() == 'g':
            print("gun will drown in water, You Win 🎊")
            xs +=1 
    elif x.lower() == 'g':
        if computer.lower() == 'w':
            print("gun will drown in water, Computer Win 🎉")
            computers +=1
        elif computer.lower() == 's':
            print("Gun will kill the snake, You Win 🎊")
            xs +=1 
        elif computer.lower() == 'g':
            print('XXX-XXXX--Draw--XXXX-XXX')

    chance -= 1

print(f"At last score of you is {xs} and computer is {computers}")
if xs > computers :
    print("\nYou win this game🎉")
elif xs < computers :
    print("\ncomputer win this game🎊")
elif (xs == computers):
    print("\n draw on both side")
else: 
    pass
