'''
take age or birth year as an input from the user .
print after how many year it will we 100yr old.
    Some condition
        present age of that person is greather than longest span of human .You seem to be the oldest person alive  🎉
        You are not yet born 😭
Ask them at what particular year then want to know there age
'''

# practice problem
# 2022 *args: object
class err(ValueError):
    def __init__(self, msg) -> None:
        self.msg = msg
        # print(msg)
try : 
    x = int(input("Enter Your Age or Birth Year"))
    if x < 0 or x == 0:
        raise ValueError("Please Enter a valid age 😭")
    age , birth = 0, 0
    longestLife = 122 
    notYetBorn = 0

    if x < 200:
        age = x
    else:
        birth = x
    
    if age != 0 :
        if age < 0 or age == 0: 
            print("You are not yet born 😭")
        else:
            year = 2122 - age
            print(f"At this {year} you will be 100 year old. 😍")

            if age > longestLife :
                print("You seem to be the oldest person alive")

    else:
        if 1850 <= birth <= 2022: 
            birth = birth + 100
            print(f"At this {birth} you will be 100 year old. 😍")

            if age > longestLife :
                print("You seem to be the oldest person alive")
        else:    
            print("You are not yet born 😭")


    interestedYr = int(input("Enter the year you want to know you age"))

    if interestedYr < 0 or interestedYr == 0:
        raise ValueError("Please Enter a valid year 😭")
    else:
        if age != 0 :
            print(f"you will {age + interestedYr - 2022} year old at {interestedYr}")
        else:
            print(f"you will {interestedYr - birth} year old at {interestedYr}")

except ValueError as e :
    print(e)

except Exception as e:
    print(e)

else:
    # print('this is run when the except is not raise')
    pass 
    
finally:
    # print("closing all the resources")
    pass 