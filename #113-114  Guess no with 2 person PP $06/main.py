'''
generate a random no between a range which is set by user
handle the data for two player
which player have the most point print its name
'''
# practice problem
class err(ValueError):
    '''
        this is simple a doc string of the class , which is inhertied from value error
    '''
    # creting a constructor
    def __init__(self,msg) -> None:
        self.msg = msg

if __name__ == '__main__':
    try:
        # importing random module
        import random

        # input a,b from the user
        a = int(input("Enter value of a : "))
        b = int(input("Enter value of b : "))

        name1 = input("Enter Name of first player : ")
        name2 = input("Enter Name of Secound player : ")
        # generating a random number between a,b using random module
        no = random.randint(a,b)

        # intialize score of the both person
        person1,person2 = [] ,[]

        # there are two player so looping twice , if there were more store it in list
        for i in range(2):

            # no of moves 
            chance = 0

            # making a infinite loop
            while True:

                # input from the user as a guess number
                my = int(input("Enter Your Guess Number : "))

                # making if-else condition
                if no == my :
                    chance+=1
                    print("You Are Chicken Dinner 🎉🎊")
                    break
                elif no > my :
                    print("Guess Large Number 😍🥰")
                    chance+=1
                    continue
                elif no < my :
                    print("Guess Small Number 😍🥰")
                    chance+=1
                    continue
            # printing the number of moves require to win   
            print(f"You Win Game in {chance} Moves")

            # making if-else condition
            if i == 0:
                person1.append(chance)
                person1.append(name1)
            else:
                person2.append(chance)
                person2.append(name1)
            # creating a blank screen effect
            print("\n\n\n\n\n\n\n\n")

        # making if-else condition
        if person1[0] == person2[0] :
            print(f"Both Have Equal Moves {chance}.")
            print("-------x----- DRAW -----x-------")
        elif person1[0] < person2[0]:
            print("-------x----- PLAYER1 WIN -----x-------")
            print(f"{person1[1]} win by {person2[0] - person1[0]} moves")
        elif person2[0] > person1[0]:
            print("-------x----- PLAYER2 WIN -----x-------")
            print(f"{person2[1]} win by {person1[0] - person2[0]} moves")

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

'''
    to do 
        making the loop code in a function 
        create small function to deal with
'''