from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import subprocess
import webbrowser

def run_code1():
    subprocess.call(["python3", "/Users/mathewgeorge/isaiahnba/scoresfromapi/scores.py"])

def run_code2():
    subprocess.call(["python3", "/Users/mathewgeorge/isaiahnba/scoresfromdb/getscorefromdb.py"])

def run_code3():
    subprocess.call(["python3", "/Users/mathewgeorge/isaiahnba/soccer/football.py"])

def run_code4():
    subprocess.call(["python3", "/Users/mathewgeorge/isaiahnba/ipl/iplfromdb.py"])


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

button4 = QPushButton('IPL Score retrieval from DB')
button4.clicked.connect(run_code4)
layout.addWidget(button4)

window.setLayout(layout)
window.show()

app.exec_()