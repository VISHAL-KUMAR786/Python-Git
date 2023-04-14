class employee:
    leave = 9
    
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def printi(self):
        print(f"My name is {self.name} and my age is {self.age}")

    @classmethod
    
    def change_leave(cls,leaves):
        print("This is the name of class -->",cls.__name__)
        cls.leave = leaves 
    pass

e1 = employee("vishal",45)
e1.printi()

e1.change_leave(47)
print(employee.__dict__)