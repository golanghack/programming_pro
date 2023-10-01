#! /usr/bin/env python3 

import sys
import os
import socket
import pickle
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from upload_client_gui import Ui_MainWindow

class gui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('localhost', 9090))

        self.download_folder = None
        self.ui.pushButton.clicked.connect(self.get_folder)
        self.ui.pushButton_2.clicked.connect(self.send_msg)

    # выбор даты выгружаемого отчета 
    def calendar_date(self):
        date = self.ui.calendarWidget.selectedDate()
        string_date = str(date.toPyDate())
        return string_date

    # открывается проводник для выбора папки в которую будет сохраняться файл
    def get_folder(self):
        try:
            self.download_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберете папку для сохранения')
            os.chdir(self.download_folder)
            print(self.download_folder)
        except:
            pass

    # отправка даты на сервер через сокет
    def send_msg(self):
        msg = self.calendar_date()
        print(msg)
        self.sock.send(msg.encode('utf-8'))

    # принятие ответа сервера
    def recv_msg(self):
        data = self.sock.recv(10240)
        data = pickle.loads(data, encoding='utf-8')
        rep_file = data.to_csv('report_df.csv', index=False)
        target_fld = self.get_folder()
        os.path.join(str(target_fld), rep_file)
        print('file upload')
        self.sock.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = gui()
    win.show()
    sys.exit(app.exec())