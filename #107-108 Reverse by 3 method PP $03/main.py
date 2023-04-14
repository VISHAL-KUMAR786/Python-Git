'''
reverse a string using 3 method
    natural method 
    string tempring 
    using swap concept of c language
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
        l1 = [x for x in input("Enter a list (whose Element are seprated by space) : ").split(' ')]

        print("InBuilt Method for reverse the list")
        l2 = l1
        l2.reverse()
        print(l2)
        l2.reverse()

        print("[::-1] Method for reverse the list")
        print(l1[::-1])


        print("Reverse a list using swap concept")
        st = 0
        en = len(l1) - 1
        while st < en :
            l1[st] , l1[en] = l1[en] , l1[st] 
            st+=1
            en-=1    

        print(l1)
        l1.reverse()
        # another solution 
        # for i in range(len(l1)):
        #     l1[i], l1[len(l1)-i-1] = l1[len(l1)- i -1],l1[i]
        # print(l1)
        
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