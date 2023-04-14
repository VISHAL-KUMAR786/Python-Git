'''
make a faulty calculator 
    generate a random number in range of (1,10)
    use the random number generated as index 
    create a worng value at that index
you have to make a program of tell at what index it is telling wrong value

'''

# practice problem
import random

def multiplicationTable(number):
    wrong = random.randint(0,9)
    table = [i*number for i in range(1,11)]
    table[wrong] += random.randint(0,10)
    return table

def isCorrect(table,number):
    for i in range(1,11):
        if table[i-1] != i*number:
            return f"At index no {i-1} have the wrong value , correct value is {i*number}"

if __name__ == '__main__':
    number= int(input("Enter a number : "))
    myTable = multiplicationTable(number)
    print(myTable)
    print(isCorrect(myTable,number))
    



# def table(n):
#     l = []
#     for i in range(0,11):
#         if i == 3 :
#             l.append(105)
#         else :
#             l.append(i*n)
#     return l
# def checkTable(n,l1):
#     l = []
#     for i in range(0,11):
#         if int(l1[i]) == i *n:
#             pass 
#         else:
#             return f"At index {i} , It is wrong {n*i}"
#     return None

# tableof = int(input("Enter Number for which you want its table : "))
# print("Rohan Das function is Executed :",end=" ")
# rohanTable= table(tableof)
# print(rohanTable)
# print(checkTable(tableof,rohanTable))
