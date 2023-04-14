'''
take list as input form the user 
print the next palindrome of each element of list
'''
# practice problem
class err(ValueError):
    '''
        this is simple a doc string of the class , which is inhertied from value error
    '''
    # creting a constructor
    def __init__(self,msg) -> None:
        self.msg = msg

def pal(n):
    # creating a if-else condition to filter the value of n
    if n < 10:
        return n
    else:
        # making a infinite loop
        while True:
            # checking the condition of palandrome by string casting
            if str(n) == str(n)[::-1]:
                return n
            else:
                n+=1

if __name__ == '__main__':

    try:
        # taking list as a input from the user
        l1 = [int(x) for x in input('Enter Element of the list : ').split(' ')]

        # intializing a blank list
        l = []

        # taking a loop through each item of list
        for item in l1:
            l.append(pal(item))

        # print the list 
        print(l)

    # Checking if there is valueError 
    except ValueError as e :
        print(e)

    # Checking if there is any kind of exception to be dealed
    except Exception as e:
        print(e)

    # this will run when no exception was run
    else:
        pass

    # it will run in all condition
    finally:
        print("Program ended sucessfully 😍🥰")
        pass 