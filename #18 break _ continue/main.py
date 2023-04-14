i = 0 
while True :
    print(f"The value of i is {i}")
    i +=1
    if(i>10):
        print(f"Breaking the loop is {i}")
        break

print("\n starting of new while loop\n")

i = 0
while True:

    if i == 5 :
        i +=1
        continue

    print(f"the value of i is {i}")

    if i > 10:
        print("Breaking of the loop")
        break

    i += 1

print("\n Playing with the game \n")

while True:
    x = int(input("Enter a number"))
    if x > 100 :
        print("you win 🥇🏆 you have enter a value greater than 100")
        break
    else :
        print("Try again")
        continue