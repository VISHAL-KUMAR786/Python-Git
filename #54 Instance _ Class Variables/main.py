class  Employee :
    leaves = 8 
    pass

e1 = Employee()
e2 = Employee()

e1.name = "vishal"
e1.age = 45
e1.role = "gamer"

e2.name = "vishal"
e2.age = 45
e2.role = "gamer"

print(Employee.leaves)
print(Employee.__dict__)
Employee.leaves = 9
print(Employee.__dict__)

e1.leaves = 10
print(Employee.leaves)