import math
x = 'saste coder'
y = 15
mystr = "this is my content %s"%x
print(mystr)

mystr = "a no is %d and name is %s"%(y,x)
print(mystr)

mystr ="this is one of my wish {}".format(x)
print(mystr)

mystr ="this is one of my wish {} {}".format(x,y)
print(mystr)

mystr ="this is one of my wish {1} {0}".format(x,y)
print(mystr)

mystr = f"name is {x} and age is {y}"
print(mystr)

k = int(input("Enter the angle of cos"))
print(f"the value of {k} in cos is {math.cos(k)}")