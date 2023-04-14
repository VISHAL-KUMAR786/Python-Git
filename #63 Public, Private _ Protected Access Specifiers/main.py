class Boi:

    _leaves = 9
    __holidays = 10

    def __init__(self,name ,age, holiday) -> None:
        self._name = name 
        self._age = age 
        Boi.__holidays = 0 if (Boi.__holidays - holiday) < 0 else (Boi.__holidays - holiday)

    def __repr__(self) -> str:
        print(f"name is {self._name} , age is {self._age} and no of holidays remaining {Boi.__holidays}")

viky = Boi('vishal',12,5)
viky.__repr__()
print(viky._Boi__holidays)

# how to access private variable outside the class
#  name of the object . _ class name  __ variable name