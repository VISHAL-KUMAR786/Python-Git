'''
take number of apple as input 
take min value and max value 
tell them how many of them are the divisor of it
'''

# practice problem
class err(ValueError):
    '''
        this is simple a doc string of the class which is inhertied from value error
    '''
    def __init__(self,msg) -> None:
        self.msg = msg

if __name__ == '__main__':
    try:
        apple = int(input("Enter the number of apple do you have"))
        if apple < 0 or apple == 0:
            raise ValueError("Please enter a valid number")
        mn = int(input("Enter the minimum value"))
        mx = int(input("Enter the maximum value"))

        if mn > mx or mn == mx:
            raise ValueError("Please Enter a valid value of minimum & maximum value")

        for i in range(mn,mx+1):
            if apple%i == 0:
                print(f"{i} is a divisor of {apple}")
            else:
                print(f"{i} is not a divisor of {apple}")

    except ValueError as e :
        print(e)

    except Exception as e:
        print(e)

    else:
        # print("When there is no exception then it will run")
        pass

    finally:
        # print("It will run in all condition")
        pass 