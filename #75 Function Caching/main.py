# from functools import lru_cache

# @lru_cache(maxsize=3)
# def myfun(n):
#     print("function has started")
#     import time
#     intialT = time.time()
#     time.sleep(n)
#     return f"function end {time.time() - intialT}"

# print(myfun(3))
# print("function implemented successfully")
# print(myfun(3))
# print(myfun(2))
# print(myfun(3))

from functools import lru_cache

x = int(input("Enter the maxsize of lru_cache"))
@lru_cache(maxsize=x)
def hi(n):
    print("started")
    import time 
    initalTime = time.time()
    time.sleep(n)
    return time.time() - initalTime 

print(hi(3))
print(hi(5))
print(hi(5))
print(hi(2))
print(hi(2))
print(hi(1))
print(hi(1))
print(hi(3))
print(hi(3))


