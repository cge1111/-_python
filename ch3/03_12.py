#  오픈 API  : 인터넷 주소 끌어올 때

import sys
from PyQt5.QtWidgets import *
 
app = QApplication(sys.argv)      # QApplication 객체 생성
label = QLabel("Hello")
label.show()
app.exec_()                       # 이벤트 루프 생성
