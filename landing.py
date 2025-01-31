from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import subprocess
import webbrowser

def run_code1():
    subprocess.call(["python", r"C:\Users\impan\PycharmProjects\nbaproject\scoresfromapi\scores.py"])

def run_code2():
    subprocess.call(["python", r"C:\Users\impan\PycharmProjects\nbaproject\scoresfromdb\getscorefromdb.py"])

def run_code3():
    subprocess.call(["python", r"C:\Users\impan\PycharmProjects\nbaproject\soccer\football.py"])

def run_code4():
    subprocess.call(["python", r"C:\Users\impan\PycharmProjects\nbaproject\ipl\iplfromdb.py"])

def run_code5():
    subprocess.call(["python", r"C:\Users\impan\PycharmProjects\nbaproject\donotuse\players1.py"])

def run_code7():
    subprocess.call(["python", r"C:\Users\impan\PycharmProjects\nbaproject\Football\Football.py"])

def run_code8():
    subprocess.call(["python", r"C:\Users\impan\PycharmProjects\nbaproject\ipl\IPL.py"])

def run_code6():
    webbrowser.open('http://127.0.0.1:5000')

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

button1 = QPushButton('NBA Score retrieval from API')
button1.clicked.connect(run_code1)
layout.addWidget(button1)

button2 = QPushButton('NBA Score retrieval from DB')
button2.clicked.connect(run_code2)
layout.addWidget(button2)

button3 = QPushButton('Football Score retrieval from API')
button3.clicked.connect(run_code3)
layout.addWidget(button3)

button5 = QPushButton('Football Score retrieval from API2')
button5.clicked.connect(run_code7)
layout.addWidget(button5)

button4 = QPushButton('IPL Score retrieval from DB')
button4.clicked.connect(run_code4)
layout.addWidget(button4)

button6 = QPushButton('IPL Score retrieval from API')
button6.clicked.connect(run_code8)
layout.addWidget(button6)

# button5 = QPushButton('Start Flask server for NBA players data retrieval')
# button5.clicked.connect(run_code5)
# layout.addWidget(button5)

# button6 = QPushButton('web browser example')
# button6.clicked.connect(run_code6)
# layout.addWidget(button6)

window.setLayout(layout)
window.show()

app.exec_()