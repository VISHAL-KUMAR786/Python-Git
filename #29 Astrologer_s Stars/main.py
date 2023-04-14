x = int(input("Enter a number"))
boolean = bool(int(input("Enter a number in form of bool")))

if boolean == True:
    for i in range(x):
        for j in range(i+1):
            print("*",end="")
        print()
elif boolean == False:
    for i in range(x):
        for j in range(x-i):
            print("*",end="")
        print()


a = int(input("please add number of line you want to print"))
b = bool(int(input("please add 0 for False")))


def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a - 1


star(a, b)