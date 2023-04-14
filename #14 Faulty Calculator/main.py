'''
# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

'''


while True :

    a = int(input("👉 Enter First Number : ").strip())
    b = int(input("👉 Enter Secound Number : ").strip())
    op = input("🤞 Enter Operation to be performed : ").strip()

    if a == 45 and b == 3 and op == '*':
        print(f"Multiplication of {a} and {b} is 555")
    elif a == 56 and b == 9 and op == '+':
        print(f"Addition of {a} and {b} is 77")    
    elif a == 56 and b == 6 and op == '/':
        print(f"Division of {a} and {b} is 4")
    elif op == '+':
        print(f"Addition of {a} and {b} is {a+b}")
    elif op == '-':
        print(f"Subtraction of {a} and {b} is {a-b}")
    elif op == '*':
        print(f"Multiplication of {a} and {b} is {a*b}")
    elif op == '/':
        print(f"Division of {a} and {b} is {a/b}")
    else:
        print("Please Enter a valid Input 😭")

    if input("Press 'q' to Quit or 'c' to Continue : ") == 'q':
        break
    else:
        continue