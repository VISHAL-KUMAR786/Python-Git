# 1 

# num = 1
# def num1():
#     k = 5 #local
#     print(num+1,k)
# num1()

# 2

# l = 50
# print(l)
# def function1():
#     global l
#     l = 5
#     print(l+5)
# function1()
# print(l)

# 3

# global mean it will check from the outer most
x = 80
print("line no 1 " ,x)
def vishal():
    x = 20
    print("line no 2 " ,x)
    def vivek():
        global x 
        x = 5
        print("line no 3 " ,x)
    vivek()
    print("line no 4 " ,x)
vishal()
print("line no 6 " ,x)


# y = 10 
# def k():
#     globals()["y"]=15
#     print(y)
# k()