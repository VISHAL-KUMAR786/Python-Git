x = int(input("Enter first number :"))
y = int(input("Enter secound number :"))
op = input("Enter the operation that you want to perform "+
            "+,-,/,%,*")

if x == 45 and y == 3 and op == '*':
    print("555")
elif x == 59 and y == 9 and op == '+':
    print("77")
elif x == 56 and y == 6 and op == '/':
    print("4")
elif op == '+':
    print(x+y)
elif op == '-':
    print(x-y)
elif op == '/':
    print(x/y)
elif op == '%':
    print(x%y)
elif op == '*':
    print(x*y)
else :
    print("Enter a valid value")
