from db import con
import os
#cursor
cur = con.cursor()
clear = ('cls' if os.name=='nt' else 'clear')

def showAllBook():
    os.system(clear)
    #execute the query
    cur.execute("select * from book where removed= false")
    rows = cur.fetchall()
    for r in rows:
        print(f"no. book : {r[0]} \tname of book: {r[1]} \tname of author: {r[2]} \tprice: {r[3]}")

def inputBook():
    print("Add a Book\n")
    name_book = input("Enter the name of the book:\n")
    
    name_author = input("Enter the name of the author:\n")
    
    price = input("Enter the price:\n")
    
    cur.execute("insert into book (name_book,name_author,price) values (%s,%s,%s)",(name_book,name_author,price))
    con.commit()

def showBook():
    enter_name_book = str(input("enter the book name you want to find:\n"))
    cur.execute("select * from book where name_book = '"+enter_name_book+"'",(enter_name_book))
    rows = cur.fetchall()
    for r in rows:
        print(f"id : {r[0]} \t\nname of book: {r[1]} \t\nname of author: {r[2]} \t\nprice: {r[3]} JOD")

def updateBook():
    os.system(clear)
    print("**** To update book****\n")
    
    name_book = input("Enter the name of book you want to update: ")
    updated_name_book = input("Enter the updated book name: ")
    updated_name_author = input("Enter the updated author name: ")
    updated_price = input("Enter the updated price: ")
    cur.execute("update book set name_book = %s, name_author = %s, price = %s where name_book = %s",(updated_name_book,updated_name_author,updated_price,name_book))
    con.commit()
    print("The book has been updated...")
    

def delete_book():
    os.system(clear)
    print("**** to Delete Book ****\n")
    book_id = input("Enter the id of the book you want to delete: ")
    cur.execute("update book set removed = True where id = %s",(book_id))
    con.commit()
    print("The book has been deleted successfully!")
    

