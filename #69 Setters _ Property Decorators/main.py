# setters We can set new values for a newer object or update values for an older one.

#  @function_name.setter is a setter method with which we can set the value of the attribute

# Deleter is used to delete the values passed as a parameter before

# getters, setters, and deleters

class employee:
    def __init__(self,fname,lname) -> None:
        self.fname = fname 
        self.lname = lname 
        # self.email = f"{self.fname}{self.lname}@vishal.io"

    # def email(self):
    #     return f"{self.fname}{self.lname}@vishal.io"

    def fullName(self):
        print(f"Name is {self.fname} {self.lname}")

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@vishal.io"

    @email.setter
    def email(self,string):
        l1 = string.split('@')
        name = l1.split('.')
        self.fname = name[0]
        self.fname = name[1]

    @email.deleter
    def email(self):
        self.fname = None 
        self.lname = None 
e1 = employee('vishal','kumar')
# print(e1.email()) we use a property as a function
print(e1.email)
e1.fname = "vivek"
print(e1.email)