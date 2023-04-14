# from goto import goto, label
def datetime():
    import datetime
    return datetime.datetime.now()

def Diet_Excercise(name,x):
    if x == 1:
        f1 = open(f"#32 health management system/{name}-Diet.txt","w")
        print(f"Enter the diet of the {name}")
        diet = input()
        date = datetime()
        string = f"date => {date} , Diet => {diet}"
        f1.write(string)
        f1.close()
        # goto.Menu
    elif x == 2:
        f1 = open(f"#32 health management system/{name}-Excercise.txt","w")
        print(f"Enter the Excercise of the {name}")
        Excercise = input()
        date = datetime()
        string = f"date => {date} , Diet => {Excercise}"
        f1.write(string)
        f1.close()
        # goto.Menu
    else:
        print("Please Enter a valid data")

# label.Menu
print("Enter the name (Harry,Rohan,Hammad): ")
name = input()
print("What you want to log- Diet or Exercise :")
print("For log- Diet Press 1 :")
print("For Exercise Press 2 :")
print("For Quit Press 3 :")
x = int(input())
while x==True:
    if name == 'Harry':
        print(f"Welcome {name}")
        Diet_Excercise(name,x)
        x = False

    elif name == 'Rohan':
        print(f"Welcome {name}")
        Diet_Excercise(name,x)
        x = False

    elif name == 'Hammad':
        print(f"Welcome {name}")
        Diet_Excercise(name,x)
        x = False

    elif x == 3:
        print("Thank you for visiting")
        x = False
        quit()
    else:
        print("you have enter wrong input please try again")
        x = False
        quit()
