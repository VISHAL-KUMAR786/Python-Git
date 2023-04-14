l1 = ["vishal","vivek","vijay","beena"]

a = " & ".join(l1)
print(a)

a = " - ".join(l1)
print(a)

sep = ', '
a = sep.join(l1)
print(a)

l1 = ["vishal",45,"vivek",45,"vijay",45,"beena"]
# a = sep.join(l1) Error
print(a)

# a = ", ".join(l1) Error Note: If the iterable contains any non-string values, join() will raise a TypeError exception.
# print(a)