class emp:
    '''this is the doc string of the class'''
    def __init__(self,name,age) -> None:
        self.name = name 
        self.age =age 

    def __repr__(self) -> str:
        return f"name is {self.name} and age is {self.age}"

    @property 
    def email(self):
        return f"{self.name}{self.age}@vishal.io"



class a(emp):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)




e1 = emp('vishal','kumar')
a1 = a('vivek','kumar')

print(type(e1)) #print the name of the class 

print(id(e1)) #print the id the class

print(dir(e1)) #all the method that are define in class
print(dir([1,3,4]))

print(hasattr(emp,'email'))

print(getattr(e1,'email')) # getattr(obj, key, def)
print(getattr(e1,'name','vivek')) # getattr(obj, key, def)

print(repr(e1))

print(vars(e1))

print(issubclass(a,emp)) #issubclass(object, classinfo)

print(isinstance(e1,emp))

print(emp.__doc__)

print(__name__)


def hi():
    return 'hello'

a = hi 
print(callable(a))
print(callable(e1))

print(help(e1))


# Types of introspects:-
# Some of the other common Introspects:

#  Functions    Working
# hasattr()     It checks if an object has an attribute.
# getattr()     It returns the contents of an attribute if there are some.
# repr()        It returns the string representation of an object
# vars()        It checks all the instance variables of an object
# issubclass()  This function checks that if a specific class is a derived class of another class.
# isinstance()  It checks if an object is an instance of a specific class. 
# __doc__       This attribute gives some documentation about an object 
# __name__      This attribute holds the name of the object
# callable()    This function checks if an object is a function
# help()        It checks what other functions do