01: import multiprocessing as mp
02: import websockets
03: import asyncio 
04: import json
05: import sys
06: import datetime
07: from PyQt5.QtWidgets import *
08: from PyQt5.QtCore import *
09: 
10: 
11: async def bithumb_ws_client(q):
12:     uri = "wss://pubwss.bithumb.com/pub/ws"
13: 
14:     async with websockets.connect(uri, ping_interval=None) as websocket:
15:         subscribe_fmt = {
16:             "type":"ticker", 
17:             "symbols": ["BTC_KRW"], 
18:             "tickTypes": ["1H"]
19:         }
20:         subscribe_data = json.dumps(subscribe_fmt)
21:         await websocket.send(subscribe_data)
22: 
23:         while True:
24:             data = await websocket.recv()
25:             data = json.loads(data)
26:             q.put(data)
27: 
28: async def main(q):
29:     await bithumb_ws_client(q)
30: 
31: def producer(q):
32:     asyncio.run(main(q))
33: 
34: class Consumer(QThread):
35:     poped = pyqtSignal(dict)
36: 
37:     def __init__(self, q):
38:         super().__init__()
39:         self.q = q
40: 
41:     def run(self):
42:         while True:
43:             if not self.q.empty():
44:                 data = q.get()
45:                 self.poped.emit(data)
46: 
47: 
48: class MyWindow(QMainWindow):
49:     def __init__(self, q):
50:         super().__init__()
51:         self.setGeometry(200, 200, 400, 200)
52:         self.setWindowTitle("Bithumb Websocket with PyQt")
53: 
54:         # thread for data consumer
55:         self.consumer = Consumer(q)
56:         self.consumer.poped.connect(self.print_data)
57:         self.consumer.start()
58: 
59:         # widget
60:         self.label = QLabel("Bitcoin: ", self)
61:         self.label.move(10, 10)
62: 
63:         # QLineEdit 
64:         self.line_edit = QLineEdit(" ", self)
65:         self.line_edit.resize(150, 30)
66:         self.line_edit.move(100, 10)
67: 
68:     @pyqtSlot(dict)
69:     def print_data(self, data):
70:         content = data.get('content')
71:         if content is not None:
72:             current_price = int(content.get('closePrice'))
73:             self.line_edit.setText(format(current_price, ",d"))
74: 
75:         now = datetime.datetime.now()
76:         self.statusBar().showMessage(str(now))
77: 
78: 
79: if __name__ == "__main__":
80:     q = mp.Queue()
81:     p = mp.Process(name="Producer", target=producer, args=(q,), daemon=True)
82:     p.start()
83:     
84:     # Main process
85:     app = QApplication(sys.argv)
86:     mywindow = MyWindow(q)
87:     mywindow.show()
88:     app.exec_()
