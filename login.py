from book import inputBook,showAllBook,showBook, updateBook,delete_book
import os 
from db import con
import maskpass

cur = con.cursor()

clear = ('cls' if os.name=='nt' else 'clear')
 
def login():
    print("*** login to your dasboard ***")
    username = input("Enter your username: ")
    password =maskpass.askpass(prompt="Enter your Password: ", mask="*")
    cur.execute("select * from users where user_name = %s and password = %s",(username,password))
    if cur.fetchone() != None:
        os.system(clear)
        home()
    else:
        while cur.fetchone() == None:
            os.system(clear)
            print("Incorrect username or password\nTry again\n")
            login()
            if cur.fetchone() != None:
                os.system(clear)
                home()


def home():
    user = input("Select your option:\n1.To add a new book\n2.To read all books\n3.To show a book\n4.To update book\n5.Delete book\n0.Exit\n")
    if int(user) == 1:
        inputBook()
        os.system(clear)
        home()

    elif int(user) == 2:
        showAllBook()
        num = input("\nTo Back to the menu click 0: ")
        if int(num) == 0:
            os.system(clear)
            home()
        while not int(num) == 0:
            os.system(clear)
            print("Invalid number")
            num = input("\nTo Back to the menu click 0: ")
            if int(num) == 0:
                os.system(clear)
                home()

    elif int(user) == 3:
        os.system(clear)
        showBook()
        num = input("\nTo Back to the menu click 0: ")
        if int(num) == 0:
            os.system(clear)
            home()
        while not int(num) == 0:
            os.system(clear)
            print("Invalid number")
            num = input("\nTo Back to the menu click 0: ")
            if int(num) == 0:
                os.system(clear)
                home()
    elif int(user) == 4:
        os.system(clear)
        updateBook()
        num = input("\nTo Back to the menu click 0: ")
        if int(num) == 0:
            os.system(clear)
            home()
        while not int(num) == 0:
            os.system(clear)
            print("Invalid number")
            num = input("\nTo Back to the menu click 0: ")
            if int(num) == 0:
                os.system(clear)
                home()
    elif int(user) == 5:
        os.system(clear)
        delete_book()
        num = input("\nTo Back to the menu click 0: ")
        if int(num) == 0:
            os.system(clear)
            home()
        while not int(num) == 0:
            os.system(clear)
            print("Invalid number")
            num = input("\nTo Back to the menu click 0: ")
            if int(num) == 0:
                os.system(clear)
                home()
    elif int(user) == 0:
        os.system(clear)
        login()
    con.close()
login()
