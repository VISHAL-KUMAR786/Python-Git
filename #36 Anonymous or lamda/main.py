def sum1(x,y):
    return x+y

sum2 = lambda x,y : x+y
sum3 = lambda x,y,z : x+y+z

print(sum1(5,3))
print(sum2(5,3))
print(sum3(5,3,2))

a =[[1, 14], [5, 6], [8,23],[11,1]]

a.sort(key=lambda x:x[1])
print(a)
a.sort(key=lambda x:x[1],reverse=True)
print(a)

# theory 
# we use is because 
#  reduce(), filter(), and map(). 

# Significant Differences Between Lambda Expressions And Simple Functions.
# Can be passed immediately with or without variables.
# They are inline functions.
# Automatic return of results.
# There is neither a document string nor a name.

# list.sort(key=myFunc ,reverse=True|False)
# Sort() does not return any value, but it changes from the original list.