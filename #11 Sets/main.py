'''
Restrictions:
Everything has a limit to its functionality, and there are some limitations on working with sets too.

Once a set is created, you can not change any of its items.  

Although you can add new items or remove previous but updating an already existing item is not possible.

There is no indexing in sets, so accessing an item in order or through a key is not possible, although we can ask the program if the specific keyword we are looking for is present in the set by using the “in” keyword or by looping through the set by using a for loop
'''
s = set()
# print(type(s))
# l = [1, 2, 3, 4]
# s_from_list = set(l)
# print(s_from_list)
# print(type(s_from_list))
s.add(1)
s.add(2)
s.remove(2)
s1 = {4, 6}
print(4 in s1)
print(s.isdisjoint(s1))

