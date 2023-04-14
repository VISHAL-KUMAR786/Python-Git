'''
take number of friends as input
make a list of friend name
shuffle the surNames of the name so that it would be funny moment
'''

# practice problem

import random

numberOfFriends = int(input("Enter the number of friends : "))
print(f"Enter the number of your {numberOfFriends} friends")
friendsName = []

for i in range(0,numberOfFriends):
    friendsName.append(input())

FLName = []
for i in friendsName:
    k = i.strip().split(" ")
    FLName.append(k)

l1 = []
l2 = []
for item in FLName:
    l1.append(item[0])
    l2.append(item[1])

random.shuffle(l2)
finalList = zip(l1,l2)

print("After Shuffling SurName of our Friends")
for item in finalList:
    print(f"{item[0]} {item[1]}")

# only name with two surnames are allowed 