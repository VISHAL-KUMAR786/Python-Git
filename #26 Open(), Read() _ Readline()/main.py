# theory 
# open("filename" ,"mode")

f = open("#26 Open(), Read() _ Readline()\gvishal.txt","rt",encoding="utf8")

# print(f.read(2))

# f = open("#26 Open(), Read() & Readline()/vishal.txt","rt", errors='ignore')
# print(f.read())

# print(f.readline())
# print(f.readline())
# print(f.readline())

# for i in f:
#     print(i,end="")

f.seek(0)

print(f.readlines()) #it return list

f.close()

# extra by u format 
s = u'that\u2019s \U0001f63b'
print(s)
print(u'that\u2019s \U0001f63b')