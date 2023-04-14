class employee:
    leaves = 9
    def __init__(self,name,age,role) -> None:
        self.name= name
        self.age = age
        self.role = role
    
    def printi(self):
        return f"my name is {self.name}. Age is {self.age},role is {self.role}"
    pass


e1 = employee("vishal",45,"Play Boy")

print(e1.name)
print(e1.printi())