class Libaray:
    '''
    This is my libaray management system 
    with all the joy and happiness
    '''
    def __init__(self,list,name) -> None:
        import datetime
        self.bookList = list 
        self.name = name 
        self.lendDict = {}

        with open(f'C:\\Users\\User\\Desktop\\Django udemy\\python basic\\CWH python\\#101 Libaray management sys\\{self.name}-bookList.txt','w') as f :
            for book in list :
                f.write(f"{book} has been added at time {datetime.time()}" + '\n')

    def displayBook(self):
        print(f"{self.name} Libaray have the following books 🥰")
        with open(f'C:\\Users\\User\\Desktop\\Django udemy\\python basic\\CWH python\\#101 Libaray management sys\\{self.name}-bookList.txt','r') as f :
            print(f.read())

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            self.bookList.remove(book)
            print("Database has been updates . you can take the book now")
        else:
            print(f"This book is lended to user . Whose name is {self.lendDict[book]}")

    def addBook(self,book):
        self.bookList.append(book)
        print("Book have Been Added Successfully 😍")

    def returnBook(self,book):
        if book in self.lendDict:
            del self.lendDict[book]
            self.bookList.append(book)
        else:
            print(f"This {book} is not in you dict of lendBook 😭")

if __name__ == '__main__':

    Name = input("Enter your Libaray Name : ")
    print("Enter the list of book that you want to add in libaray")
    print('''⚠️ Enter the book name which are seprated by " " Key ⚠️''')
    l = [ x for x in input().split('"')]
    l1= [item for item in l if len(item)!= 0]

    Libaray1 = Libaray(l1,Name)

    while(True):
        print(f"🙏 Welcome to {Libaray1.name} Libaray 🙏")
        print("🔥 Enter you choice 🔥")
        print("1. Display All the Book")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        
        try:
            user_choice = int(input())
            if user_choice not in ['1','2','3','4']:
                print("🥺 Please Enter valid option")
                continue
            else:
                user_choice = int(user_choice)


            if user_choice == 1:
                Libaray1.displayBook()

            elif user_choice == 2:
                user = input("Enter the user name : ")
                book = input("Enter the book name : ")
                Libaray1.lendBook(user,book)
            
            elif user_choice == 3:
                book = input("Enter the Book Name Which you want to add : ")
                Libaray1.addBook(book)
            
            elif user_choice == 4:
                book = input("Enter the book which you want to return : ")
                Libaray1.returnBook(book)

            else :
                print("Please Enter a valid input")

            user_choice2 = ''
            while( user_choice2.lower() != 'c' and user_choice2.lower() != 'q'):

                user_choice2 = input("Enter 'q' to Quit and 'c' to Continue : ")
                if user_choice2.lower() == 'q':
                    exit()
                if user_choice2.lower() == 'c':
                    continue
        except Exception as e:
            print(e)          



'''

work remaining 

    add more option like 
        change libaray name
        change book name
        chnage user name in lend book 
        and more .....
    
    add doc string to the function and class

    aad file management system

'''