# what is decorator ?

# A decorator takes a function and inserts some new functionality in it without changing the function itself. A reference to a function is passed to a decorator, and the decorator returns a modified function. The modified functions usually contain calls to the original function. This is also known as metaprogramming because a part of the program tries to modify and add functionality to another part of the program at compile time.

# what is wrapper ? 
# A wrapper is a function that provides a wrap-around another function While using decorator, all the code executed before our function that we passed as a parameter and the code after it is executed belongs to the wrapper function.


# NOTE  
# A function can be decorated many times. 
# Note that a decorator is called before defining a function.


# There are two ways to write a Python decorator:

# We can pass our function to the decorator as an argument, thus defining a function and passing it to our decorator.
#  We can simply use the @ symbol before the function we’d like to decorate.


def func1():
    print("Hi my name is anabella")
    return 0

func2 = func1
# this show error func2 = func1()
del func1
func2()

print()

def executor(func):
    func("this")

print("one")
executor(print)

print()

# def inner1(func):
#     # joo function nest kiya ha use return kar diya
#     def inner2():
#         print("Before")
#         func()
#         print("after")
#     return inner2

# @inner1
# def woo():
#     print("This is my content")
# woo()

def thisInner1(function):
    def thisInner2():
        print("This before the statement")
        function()
        print("This is after the statement")

    return thisInner2

def funk():
    print("Hi my name is khan ")

a = thisInner1(funk)
print(a())

print()

vishal = thisInner1(funk)
vishal()