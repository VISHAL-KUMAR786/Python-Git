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


e1 = emp('vishal',12,'boii')
e2 = emp.classInit('123-12-1')
emp.empData('my name is khan')