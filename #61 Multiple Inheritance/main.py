# "In multiple inheritance, a class is derived from more than one class i.e. multiple base classes. The child class, in this case, has features of both the parent classes."

# Override means having two methods that have the same name
#  when the same method defined in the parent class is also defined in the child class, the process is known as Method overriding

# rules in orverride

# The name of the child method should be the same as parents.
# Inheritance should be there, and we need to derive a child class from a parent class
# Both of their parameters should be the same. 






# class Base1:
#     def first():
#         print("this is from first ")
# class Base2:
#     def secound():
#         print("this is from secound ")
#     def first():
#         print("this is from secound ")
# class child(Base1,Base2):
#     def third():
#         print("this is the child third")

# child.first() #in this first it will check base 1 for the function if it is not found then will check in other base 2 class
# child.secound()
# child.third()







class emp:
    leaves = 3
    def __init__(self,name,age,role) -> None:
        self.name = name 
        self.age = age
        self.role = role 
    def printi(self):
        print(f"My name is {self.name} , My age is {self.age} and my role is {self.role}")
    @classmethod
    def changeLeave(cls,leave):
        cls.leaves = leave
    @classmethod
    def classInit(cls,str):
        return cls(*str.split('-'))
    @staticmethod
    def empData(str):
        print(f"you data is {str}")

class player:
    holiday = 9 
    def __init__(self,name,game) -> None:
        self.name = name 
        self.game = game 
    def printPlayer(self):
        print(f"my name is {self.name} and i play {self.game}")


class coolPro(emp,player):
    def __init__(self, name, age, role, game , lang) -> None:
        self.lang = lang
        # this is the substitude of it
        # emp.__init__(self,name, age, role)
        # player.__init__(self,name,game)

        super().__init__(name,age,role)
        super(emp,self).__init__(name,game)
        
    def printLang(self):
        print(f"name -> {self.name} | age -> {self.age} | role -> {self.role} | lang -> {self.lang} | game -> {self.game}")


c1 = coolPro('vishal',12,'Bruh BOI','Thenga','hindi')

c1.printLang()




# it is single inheritance stack overflow example
# You could use super(ChildClass, self).__init__()

# class BaseClass(object):
#     def __init__(self, *args, **kwargs):
#         pass

# class ChildClass(BaseClass):
#     def __init__(self, *args, **kwargs):
#         super(ChildClass, self).__init__(*args, **kwargs)




# Calling parent class __init__ with multiple inheritance, what's the right way?
# class A(object):
#     def __init__(self):
#         print("Entering A")
#         super(A, self).__init__()
#         print("Leaving A")

# class B(object):
#     def __init__(self):
#         print("Entering B")
#         super(B, self).__init__()
#         print("Leaving B")

# class C(A, B):
#     def __init__(self):
#         print("Entering C")
#         A.__init__(self)
#         B.__init__(self)
#         print("Leaving C")
# Then I get:

# Entering C
# Entering A
# Entering B
# Leaving B
# Leaving A
# Entering B
# Leaving B
# Leaving C
# Note that B's init gets called twice. If I do:

# class A(object):
#     def __init__(self):
#         print("Entering A")
#         print("Leaving A")

# class B(object):
#     def __init__(self):
#         print("Entering B")
#         super(B, self).__init__()
#         print("Leaving B")

# class C(A, B):
#     def __init__(self):
#         print("Entering C")
#         super(C, self).__init__()
#         print("Leaving C")
# Then I get:

# Entering C
# Entering A
# Leaving A
# Leaving C