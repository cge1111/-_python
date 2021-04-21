# 윈도우 크기 조절

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()  
        self.setGeometry(100, 200, 300, 400)      # 윈도우 타이틀바 변경
        self.setWindowTitle("PyQt")               # 윈도우 타이틀바의 텍스트
        self.setWindowIcon(QIcon("bitcoin.png"))  # 아이콘 파일
        
        btn = QPushButton("버튼1", self)          # 버튼 추가하기    
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked)     # 버튼에 클릭 이벤트 추가

    def btn_clicked(self):                        # 버튼에 클릭 이벤트 추가
        print("버튼 클릭")

app = QApplication(sys.argv)  
window = MyWindow()
window.show()
app.exec_()