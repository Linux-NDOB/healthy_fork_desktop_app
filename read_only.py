# Imports
from multiprocessing import Process
import sys, serial, time, json, math, worker
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import (
        QMainWindow, QApplication, QVBoxLayout, QHBoxLayout,
        QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
        QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QPushButton,
        QWidget)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import mysql.connector


# WINDOW APP
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        teal_darken_1 = QColor("#00897b");
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color), teal_darken_1)
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def onIntReady(self, temperature, oxigen, h_rate, resp_rate):
         # Imported from worker vars
        self.temperature_label1.setText("{}".format(temperature))
        self.oxigen.setText("{}".format(oxigen))
        self.h_rate.setText("{}".format(h_rate))
        self.resp_rate.setText("{}".format(resp_rate))

        self.atemp = temperature
        self.aox = oxigen
        self.ah_rate = h_rate
        self.a_rate = resp_rate


    # Window components
    def __init__(self):
        super(MainWindow, self).__init__()

        # 1 - create Worker and Thread inside the Form
        self.obj = worker.Worker()  # no parent!
        self.thread = QThread()  # no parent!

        # 2 - Connect Worker`s Signals to Form method slots to post data.
        self.obj.intReady.connect(self.onIntReady)

        # 3 - Move the Worker object to the Thread object
        self.obj.moveToThread(self.thread)

        # 4 - Connect Worker Signals to the Thread slots
        self.obj.finished.connect(self.thread.quit)

        # 5 - Connect Thread started signal to Worker operational slot method
        self.thread.started.connect(self.obj.procCounter)

        # * - Thread finished signal will close the app if you want!
        # self.thread.finished.connect(app.exit)

        # 6 - Start the thread
        self.thread.start()

        #read()
        self.setWindowTitle("Healthy Fork V.0")
        #self.setWindowIcon(QIcon(""))

        layout = QGridLayout()
        layout.setRowStretch(0,1)
        layout.setRowStretch(1,1)
        layout.setRowStretch(2,1)
        layout.setRowStretch(3, 1)

        # imported temp
        self.temperature_label1 = QLabel("0")
        self.temperature_label1.setStyleSheet("QLabel {background-color: #00b8d4 ; color : white}")
        layout.addWidget(self.temperature_label1, 2, 0)
        self.temperature_label1.setAlignment(Qt.AlignCenter)
        #self.setFont()

        #
        self.oxigen = QLabel("0")
        self.oxigen.setStyleSheet("QLabel {background-color: #00b8d4 ; color : white}")
        layout.addWidget(self.oxigen,2,1)
        self.oxigen.setAlignment(Qt.AlignCenter)

        #
        self.h_rate = QLabel("")
        self.h_rate.setStyleSheet("QLabel {background-color: #00b8d4 ; color : white}")
        layout.addWidget(self.h_rate, 2, 2)
        self.h_rate.setAlignment(Qt.AlignCenter)

        #
        self.resp_rate = QLabel("")
        self.resp_rate.setStyleSheet("QLabel {background-color: #00b8d4 ; color : white}")
        layout.addWidget(self.resp_rate, 2, 3)
        self.resp_rate.setAlignment(Qt.AlignCenter)

        # Title
        title = QLabel("HealthyPi 3 Fork",self)
        #title.setStyleSheet("font-size: 40")
        title.setAlignment(Qt.AlignCenter)
        title_font = title.font()
        title_font.setPointSize(25)
        title.setFont(title_font)
        title.setStyleSheet("QLabel {background-color: #004d40  ; color : white}")

        # Temp
        temperature = QLabel("Temperatura C°")
        temperature.setStyleSheet("QLabel {background-color: #00897b ; color : white}")
        temperature.setAlignment(Qt.AlignCenter)

        # SOP2
        oxigen = QLabel("SPO2")
        oxigen.setStyleSheet("QLabel {background-color: #00897b ; color : white}")
        oxigen.setAlignment(Qt.AlignCenter)

        # RRate
        resp_rate = QLabel("BPM")
        resp_rate.setStyleSheet("QLabel {background-color: #00897b ; color : white}")
        resp_rate.setAlignment(Qt.AlignCenter)

        # Hrate
        heart_rate = QLabel("Corazón BPM")
        heart_rate.setStyleSheet("QLabel {background-color: #00897b ; color : white}")
        heart_rate.setAlignment(Qt.AlignCenter)

        # Input cedula
        self.cedula = QLineEdit()
        self.cedula.setMaxLength(10)
        self.cedula.setPlaceholderText("INSERTE SU CEDULA")

        #Send Button
        button = QPushButton("Enviar datos")
        button.setCheckable(True)
        button.clicked.connect(self.send_data)

        #Result button
        self.a_enviar = QLabel()
        self.a_enviar.setStyleSheet("QLabel {background-color: #00897b ; color : white}")
        self.a_enviar.setAlignment(Qt.AlignCenter)

        # Adding Widgets
        layout.addWidget(title, 0,0, 1,0 )
        layout.addWidget(temperature, 1, 0)
        layout.addWidget(resp_rate, 1, 1)
        layout.addWidget(heart_rate, 1, 2)
        layout.addWidget(oxigen, 1, 3)
        layout.addWidget(button, 4, 1, 4, 2)
        layout.addWidget(self.cedula, 3, 1, 3, 2)
        layout.addWidget(self.a_enviar,9,1,9,2)

        # Footer
        footer = QLabel("HealthyPi 3 Fork ")
        footer.setStyleSheet("QLabel {background-color: #00897b ; color : white}")
        footer.setFont(title_font)
        footer.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer, 18,0,18,4)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setFixedWidth(720)
        self.setFixedHeight(480)

    def send_data(self):
        #ced = int(self.cedula.text())
        #self.atemp = temperature
        #self.aox = oxigen
        #self.ah_rate = h_rate
        #self.a_rate = resp_rate
        #1003066575
        #self.a_enviar.setText("Datos enviados a usuario: " + ced)

        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='healthy',
                                                 user='root',
                                                 password='kodokushi')

            mySql_insert_query = """INSERT INTO vital_signs ( patient_id, oxigen, heart_rate, temperature, resp_rate, weight, height, day_taken, year_taken, month_taken, hour_taken)
                                   VALUES 
                                   (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

            record = (1003066575, self.aox, self.ah_rate, self.atemp, self.a_rate, 100, 80, 12, 2022, 6, 11 )


            cursor = connection.cursor()
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Laptop table")
            cursor.close()

        except mysql.connector.Error as error:
            print("Failed to insert record into Laptop table {}".format(error))

        finally:
            if connection.is_connected():
                connection.close()
                print("MySQL connection is closed")

# Window process after arduino starts
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
