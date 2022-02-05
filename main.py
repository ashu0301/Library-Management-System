class Library:
    def __init__(self,books) -> None:
        self.books=books
    def displayAvailbleBooks(self):
        print("Available Books are: ")
        i=1
        for book in self.books:
            print(f"{i}.{book}")
            i +=1
    
    def borrowBook(self,BookName):
        if BookName in self.books:
            print(f"You have been issued {BookName}. Please keep it safe and Return it within 30 Days.")
            self.books.remove(BookName)
        else:
            print(f"{BookName} is not available right now or issued to someone. Please visit once the book is returned or available")

    def returnBook(self,BookName):
        self.books.append(BookName)
        print("Thanks for Returning/Donating the Book. We hope you Enjoyed it! ")

        

class Student:
    
    def requestBook(self):
        self.rektbook = input("Enter the name of the Book you want to be borrow: ")
        return self.rektbook

    def returnBook(self):
        self.retBook = input("Enter the Name of the Book you want to Return/Donate: ")
        return self.retBook



if __name__ == '__main__':
    GoyalLibrary=Library(["Python","C++","Java","DSA","SQL"])
    Student=Student()
    while(True):
        welcomeMessage='''\n----- Welocme To Central Library ----
        Select one option from below:
        1. Listing all the Books available in the Library
        2. Borrowing a Book from the Library
        3. To Return/Donate a to the Library
        4. To Exit from Central Library
        \n'''
        print(welcomeMessage)
        a=int(input(" Enter your Option here: "))
        if a==1:
            GoyalLibrary.displayAvailbleBooks()
        elif a==2:
            GoyalLibrary.borrowBook(Student.requestBook())
        elif a==3:
            GoyalLibrary.returnBook(Student.returnBook())
        elif a==4:
            print("Thank you for visiting Central Library.Hope to see you soon! ")
            exit()
        else:
            print("Invalid Choice! ")