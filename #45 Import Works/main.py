import sys 
import math
import file2

print(sys.path) # it is the hiearchy of searching module , we can also change it
# sys.path prints out a list of directories. When we tell Python to import something, then it looks in each of the listed locations in order. 
print(math.factorial(5))
print(file2.a)
file2.fun("vishal")


# import math as m 
# it is not a best practive as importing m

# Disadvantages:
# One of the major disadvantages of the flexibility provided by a python in the case of modules is that they can be easily modified and overridden. Along with disrupting the functionality of the program, it also poses a major security risk.