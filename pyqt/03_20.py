import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyupbit

form_class = uic.loadUiType("mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.inquiry)


    def inquiry(self):
        price = pyupbit.get_current_price("KRW-BTC")
        self.lineEdit.setText(str(price)) 

        price2 = pyupbit.get_current_price("KRW-ETH")
        self.lineEdit_2.setText(str(price2)) 

        price3 = pyupbit.get_current_price("KRW-XRP")
        self.lineEdit_3.setText(str(price3)) 

        price4 = pyupbit.get_current_price("KRW-DOGE")
        self.lineEdit_4.setText(str(price4)) 

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
