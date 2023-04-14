# Methods starting with a double underscore ( __ ) and ending with a double underscore ( __ ) represent dunder methods.


# Difference between __str__ and __repr__ functions

# difference in them is the way of writing them
#  __str__ method is mainly written for the end-user, while __repr__ is written for a developer
# priority of __str__ is greater than __repr__
# If the implementation of __str__ is missing, then __repr__ function is used as a fallback. If the implementation of __repr__ is missing, then there will be no fallback.
# If __repr__ function is returning the object's String representation, we can skip the implementation of __str__ function. 

class emp:
    leaves = 3

    def __init__(self,name,age,salary) -> None:
        self.name = name 
        self.age = age
        self.salary = salary 

    def printi(self):
        print(f"My name is {self.name} , My age is {self.age} and my role is {self.salary}")

    def __add__(self,other) -> int:
        return self.salary + other.salary

    def __truediv__(self, other) -> float :
        return self.salary / other.salary

    def __repr__(self) -> str:
        return f"Employee('{self.name}',{self.age},{self.salary})"
    
    def __str__(self) -> str:
        return f"Name is {self.name} , age is {self.age} and salary is {self.salary}"

    def __pow__(self, other):
        return self.salary ** other.salary

    def __lt__(self, other):
        return self.salary > other.salary

    def __neg__(self):
        return -(self.salary)

    def __iadd__(self, other):
        self.salary += other.salary
        return emp(self.name,self.age,self.salary)
    pass 

e1 = emp('vishal',12,120)
e2 = emp('vivek',12,111)

print(e1 + e2, e1 / e2, str(e1), repr(e2),sep="\n")
print(e1 ** e2)
print(e1 > e2)
print(-e1)
e1 += e2
print(e1)


# Operator	Magic Method
# +	__add__(self, other)
# –	__sub__(self, other)
# *	__mul__(self, other)
# /	__truediv__(self, other)
# //	__floordiv__(self, other)
# %	__mod__(self, other)
# **	__pow__(self, other)
# >>	__rshift__(self, other)
# <<	__lshift__(self, other)
# &	__and__(self, other)
# |	__or__(self, other)
# ^	__xor__(self, other)

# Comparison Operators :
# Operator	Magic Method
# <	__lt__(self, other)
# >	__gt__(self, other)
# <=	__le__(self, other)
# >=	__ge__(self, other)
# ==	__eq__(self, other)
# !=	__ne__(self, other)

# Assignment Operators :
# Operator	Magic Method
# -=	__isub__(self, other)
# +=	__iadd__(self, other)
# *=	__imul__(self, other)
# /=	__idiv__(self, other)
# //=	__ifloordiv__(self, other)
# %=	__imod__(self, other)
# **=	__ipow__(self, other)
# >>=	__irshift__(self, other)
# <<=	__ilshift__(self, other)
# &=	__iand__(self, other)
# |=	__ior__(self, other)
# ^=	__ixor__(self, other)

# Unary Operators :
# Operator	Magic Method
# –	__neg__(self)
# +	__pos__(self)
# ~	__invert__(self)