'''
==   -      value equality          -      Two objects have the same value
is   -      reference equality      -       Two references refer to the same object

c = [1, 2, 3, 4] and d = [1, 2, 3, 4]

This creates a list object and stores a reference to it in c; then, it creates a second list object and stores a reference to it in d.

‘c == d’ is still true. However, 'c is d' is now false. This is because both c and d refer to different objects.
'''

a = 5 
b = a 
print(a is b)
print(a == b)


a =[6, 4 , "34"]
b = a 