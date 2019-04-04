import sqlite3
def bookstore(value):
    cost=value
    Book=sqlite3.connect('booklist.db')
    curbook=Book.cursor()
    nm=input("Enter name:")
    sql="select * from book where Title='"+nm+"';"
    curbook.execute(sql)
    record=curbook.fetchone()
    if record==None:
        print ("No such book found\nTry again")
        ask=input("Add more books? Y/N ")
        if ask=="Y":
            return bookstore(cost)
        if ask=="N":
            print ("Total cost is ",cost)
    else:
        print (record)
        cpy=int(input("No. of Copies:"))
        a=record[3]
        cost=cost+cpy*a
        ask=input("Add more books? Y/N ")
        if ask=="Y":
            return bookstore(cost)
        if ask=="N":
            print ("Total cost is ",cost)
value=0
bookstore(value)
    


