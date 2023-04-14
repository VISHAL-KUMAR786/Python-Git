"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -
it is mainly use in saving ram not loading all the code at once but when called then it will be provided

generator --> they generates the value of the fly
"""

def getNum(n):
    for i in range(n):
        yield i

n = 5
print(getNum(n))
lol = getNum(n)
print(lol.__next__())
print(lol.__next__())
print(lol.__next__())
print(lol.__next__())
print(lol.__next__())
# print(lol.__next__()) this time error

print("this is the secound ")
lol = getNum(5)
for i in lol:
    print(i)

# print("this is the third")
k = 465654654
# genq = iter(k) int is not iterable
# for i in genq:
#     print(i)

print("this is the third")
k = 'my name is khan'
for  i in iter(k):
    print(i,end="-")

print("\nthis is the fourth")
def fact1(n):
    if n < 0:
        yield 0
    elif n == 1 :
        yield 1
    else:
        multi = 1
        for i in range(1,n+1):
            multi *= i
        yield multi 
k = fact1(5)
print()
print(k.__next__())

print('this is the five')
# def gener(n):
#     for i in range(n):
#         yield i
gen1 = ( i for  i in range(5))
# print(gen1.__next__())
# print(gen1.__next__())
# print(gen1.__next__())
# print(gen1.__next__())
# print(gen1.__next__())
for i in gen1 :
    print(i)

# some more about dict 

d2 = {i for i in range(1,10001) if i%3==0}
print(d2)