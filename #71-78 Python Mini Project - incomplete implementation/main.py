class libaray:
    lend_book = {}

    def __init__(self,book_list,libaray_name) -> None:
        self.book = book_list
        libaray.libaray_name = libaray_name
        pass

    def display(self):
        for i in self.book:
            print(i)
        pass 

    def add(self,book_name):
        self.book.append(book_name)
        pass 

    def lendBook(self,requestedBook):
        if requestedBook in self.book:
            print("The book you requested has now been borrowed")
            self.book.remove(requestedBook)
            pass 
        else:
            print("Sorry the book you have requested is currently not in the library")
            pass 


class student:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow>>")
            self.book=input()
            libaray.lendBook(self,self.book)
            return self.book

      def returnBook(self):
            print("Enter the name of the book you'd like to return>>")
            self.book=input()
            return self.book


if __name__ == '__main__':
    library1 = libaray(["The Last Battle","The Screwtape letters","The Great Divorce"],'kattapaLibaray')
    rajesh = student()
    print(rajesh.requestBook())
