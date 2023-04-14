'''
find the next palindrome of a given number by user
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
        n = int(input("Enter the test case : "))

        for i in range(n):

            x = int(input("Enter a number : "))

            while True :
                if str(x) == str(x)[::-1]:
                    print(f"Next Palindrome is {x}")
                    break
                else:
                    x+=1

    except ValueError as e :
        print(e)

    except Exception as e:
        print(e)

    else:
        # print("When there is no exception then it will run")
        pass

    finally:
        print("Program ended sucessfully 😍🥰")
        # print("It will run in all condition")
        pass 