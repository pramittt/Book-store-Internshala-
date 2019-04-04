from bookstore import *
import sqlite3
def book(nm):
    Book=sqlite3.connect('booklist.db')
    curbook=Book.cursor()
    sql="select * from book where Title='"+nm+"';"
    curbook.execute(sql)
    record=curbook.fetchone()
    return record[3]
def signals(self):
    self.btn1.clicked.connect(self.price)
    self.btn2.clicked.connect(self.total)

def price(self):
    nm=self.ed1.text()
    try:
        a=book(nm)
        self.ed2.setText(str(a))
    except:
        QtWidgets.QMessageBox.critical(MainWindow, 'Error','Invalid inputs',
        QtWidgets.QMessageBox.Ok)
def total(self):
    cpy=self.ed3.text()
    nm=self.ed1.text()
    try:
        cpy=int(cpy)
        a=book(nm)
        t=a*cpy
        self.ed4.setText(str(t))
    except:
        QtWidgets.QMessageBox.critical(MainWindow, 'Error','Invalid inputs',
        QtWidgets.QMessageBox.Ok)

Ui_MainWindow.signals=signals
Ui_MainWindow.price= price
Ui_MainWindow.total= total

if __name__== "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)

    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())
    
