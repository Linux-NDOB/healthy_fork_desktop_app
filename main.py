# main.py
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout
import sys
import worker


class Form(QWidget):

    def __init__(self):
        super().__init__()


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

        # 7 - Start the form
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.label, 0, 0)

        self.move(300, 150)
        self.setWindowTitle('thread test')
        self.show()

    def onIntReady(self, i):
        self.label.setText("{}".format(i))
        print(i)

    app = QApplication(sys.argv)

    form = Form()

    sys.exit(app.exec_())
#app = QApplication(sys.argv)
#window = MainWindow()
#window.show()
#app.exec()


def read(self):
    while True:
        json_data = open('data.json').read()

        json_obj = json.loads(json_data)

        # Variables
        self.h_rate = json_obj["Heart Rate"]
        self.oxigen = json_obj["SPO2"]
        self.temperature = json_obj["Temperature"]
        self.resp_rate = json_obj["Resp Rate"]

    temp_label = QLabel("Any", self)
    temp_label.setText(str(self.temperature))
    layout.addWidget(temp_label, 2, 0)


# read(self)
read_json = Process(target=read(self))
read_json.start()

read_json.join()
# gui = Process(target= app.start())
# gui.start()