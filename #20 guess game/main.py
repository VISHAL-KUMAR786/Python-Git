guess = 101
while True :
    x = int(input("Enter any intiger value : "))
    if x == guess :
        print("You win 🥇🏆")
        break
    elif x > guess :
        print("Try again You have enter greater value")
        continue
    else :
        print("Try again You have enter smaller value")
        continue    