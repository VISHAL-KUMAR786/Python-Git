# comprehence are the one liner code 
# Sets - List - Dictionary - Generators


# for list 
l1 = []
for i in range(100):
    if i % 3 == 0:
        l1.append(i)
print('one',l1,len(l1))

l2 = [i for i in range(100) if i%3 == 0]
print('secound',l2,len(l2))


# for set 
s1 = {i for i in ["a", "a", "b", "c", "d", "d"]}
print(s1,len(s1))

# for dict 
d1 = { i:f"item{i}" for i in range(12)}
print(d1)

# reverse dict  
d2 = {Value : key for key,Value in d1.items()}
print(d2)

# gen


