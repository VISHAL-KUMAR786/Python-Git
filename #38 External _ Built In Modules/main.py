from inspect import ClassFoundException
import random
import turtle
import datetime
import calendar
import math

print("using math function => ",math.cos(60))

random1 = random.randint(1,5)
print(random1)

random2 = random.random()
print(random2)

l1 = ["vishal","vivek","vijay","Beena"]
l1.sort()

t = turtle.Turtle()
for i in range(4):
    t.rt(90)
    t.fd(200)

myrandom = random.choices(l1)
print(myrandom) #return list

myrandom = random.choice(l1)
print(myrandom) #return value

myturtle = turtle.Turtle()

myturtle.right(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.backward(100)

t = turtle.Turtle()
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

mydate = datetime.datetime(2022,4,17)
print(mydate)

c = calendar.TextCalendar(calendar.THURSDAY)
print(c.firstweekday)



# Modules Names

# Purpose

# calendar
# used in case we are working with calendars

# random
# used for generating random numbers within certain defined limits

# enum
# used while working with enumeration class

# html
# for handling and manipulating code in HTML

# math
# for working with math functions such as sin, cos, etc.

# runpy
# runpy is an important module as it locates and runs python modules without importing them first

