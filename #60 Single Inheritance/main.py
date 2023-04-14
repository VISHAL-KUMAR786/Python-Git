# “Inheritance is the ability to define a new class(child class) that is a modified version of an existing class(parent class)”


# class parent:
#     def pop():
#         print("from parent")

# class child(parent):
#     def push():
#         print("from child")

# child.pop()
# child.push()


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

class pro(emp):
    holiday = 69
    def __init__(self, name, age, role,language) -> None:
        self.language = language
        super().__init__(name, age, role)

    def printi(self):
        print(f"my name is {self.name} , my age is {self.age} , my role is {self.role} and languages know to me is {self.language}")
        pass

e1 = emp('vishal',12,'boii')
e2 = emp.classInit('123-12-1')

p1 = pro('vishal',12 ,'boiii',['hindi','Bindi','c','css','html','py'])
p1.printi()
