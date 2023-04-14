class hi:
    '''This is the doc string'''
    def __init__(self,age,name) -> None:
        self.name = name 
        self. age = age
    pass

print(hi.__doc__)

e1 = hi(45,'vishal')
e2 = hi(45,'vivek')

e1.subject = ["hindi","bindi"]
print(e1.__dict__)

e2.section = 'a1'
print(e2.__dict__)

print(e1,e2)