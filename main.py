from lms import Library

def main():
    lb=Library()

    while(True):
        print('''=====Welcome to Central Library=====
        Please choose an option:
        1. List all the Books
        2. Request a Book to Borrow
        3. Return a Book
        4. Exit the Library
        ''')
        try:
            choice=int(input())
            if choice==1:
                # display books
                lb.display_books()
            
            elif choice==2:
                # borrow a book
                bid1= int(input("Enter the BookId of the Book you want to Borrow: "))
                lb.borrow_book(bid1)
               
            elif choice==3:
                # return a book
                bid2=int(input("Enter the BookId of the Book you want to Return: "))
                bname=input("Enter the Name of the Book you want to Return: ")
                lb.return_Book(bid2, bname)
                
            elif choice==4:
                break

            else:
                print("Invalid Choice, Try Again")

        except Exception as e:
            print(e)
            print("Invalid Details! Try Again!")

if __name__ == "__main__":
    main()