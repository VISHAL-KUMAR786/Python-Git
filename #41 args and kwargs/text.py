def my(l):
    print(l)
    for i in l:
        print(i)
my([1,2,3])

def my1(*l):
    print(l)
    for i in l:
        print(i)
my1(*[1,2,3])