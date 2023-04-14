'''
filter the list as how many of them are odd and even

if we wanna to change the value of the list item which are even multi 2


  chunck  -->       filter     -->       map       -->       reduce
(raw data)  (only refined data)  (operation on data) (one value out of data)


reduce take two values at a time

# filter
# def isEven(n):
#     return n%2 == 0

# map
# def update(n):
#     return ((n*10)-3)

# reduce
# def addAll(a,b):
#     return a+b

'''
from functools import reduce

l1 = [int(x) for x in input().split(" ")]

evens = list(filter(lambda n : n%2 == 0,l1))

double = list(map(lambda n : ((n*10)-3),evens))

sums = reduce(lambda a,b : a+b,double)

print(evens)
print(double)
print(sums)