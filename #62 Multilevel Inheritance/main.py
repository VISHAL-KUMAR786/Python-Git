#  Multiple inheritance VS. Multilevel inheritance

# Multiple inheritance
# Multiple Inheritance is where a class inherits from more than one base class.
# Sometimes, multiple Inheritance makes the system more complex, that’s why it is not widely used.
# Multiple Inheritance has two class levels; these are base class and derived class.

# Multilevel inheritance
# In multilevel inheritance, we inherit from a derived class, making that derived class a base class for a new class.
# Multilevel Inheritance is widely used. It is easier to handle code when using multilevel inheritance.
# Multilevel Inheritance has three class levels, which are base class, intermediate class, and derived class.




# class parent:
#     basketBall = 1
#     def base1(self):
#         print(f"my score in {self.basketBall}")
#     pass

# class child(parent):
#     cycling = 2
#     def base2(self):
#         print(f"my score in {self.basketBall} , {self.cycling}")
#     pass

# class grandson(child):
#     listingSong = 3
#     def base3(self):
#         print(f"my score in {self.basketBall} , {self.cycling} and {self.listingSong}")
#     pass

# k = grandson()
# k.base3()
# k.base2()
# k.base1()




class electronicDevice:
    def iselectronicDevice():
        print('The field of electronics is a branch of physics and electrical'\
            ' engineering that deals with the emission, behaviour and effects of electrons using electronic devices')
    pass

class pocketGadget(electronicDevice):
    def ispocketGadget():
        print('A Pocket PC (P/PC, PPC) is a class of personal digital assistant (PDA) that runs the Windows Mobile or Windows Embedded Compact operating system that has some of the abilities of modern desktop PCs. The name was introduced by Microsoft in 2000 as a rebranding of the Palm-size PC category.')
    pass

class phone(pocketGadget):
    def isphone():
        print('A mobile phone, cellular phone, cell phone, cellphone, handphone, hand phone or pocket phone sometimes shortened to simply mobile, cell, or just phone, is a portable telephone that can make and receive calls over a radio frequency link while the user is moving within a telephone service area')
    pass


phone.iselectronicDevice()
phone.ispocketGadget()
phone.isphone()