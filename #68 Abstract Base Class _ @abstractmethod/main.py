# Abstract Base Class 
# it is the set of rule that are set by us so that any class that is inheriting abstract base class have to make those parameter (mendentory)


# from abc import ABCMeta , abstractmethod
from abc import abc , abstractmethod 

# class shape(metaclass= ABCMeta):
class shape(metaclass= abc):
    @abstractmethod
    def area(self):
        return 0

class square(shape):
    def __init__(self,len) -> None:
        self.len = len 
    def area(self):
        return self.len * self.len

class rectangle(shape):

    def __init__(self,len,bre):
        self.len = len 
        self.bre = bre 

    def area(self):
        return f"area is {self.len * self.bre}"
        
r1 = rectangle(3,4)
print(r1.area())
s1 = square(3)
print(s1.area())