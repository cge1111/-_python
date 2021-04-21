# 나만의 윈도우 클래스 정의하기
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()   # 'self.부모클래스_메서드()' 


app = QApplication(sys.argv)  
window = MyWindow()
window.show()
app.exec_()
