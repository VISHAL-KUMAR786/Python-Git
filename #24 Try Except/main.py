x = int(input("Enter first number \n"))
y = int(input("Enter secound number \n"))

try:
    z = int(x) / int(y)
    print(f"Division of two number is {z}")
except Exception as e:
    print(e)
print("I am last line")