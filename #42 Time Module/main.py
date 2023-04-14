from threading import local
import time 

intial = time.time()

for i in range(45):
    print(i,end=" ")
print("for loop time",time.time()- intial)

intial2 = time.time()

n = 45
while n :
    print(n,end=" ")
    n -=1
print("wwhile loop time",time.time()- intial2)


print(time.time()) # return the tick tick
print(time.localtime(time.time())) # return time in form of tuple
print(time.asctime(time.localtime(time.time()))) # convert tupple into string
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
