# worker.py
from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time
import json, os, serial
from json.decoder import JSONDecodeError

# Adafruit
from Adafruit_IO import *
aio = Client('SirAstolf','aio_SFgP65PgaZ2bTOcuKQt60KO9t42o')

class Worker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(float,float,float,float)

    @pyqtSlot()
    def procCounter(self): # A slot takes no params
        while True:
            try:
                arduino_port = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
                time.sleep(1)
                if arduino_port.isOpen():
                    while arduino_port.inWaiting() == 0: pass
                    if arduino_port.inWaiting() > 0:
                        write_json = open('data.json', 'w')
                        for i in range(7):
                            line = arduino_port.readline().rstrip().decode('utf-8')
                            write_json.write(line)
                            print("wrote" + line.strip())
                            # time.sleep(0.1)
                        write_json.close()

                        # READ JSON
                        filesize = os.path.getsize('data.json')

                        if filesize == 0:

                            # self.intReady.emit(1.0, 1.0, 1.0, 1.0)
                            print("Empty file")

                        else:
                            with open("data.json") as data_json:
                                obj_json = json.load(data_json)
                                data_json.close()

                            h_rate = obj_json["Heart Rate"]
                            oxigen = obj_json["SPO2"]
                            temperature = obj_json["Temperature"]
                            resp_rate = obj_json["Resp Rate"]

                            self.intReady.emit(temperature, oxigen, h_rate, resp_rate)
                            time.sleep(1)
                            #aio.send("healthypi.heartrate", str(h_rate))
                            #aio.send("healthypi.spo2", str(oxigen))
                            #aio.send("healthypi.temperature", str(temperature))
                            #aio.send("healthypi.respiration", str(resp_rate))
                            #time.sleep(1)

                        self.finished.emit()
                else:
                    print("not found")

            except  serial.SerialException as e:
                print(e)

            except KeyboardInterrupt as e:
                print(e)










