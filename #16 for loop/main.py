dict1= {"Best Python Course": "CodeWithHarry",
        "Best C Languge Course": "CodeWithHarry",
        "Harry Sir":"Tom Cruise Of Programming"
        }

# for x ,y in dict1.items():
#     print(x,y)

list1 = [ ["Harry", 1], ["Larry", 2],
          ["Carry", 6], ["Marie", 250]]

dict2 = dict(list1)

# for x ,y in dict2.items():
#     print(x,y)

# for key in dict2:
#     print(key)

items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for _ in items:
    if str(_).isnumeric() and _ >= 6:
        print(_)