import sys # 코빗 시세조회
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pykorbit

form_class = uic.loadUiType("mycobit.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)


    def inquiry(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit_1.setText(str(price)) 

        price2 = pykorbit.get_current_price("ETH")
        self.lineEdit_2.setText(str(price2)) 


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
