# -*- coding: utf-8 -*-

# import json
import time

from PyQt5.QtWidgets import QMessageBox
# from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
#
# import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
from modbus_tk import modbus_rtu
import serial
from PyQt5 import QtCore

import app_logger
import db

logger = app_logger.get_logger(__name__)

class MyThread(QtCore.QThread):
    signal_data = QtCore.pyqtSignal(list)
    host: str
    port: int
    interval: int

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

        self.listok = [3137, 3139, 3141, 3143, 3145, 3154, 3156, 1280, 1282, 1283, 3161, 3162, 3163]

    def run(self):
        self.running = True
        # self.alarmoff = False
        host = self.host
        port = self.port
        interval = self.interval
        client = modbus_tcp.TcpMaster(host=host, port=port, timeout_in_sec=10)
        unit = 1
        while self.running:
            data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, False]
            data = {'3137': 0, '3139': 0, '3141': 0, '3143': 0, '3145': 0, '3154': 0, '3156': 0, '1280': 0, '1282': 0, '1283': 0, '3161': 0, '3162': 0, '3163': 0, 'err': False}
            for key in data:
                if key in ['err']:
                    continue

                if key in ['3161', '3162', '3163', 'err']:
                    try:
                        data[key] = client.execute(unit, cst.READ_HOLDING_REGISTERS, int(key), 1)[0]
                    except Exception as err:
                        self.running = False
                        logger.error("Ошибка чтения {err}".format(err=err))
                        data['err'] = True
                        break
                else:
                    try:
                        data[key] = client.execute(unit, cst.READ_HOLDING_REGISTERS, int(key), 1)[0] / 10
                    except Exception as err:
                        self.running = False
                        logger.error("Ошибка чтения {err}".format(err=err))
                        data["err"] = True
                        break

            self.signal_data.emit(list(data.values()))
            # Если ошибка не будем ждать
            if data['err']:
                return

            d = list(data.values())
            d.pop(13)
            # db.add_record_log(d)


            time.sleep(interval)
        client.close()

def blockunblock(host, port):
    unit = 1
    client = modbus_tcp.TcpMaster(host=host, port=int(port), timeout_in_sec=10)
    response = client.execute(unit, cst.WRITE_MULTIPLE_COILS, 1636, 1, [1])
    time.sleep(0.1)
    response = client.execute(unit, cst.WRITE_MULTIPLE_COILS, 1636, 1, [0])
    client.close()

def readcondition(host, port):
    unit = 1
    client = modbus_tcp.TcpMaster(host=host, port=int(port), timeout_in_sec=10)
    try:
        response = client.execute(unit, cst.READ_COILS, 1543, 1)[0]
    except Exception as err:
        client.close()
        return ['err', err]
    client.close()
    return ['good', response]