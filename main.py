# -*- coding: utf-8 -*-

import datetime
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QDialogButtonBox, QGridLayout
from PyQt5.QtGui import *
import pyqtgraph as pg
import sys
import wind
import win
import app_logger
import bible
import db

logger = app_logger.get_logger(__name__)
logger.info("Начало работы.")

app = QtWidgets.QApplication(sys.argv)
######### Стиль окна
app.setStyleSheet("Oxygen")
app.setStyle("Oxygen")

############ Инициализируем базы данных
db.init_db()

class AboutDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HELLO!")

        QBtn = QtWidgets.QDialogButtonBox.Ok \
               # | QtWidgets.QDialogButtonBox.Cancel

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel("""                            R@R studies prodaction.\
                     \nМонитор контроллера фирмы АльфаНорм вер.1.0.0""")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class setWin(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.main_ui = wind.Ui_Dialog()
        self.main_ui.setupUi(self)

        self.settings = QtCore.QSettings('R@RMonitor', 'setalarm')

        self.getset()
        self.main_ui.buttonok.clicked.connect(self.ok_clicked)
        self.main_ui.cancel.clicked.connect(self.cancel_clicked)

    def getset(self):
        if self.settings.contains("userangealarm"):
            self.main_ui.userangealarm.setChecked(True if self.settings.value('userangealarm') == 'true' else False)
        else:
            self.settings.setValue('userangealarm', False)

        if self.settings.contains("vmin"):
            self.main_ui.vmin.setText(self.settings.value('vmin'))
        else:
            self.settings.setValue('vmin', '0')
        if self.settings.contains("vmax"):
            self.main_ui.vmax.setText(self.settings.value('vmax'))
        else:
            self.settings.setValue('vmax', '0')

        if self.settings.contains("vmin1"):
            self.main_ui.vmin1.setText(self.settings.value('vmin1'))
        else:
            self.settings.setValue('vmin1', '0')
        if self.settings.contains("vmax1"):
            self.main_ui.vmax1.setText(self.settings.value('vmax1'))
        else:
            self.settings.setValue('vmax1', '0')

        if self.settings.contains("vmin2"):
            self.main_ui.vmin2.setText(self.settings.value('vmin2'))
        else:
            self.settings.setValue('vmin2', '0')
        if self.settings.contains("vmax2"):
            self.main_ui.vmax2.setText(self.settings.value('vmax2'))
        else:
            self.settings.setValue('vmax2', '0')

        if self.settings.contains("vmin3"):
            self.main_ui.vmin3.setText(self.settings.value('vmin3'))
        else:
            self.settings.setValue('vmin3', '0')
        if self.settings.contains("vmax3"):
            self.main_ui.vmax3.setText(self.settings.value('vmax3'))
        else:
            self.settings.setValue('vmax3', '0')

        if self.settings.contains("vmin4"):
            self.main_ui.vmin4.setText(self.settings.value('vmin4'))
        else:
            self.settings.setValue('vmin4', '0')
        if self.settings.contains("vmax4"):
            self.main_ui.vmax4.setText(self.settings.value('vmax4'))
        else:
            self.settings.setValue('vmax4', '0')

        if self.settings.contains("vmin5"):
            self.main_ui.vmin5.setText(self.settings.value('vmin5'))
        else:
            self.settings.setValue('vmin5', '0')
        if self.settings.contains("vmax5"):
            self.main_ui.vmax5.setText(self.settings.value('vmax5'))
        else:
            self.settings.setValue('vmax5', '0')

        if self.settings.contains("vmin6"):
            self.main_ui.vmin6.setText(self.settings.value('vmin6'))
        else:
            self.settings.setValue('vmin6', '0')
        if self.settings.contains("vmax6"):
            self.main_ui.vmax6.setText(self.settings.value('vmax6'))
        else:
            self.settings.setValue('vmax6', '0')

        if self.settings.contains("vmin7"):
            self.main_ui.vmin7.setText(self.settings.value('vmin7'))
        else:
            self.settings.setValue('vmin7', '0')
        if self.settings.contains("vmax7"):
            self.main_ui.vmax7.setText(self.settings.value('vmax7'))
        else:
            self.settings.setValue('vmax7', '0')

        if self.settings.contains("vmin8"):
            self.main_ui.vmin8.setText(self.settings.value('vmin8'))
        else:
            self.settings.setValue('vmin8', '0')
        if self.settings.contains("vmax8"):
            self.main_ui.vmax8.setText(self.settings.value('vmax8'))
        else:
            self.settings.setValue('vmax8', '0')

        if self.settings.contains("vmin9"):
            self.main_ui.vmin9.setText(self.settings.value('vmin9'))
        else:
            self.settings.setValue('vmin9', '0')
        if self.settings.contains("vmax9"):
            self.main_ui.vmax9.setText(self.settings.value('vmax9'))
        else:
            self.settings.setValue('vmax9', '0')

    def ok_clicked(self):
        self.settings.setValue('userangealarm', self.main_ui.userangealarm.isChecked())
        self.settings.setValue('vmin', self.main_ui.vmin.text().replace(',','.'))
        self.settings.setValue('vmax', self.main_ui.vmax.text().replace(',','.'))
        self.settings.setValue('vmin1', self.main_ui.vmin1.text().replace(',','.'))
        self.settings.setValue('vmax1', self.main_ui.vmax1.text().replace(',','.'))
        self.settings.setValue('vmin2', self.main_ui.vmin2.text().replace(',','.'))
        self.settings.setValue('vmax2', self.main_ui.vmax2.text().replace(',','.'))
        self.settings.setValue('vmin3', self.main_ui.vmin3.text().replace(',','.'))
        self.settings.setValue('vmax3', self.main_ui.vmax3.text().replace(',','.'))
        self.settings.setValue('vmin4', self.main_ui.vmin4.text().replace(',','.'))
        self.settings.setValue('vmax4', self.main_ui.vmax4.text().replace(',','.'))
        self.settings.setValue('vmin5', self.main_ui.vmin5.text().replace(',','.'))
        self.settings.setValue('vmax5', self.main_ui.vmax5.text().replace(',','.'))
        self.settings.setValue('vmin6', self.main_ui.vmin6.text().replace(',','.'))
        self.settings.setValue('vmax6', self.main_ui.vmax6.text().replace(',','.'))
        self.settings.setValue('vmin7', self.main_ui.vmin7.text().replace(',','.'))
        self.settings.setValue('vmax7', self.main_ui.vmax7.text().replace(',','.'))
        self.settings.setValue('vmin8', self.main_ui.vmin8.text().replace(',','.'))
        self.settings.setValue('vmax8', self.main_ui.vmax8.text().replace(',','.'))
        self.settings.setValue('vmin9', self.main_ui.vmin9.text().replace(',','.'))
        self.settings.setValue('vmax9', self.main_ui.vmax9.text().replace(',','.'))

        self.close()
        logger.info("Изменены настройки границ аварийных значений")

    def cancel_clicked(self):
        self.close()


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        # uic.loadUi("win.ui", self)
        self.main_ui = win.Ui_MainWindow()
        self.main_ui.setupUi(self)


    # def __init__(self):
    #     QtWidgets.QMainWindow.__init__(self)
    #     self.main_ui = wind.Ui_Dialog()
    #     self.main_ui.setupUi(self)

######################################################################
######################################################################

        self.settings = QtCore.QSettings('R@RMonitor', 'context')
        self.registration()
        self.getsetting()
        self.setalarmget = QtCore.QSettings('R@RMonitor', 'setalarm')

        self.w = None

        self.main_ui.StartOpros.clicked.connect(self.on_button_start)
        self.main_ui.StopOpros.clicked.connect(self.on_button_stop)

        self.main_ui.block.clicked.connect(self.buttonblock)
        self.main_ui.tabWidget.tabBarClicked.connect(self.changepage)
        #####################  Поток опроса #################################################
        self.mythread = bible.MyThread()
        self.mythread.signal_data.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.mythread.finished.connect(self.on_finished)
        #####################  Основное меню  ###############################################
        self.main_ui.exitapp.triggered.connect(self.ExitButtonClick)
        self.main_ui.about.triggered.connect(self.Dlgabout)
        self.main_ui.setalarm.triggered.connect(self.settingalarm)


    def registration(self):
        if self.settings.contains("R@R"):
            regdata = self.settings.value('R@R')
            print(regdata)
            if regdata != datetime.date(1917,11,7):
                if (datetime.date.today() - regdata).days > 30:

                    dialog = QtWidgets.QDialog()
                    dialog.setWindowTitle("Внимание!")
                    layout = QtWidgets.QVBoxLayout()

                    message = QtWidgets.QLabel("Внимание! Истёк срок пробного периода.")
                    layout.addWidget(message)
                    message = QtWidgets.QLabel("Введите код регистрации 369:")
                    layout.addWidget(message)
                    dialog.inpkod = QtWidgets.QLineEdit()
                    # inpkod = QtWidgets.QLineEdit()
                    layout.addWidget(dialog.inpkod)

                    buttonBox = QDialogButtonBox()
                    okButton = buttonBox.addButton("Ok", QDialogButtonBox.AcceptRole)
                    cancelButton = buttonBox.addButton("Отмена", QDialogButtonBox.RejectRole)
                    layout.addWidget(buttonBox)

                    def handleButton(button):
                        if button == okButton:

                            if dialog.inpkod.text() == '1917':
                                self.settings.setValue('R@R', datetime.date(1917,11,7))
                                QMessageBox(dialog, "Сообщение", "Зарегистрированно.", buttons=QMessageBox.Ok)
                                logger.info("Программа зарегистрированна.")
                            dialog.close()
                            logger.info("Ошибка регистрации.")
                            logger.info("Завершение работы программы.")
                            sys.exit()
                        else:
                            logger.info("Завершение работы программы.")
                            sys.exit()

                    buttonBox.accepted.connect(lambda: handleButton(okButton))
                    buttonBox.rejected.connect(lambda: handleButton(cancelButton))

                    dialog.setLayout(layout)
                    dialog.exec_()
            #     else:
            # self.settings.setValue('R@R', datetime.date.today())

    def changepage(self, page):
        if page==1:
            res = bible.readcondition(self.main_ui.Host.text(), self.main_ui.Port.text())
            if res[0] == 'good':
                if res[1] == 1:
                    self.main_ui.condition.setText("Программа активна.")
                    self.main_ui.block.setText("Блокировать")
                else:
                    self.main_ui.condition.setText("Программа заблокирована.")
                    self.main_ui.block.setText("Разблокировать")
            else:
                self.main_ui.condition.setText("Состояние не прочитано.")
                self.main_ui.block.setText("Не доступно")
                self.main_ui.block.setDisabled(True)
                logger.error("Ошибка чтения данных.")

                button = QMessageBox.critical(self, "Ошибка!", "Ошибка чтения данных.", buttons=QMessageBox.Ok, )

    def buttonblock(self):

        bible.blockunblock(self.main_ui.Host.text(), self.main_ui.Port.text())

        res = bible.readcondition(self.main_ui.Host.text(), self.main_ui.Port.text())
        if res[0] == 'err':
            logger.error("Ошибка чтения данных.")
            button = QMessageBox.critical(self, "Ошибка!", "Ошибка чтения данных.", buttons=QMessageBox.Ok, )
            return

        if res[1] == 1:
            self.main_ui.condition.setText("Программа активна.")
            self.main_ui.block.setText("Блокировать")
        else:
            self.main_ui.condition.setText("Программа заблокирована.")
            self.main_ui.block.setText("Разблокировать")

    def settingalarm(self):

        if self.w is None:
            self.w = setWin()
            self.w.setWindowTitle("Настройки аварийных порогов.")
            self.w.show()
        else:
            self.w.show()
            # self.w.close()  # Close window.
            # self.w = None  # Discard reference.

    def on_button_start(self):

        if self.main_ui.Host.text().count('.') != 3:
            logger.info("Неправельный HOST")
            return

        if not self.main_ui.Port.text().isdigit():
            logger.info("Неправельный port")
            return

        res = bible.readcondition(self.main_ui.Host.text(), self.main_ui.Port.text())
        if res[0] == 'err':
            t = time.localtime()
            _time = time.strftime("%H:%M:%S", t)
            errorFormat = '<span style="color:red;">{}</span>'
            self.main_ui.textEdit.append(errorFormat.format(_time + ' Ошибка чтения данных с контроллера.'))

            logger.error("Ошибка чтения данных.")
            button = QMessageBox.critical(self, "Ошибка!", "Ошибка чтения данных.", buttons=QMessageBox.Ok, )
            return

        self.settings.setValue('host', self.main_ui.Host.text())
        self.settings.setValue('port', self.main_ui.Port.text())
        self.settings.setValue('interval', self.main_ui.interval.text())
        self.rangalarm = self.getset()
        self.default_background_color()
        self.main_ui.StartOpros.setDisabled(True)  # Делаем кнопку неактивной
        self.mythread.host = self.main_ui.Host.text()
        self.mythread.port = int(self.main_ui.Port.text())
        self.mythread.interval = int(self.main_ui.interval.text())
        # self.main_ui.StartOpros.setStyleSheet('background-color: rgb(255, 254, 240)')
        t = time.localtime()
        _time = time.strftime("%H:%M:%S", t)
        self.main_ui.textEdit.append(_time + ' Старт опроса.')


        try:
            logger.info("Запуск опроса.")
            self.mythread.start()  # Запускаем поток
        except IOError as err:
            logger.info("Ошибка запуска. " + err)
            print("I/O error({0}): {1}".format(err.errno, err.strerror))

    def on_button_stop(self):

        # db.convertDBtoCSV()

        try:
            if self.mythread.running is False:
                pass
                # self.mythread.running = True
                # self.main_ui.StartOpros.setDisabled(True)
            else:
                self.mythread.running = False
                self.main_ui.StartOpros.setDisabled(False)
                time.sleep(1)
                t = time.localtime()
                _time = time.strftime("%H:%M:%S", t)
                self.main_ui.textEdit.append(_time + ' Завершение опроса.')
                self.win.close()

        except:
            pass

    def default_background_color(self):

        for pos in range(0,9):
            key = list(self.rangalarm.keys())[pos]
            getattr(self.main_ui, key).setStyleSheet('background-color: rgb(255, 254, 240)')

    def control_alarm(self, data):
        err = False

        for pos in range(0,9):
            rangMinMax = list(self.rangalarm.values())[pos]
            if rangMinMax[0] == rangMinMax[1] == '0':
                continue
            key = list(self.rangalarm.keys())[pos]
            val = data[pos]
            getattr(self.main_ui, key).setStyleSheet('background-color: green')
            if float(rangMinMax[0]) > val:
                # print(float(rangMinMax[0]), val, key)
                getattr(self.main_ui, key).setStyleSheet('background-color: red')
                err = True
            else:
                getattr(self.main_ui, key).setStyleSheet('background-color: rgb(255, 254, 240)')

            if float(rangMinMax[1]) < val:
                getattr(self.main_ui, key).setStyleSheet('background-color: red')
                err = True
            else:
                getattr(self.main_ui, key).setStyleSheet('background-color: rgb(255, 254, 240)')

        return err

    def on_change(self, data_):

        if data_[13]:
            t = time.localtime()
            _time = time.strftime("%H:%M:%S", t)
            errorFormat = '<span style="color:red;">{}</span>'
            self.main_ui.textEdit.append(errorFormat.format(_time + ' Ошибка чтения данных с контроллера.'))

            button = QMessageBox.critical(self, "Ошибка!", "Ошибка чтения данных.", buttons=QMessageBox.Ok,)
            # return
        # Если установлен контроль аварий
        err = False
        if True if self.setalarmget.value('userangealarm') == 'true' else False:
            err = self.control_alarm(data_)

        # # # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # self.d1.append(time.time())
        # self.d2.append(data_[0])
        # self.d3.append(data_[4])
        # if self.d1.__len__() > 10:
        #     self.d1.pop(0)
        #     self.d2.pop(0)
        #     self.d3.pop(0)
        #     # self.d3.pop(0)
        # self.d1[:-1] = self.d1[1:]
        # self.d2[:-1] = self.d2[1:]
        # self.d3[:-1] = self.d3[1:]
        # # self.d4[:-1] = self.d4[1:]
        # self.ptr1 += 1
        # self.curve.setData(self.d2)
        # self.curve.setPos(self.ptr1, 0)
        # self.curve2.setData(self.d3)
        # self.curve2.setPos(self.ptr1, 0)
        # # self.curve3.setData(self.d3)
        # # self.curve3.setPos(self.ptr1, 0)
        # # self.curve4.setData(self.d4)
        # # self.curve4.setPos(self.ptr1, 0)
        #
        # # # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        t = time.localtime()
        _time = time.strftime("%H:%M:%S", t)
        if err:
            errorFormat = '<span style="color:red;">{}</span>'
            self.main_ui.textEdit.append(errorFormat.format(_time + ' '+ str(data_).replace(', False', '')))

        else:
            validFormat = '<span style="color:green;">{}</span>'
            self.main_ui.textEdit.append(validFormat.format(_time + ' ' + str(data_).replace(', False', '')))

        try:
            self.main_ui.reg3137.setText(str(data_[0]))
            self.main_ui.reg3139.setText(str(data_[1]))
            self.main_ui.reg3141.setText(str(data_[2]))
            self.main_ui.reg3143.setText(str(data_[3]))
            self.main_ui.reg3145.setText(str(data_[4]))
            self.main_ui.reg3154.setText(str(data_[5]))
            self.main_ui.reg3156.setText(str(data_[6]))
            self.main_ui.reg1280.setText(str(data_[7]))
            self.main_ui.reg1282.setText(str(data_[8]))
            self.main_ui.reg1283.setText(str(data_[9]))
            self.main_ui.reg3161.setText(str(data_[10]))
            self.main_ui.reg3162.setText(str(data_[11]))
            self.main_ui.reg3163.setText(str(data_[12]))
            mask = "{:0>15}".format(bin(data_[10])[2:])
            self.main_ui.mask3161_1.setChecked(bool(int(mask[14])))
            self.main_ui.mask3161_2.setChecked(bool(int(mask[13])))
            self.main_ui.mask3161_3.setChecked(bool(int(mask[12])))
            self.main_ui.mask3161_4.setChecked(bool(int(mask[11])))
            self.main_ui.mask3161_5.setChecked(bool(int(mask[10])))
            self.main_ui.mask3161_6.setChecked(bool(int(mask[9])))
            self.main_ui.mask3161_7.setChecked(bool(int(mask[8])))
            self.main_ui.mask3161_8.setChecked(bool(int(mask[7])))
            self.main_ui.mask3161_9.setChecked(bool(int(mask[6])))
            self.main_ui.mask3161_10.setChecked(bool(int(mask[5])))
            self.main_ui.mask3161_11.setChecked(bool(int(mask[4])))
            self.main_ui.mask3161_12.setChecked(bool(int(mask[3])))
            self.main_ui.mask3161_13.setChecked(bool(int(mask[2])))
            self.main_ui.mask3161_14.setChecked(bool(int(mask[1])))
            self.main_ui.mask3161_15.setChecked(bool(int(mask[0])))
            mask = "{:0>15}".format(bin(data_[11])[2:])
            self.main_ui.mask3162_1.setChecked(bool(int(mask[14])))
            self.main_ui.mask3162_2.setChecked(bool(int(mask[13])))
            self.main_ui.mask3162_3.setChecked(bool(int(mask[12])))
            self.main_ui.mask3162_4.setChecked(bool(int(mask[11])))
            self.main_ui.mask3162_5.setChecked(bool(int(mask[10])))
            self.main_ui.mask3162_6.setChecked(bool(int(mask[9])))
            self.main_ui.mask3162_7.setChecked(bool(int(mask[8])))
            self.main_ui.mask3162_8.setChecked(bool(int(mask[7])))
            self.main_ui.mask3162_9.setChecked(bool(int(mask[6])))
            self.main_ui.mask3162_10.setChecked(bool(int(mask[5])))
            self.main_ui.mask3162_11.setChecked(bool(int(mask[4])))
            self.main_ui.mask3162_12.setChecked(bool(int(mask[3])))
            self.main_ui.mask3162_13.setChecked(bool(int(mask[2])))
            self.main_ui.mask3162_14.setChecked(bool(int(mask[1])))
            self.main_ui.mask3162_15.setChecked(bool(int(mask[0])))
            mask = "{:0>7}".format(bin(data_[12])[2:])
            self.main_ui.mask3163_1.setChecked(bool(int(mask[6])))
            self.main_ui.mask3163_2.setChecked(bool(int(mask[5])))
            self.main_ui.mask3163_3.setChecked(bool(int(mask[4])))
            self.main_ui.mask3163_4.setChecked(bool(int(mask[3])))
            self.main_ui.mask3163_5.setChecked(bool(int(mask[2])))
            self.main_ui.mask3163_6.setChecked(bool(int(mask[1])))
            self.main_ui.mask3163_7.setChecked(bool(int(mask[0])))
        except Exception as err:
            logger.info("Ошибка обновления данных формы. {err}".format(err=err))

    def on_finished(self):  # Вызывается при завершении потока
        # ui.label.setText("Вызван метод on_finished()")
        self.main_ui.StartOpros.setDisabled(False)  # Делаем+-+-* кнопку активной
        logger.info("Завершение опроса.")

    def ExitButtonClick(self):
        logger.info("Завершение работы программы.")
        sys.exit()

    def Dlgabout(self):

        # getattr(self, "mask3161_1").setStyleSheet('background-color: #fddeff')
        dlg = AboutDialog()
        dlg.setModal(True)
        dlg.setWindowTitle("О программе")
        dlg.exec()

    def getsetting(self):
        if self.settings.contains("host"):
            self.main_ui.Host.setText(self.settings.value('host'))
        # else:
        #     self.settings.setValue('theme_selection', 'Dark')

        if self.settings.contains("port"):
            self.main_ui.Port.setText(self.settings.value('port'))

        if self.settings.contains("interval"):
            self.main_ui.interval.setValue(int(self.settings.value('interval')))

    def getset(self):
        rangealarm = {'reg3137': [0, 0],
                      'reg3139': [0, 0],
                      'reg3141': [0, 0],
                      'reg3143': [0, 0],
                      'reg3145': [0, 0],
                      'reg3154': [0, 0],
                      'reg3156': [0, 0],
                      'reg1280': [0, 0],
                      'reg1282': [0, 0],
                      'reg1283': [0, 0],
                      'reg3161': [0, 0],
                      'reg3162': [0, 0],
                      'reg3163': [0, 0]}

        if self.setalarmget.contains("vmin"):
            mi = self.setalarmget.value('vmin')
        else:
            self.setalarmget.setValue('vmin', '0')
            mi = 0
        if self.setalarmget.contains("vmax"):
            ma = self.setalarmget.value('vmax')
        else:
            self.setalarmget.setValue('vmax', '0')
            ma = 0
        rangealarm['reg3137'] = [mi, ma]

        if self.setalarmget.contains("vmin1"):
            mi = self.setalarmget.value('vmin1')
        else:
            self.setalarmget.setValue('vmin1', '0')
            mi = 0
        if self.setalarmget.contains("vmax1"):
            ma = self.setalarmget.value('vmax1')
        else:
            self.setalarmget.setValue('vmax1', '0')
            ma = 0
        rangealarm['reg3139'] = [mi, ma]

        if self.setalarmget.contains("vmin2"):
            mi = self.setalarmget.value('vmin2')
        else:
            self.setalarmget.setValue('vmin2', '0')
            mi = 0
        if self.setalarmget.contains("vmax2"):
            ma = self.setalarmget.value('vmax2')
        else:
            self.setalarmget.setValue('vmax2', '0')
            ma = 0
        rangealarm['reg3141'] = [mi, ma]

        if self.setalarmget.contains("vmin3"):
            mi = self.setalarmget.value('vmin3')
        else:
            mi = self.setalarmget.setValue('vmin3', '0')
        if self.setalarmget.contains("vmax3"):
            ma = self.setalarmget.value('vmax3')
        else:
            self.setalarmget.setValue('vmax3', '0')
            ma = 0
        rangealarm['reg3143'] = [mi, ma]

        if self.setalarmget.contains("vmin4"):
            mi = self.setalarmget.value('vmin4')
        else:
            self.setalarmget.setValue('vmin4', '0')
            mi = 0
        if self.setalarmget.contains("vmax4"):
            ma = self.setalarmget.value('vmax4')
        else:
            self.setalarmget.setValue('vmax4', '0')
            ma = 0
        rangealarm['reg3145'] = [mi, ma]

        if self.setalarmget.contains("vmin5"):
            mi = self.setalarmget.value('vmin5')
        else:
            self.setalarmget.setValue('vmin5', '0')
            mi = 0
        if self.setalarmget.contains("vmax5"):
            ma = self.setalarmget.value('vmax5')
        else:
            self.setalarmget.setValue('vmax5', '0')
            ma = 0
        rangealarm['reg3154'] = [mi, ma]

        if self.setalarmget.contains("vmin6"):
            mi = self.setalarmget.value('vmin6')
        else:
            self.setalarmget.setValue('vmin6', '0')
            mi = 0
        if self.setalarmget.contains("vmax6"):
            ma = self.setalarmget.value('vmax6')
        else:
            self.setalarmget.setValue('vmax6', '0')
            ma = 0
        rangealarm['reg3156'] = [mi, ma]

        if self.setalarmget.contains("vmin7"):
            mi = self.setalarmget.value('vmin7')
        else:
            self.setalarmget.setValue('vmin7', '0')
            mi = 0
        if self.setalarmget.contains("vmax7"):
            ma = self.setalarmget.value('vmax7')
        else:
            self.setalarmget.setValue('vmax7', '0')
            ma = 0
        rangealarm['reg1280'] = [mi, ma]

        if self.setalarmget.contains("vmin8"):
            mi = self.setalarmget.value('vmin8')
        else:
            self.setalarmget.setValue('vmin8', '0')
            mi = 0
        if self.setalarmget.contains("vmax8"):
            ma = self.setalarmget.value('vmax8')
        else:
            self.setalarmget.setValue('vmax8', '0')
            ma = 0
        rangealarm['reg1282'] = [mi, ma]

        if self.setalarmget.contains("vmin9"):
            mi = self.setalarmget.value('vmin9')
        else:
            self.setalarmget.setValue('vmin9', '0')
            mi = 0
        if self.setalarmget.contains("vmax9"):
            ma = self.setalarmget.value('vmax9')
        else:
            self.setalarmget.setValue('vmax9', '0')
            ma = 0
        rangealarm['reg1283'] = [mi, ma]

        return rangealarm

    def closeEvent(self, event):
        if self.w:
            self.w.close()
######################################################################
######################################################################

if __name__ == "__main__":
    ui = MainWindow()
    ui.setWindowTitle("Основное окно")

    ui.show()
    sys.exit(app.exec_())
