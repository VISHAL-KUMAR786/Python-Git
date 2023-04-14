dict1= {"what is your name": "vishal kumar",
        "How old are you": "19yr",
        "What you dream":"To be a GREAT programmer"
        }

for x,y in dict1.items():
    print(x, y)


# list1 = [ ["vishal", 1], ["sishal", 2],
#           ["aishal", 6], ["dishal", 250]]
# dict1 = dict(list1)
#
# for item in dict1:
#     print(item)
# for item, lollypop in dict1.items():
#     print(item, "and lolly is ", lollypop)
items = [int, float, "ViSHAL", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)

