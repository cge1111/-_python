# 나만의 윈도우 클래스 정의하기
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(slef):
        super().__init__()


app = QApplication(sys.argv)  
window = MyWindow()
window.show()
app.exec_()
