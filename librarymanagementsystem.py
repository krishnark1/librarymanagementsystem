class library:
    def __init__(self, listOfBooks, libraryName):
        self.userData = {}
        self.listOfBooks = listOfBooks
        self.libraryName = libraryName
        for books in self.listOfBooks:
            self.userData[books] = None
    #to display the library
    def displayBooks(self):
        for book in self.listOfBooks:
            print(book)
    #to withdraw book from library
    def withdrawBook(self, username, book):
        if book in self.listOfBooks:
            if self.userData[book] is None:
                self.userData[book] = username
                print("done")
            elif self.userData[book] == username:
                print("you already withdraw this book.")
            else:
                print(f"Book already withdraw by {self.userData[book]}.")
        else:
            print("invalid book name!!!")
    #to add new book to the library
    def addBook(self, nBook):
        self.listOfBooks.append(nBook)
        self.userData[nBook] = None
        print("done")
    #to return book to the library
    def returnBook(self, username, book):
        if book in self.listOfBooks:
            if self.userData[book] is not None:
                if self.userData[book] == username:
                    self.userData[book] = None
                    print("done")
                else:
                    print(f"this book is not belong to you\n this book is withdrawn by {self.userData[book]}")
            else:
                print("Sorry this book is not withdraw by anyone.")
        else:
            print("invalid book name!!!")
    #to delete the book inside the library
    def deleteBook(self, delBook):
        self.listOfBooks.remove(delBook)
        self.userData.pop(delBook)
        print("done")
    #to the details of library
    def showUser(self):
        for bk in self.userData:
            print(f'BookName:     {bk}\n UserName:    {self.userData[bk]}')
            print('-' * 80)
if __name__ == '__main__':
    bookList = ["2666", "Love Yourself", "Desert Solitaire", "Geek Love", "Avenger Tale", "Iron Man tale"]
    libNmae = input("enter your library name")
    key = int(input("enter your secret key for your library"))
    lib1 = library(bookList, libNmae)
    print("=" * 80)
    print(f"                    welcome to {lib1.libraryName}'s Library")
    print("=" * 80)
    loop = True
    while loop == True:
        print("\nTo display all books type 'l'")
        print("To withdraw any book type 'w'")
        print("To add any book type 'a'")
        print("To return any book type 'r'")
        print("To delete any book type 'del'")
        print("To check data in library type 'check'")
        print("To quit type 'q'")
        inp = input("Option: ")
        print("-" * 80)
        if inp == "l":
            lib1.displayBooks()
        elif inp == "w":
            nm1 = input("Enter your name: ")
            bk1 = input("Enter book name: ")
            lib1.withdrawBook(nm1, bk1)
        elif inp == "a":
            bk2 = input("Enter book name: ")
            lib1.addBook(bk2)

        elif inp == "r":
            nm2 = input("Enter your name: ")
            bk3 = input("Enter book name: ")
            lib1.returnBook(nm2, bk3)

        elif inp == "del":
            bk4 = input("Enter book name: ")
            ky = int(input("Enter secret key: "))
            if ky == key:
                lib1.deleteBook(bk4)
            else:
                print("You have no access to delete any book.")

        elif inp == 'q':
            print("Thanks for using.")
            break
        elif inp == 'check':
            lib1.showUser()
        else:
            print("Invalid Input!!!")
