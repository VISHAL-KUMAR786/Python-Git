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
        l1 = str.split('-')
        print(l1)
        return cls(l1[0],l1[1],l1[2]) 
        # emp('vishal',12,'boii') this is working as cls(l1[0],l1[1],l1[2])
        # return cls(*str.split('-'))


e1 = emp('vishal',12,'boii')
# e2.classInit('12-1-43') wrong 
e2 = emp.classInit('123-12-1')
print(e2.name,e2.age,e2.role)