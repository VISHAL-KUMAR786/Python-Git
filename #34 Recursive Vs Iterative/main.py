# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
print("Enter a number ")
k = int(input())
def fact_iteratice(n):
    p = 1
    for i in range(1,n+1):
        p = p * i
    else:
        return p
print(fact_iteratice(k))

def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    else :
        return fact_recursive(n-1) * n
print(fact_recursive(k))

# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 * factorial_recursive(1)
# 5 * 4 * 3 * 2 * 1 = 120

def fib(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fib(n-1) + fib(n-2)


for i in range(0,k+1):
    print(fib(i))