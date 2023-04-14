kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
vis = "this is my name"
har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]

sum1 = lambda x,y,z : x+y+z

def sum2(*args):
    return sum(args)

print(sum1(12,23,45))
print(sum2(12,23,45))
print(sum2(12,23,45,56))

# kwargs is dict
# args is list or tuple

def sum3(vishal,*args,**kwargs):

    print(vishal)
    print(args)
    print(kwargs.items())
    for item in args :
        print(f"item in args is {item}")

    for item,key in kwargs.items():
        print(f"item in kwargs is {item} and value is {key}")

sum3(vis,har,kw)
# this is my name
# item in args is ['Harry', 'Rohan', 'Skillf', 'Hammad', 'Shivam', 'The programmer']
# item in args is {'Rohan': 'Monitor', 'Harry': 'Fitness Instructor', 'The Programmer': 'Coordinator', 'Shivam': 'Cook'}
print()
sum3(vis,*har,**kw)


# theory 

# there are two type of argument 

# 1. positional arguments - are the one in which an order
# we have to know about asterisk or more commonly known in Perl 6 and ruby as a splat operator.

# Asterisk is used in python as a mathematical symbol for multiplication, but in case of arguments, it refers to unpacking. The unpacking could be for a list, tuple, or a dictionary. We will discover more about it by defining *args and **kwargs.

# 2. keyword arguments

# Note that the name args does not make any difference, we can use any other name, such as *myargs. The only thing that makes a difference is the Asterisk(*).

# **kwargs is keyword arguments. It passes the data to the argument in the form of a dictionary

