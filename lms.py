import mysql.connector as connector

class Library:
    def __init__(self):
        self.con= connector.connect(host='localhost', port='3306', user='root', password='22061999', database='library')
        query='create table if not exists libra (bookId int primary key, bookName varchar (100))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Library Created")

    #display Books 
    def display_books(self):
        query="select * from libra"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("BookId: ", row[0])
            print("Book Name: ", row[1])
            print()
            print()


    #Borrow Book
    def borrow_book(self, bookId):
        query="delete from libra where bookId= {}".format(bookId)
        # print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Borrowed!")
        
    #Return Book
    def return_Book(self, bookId, bookName):
        query="insert into libra(bookId, bookName) values({}, '{}')".format(bookId, bookName)
        # print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Book saved to Database")