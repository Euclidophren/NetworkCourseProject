import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pyqtgraph import *
from parse.xmlParse import *

audits_path = "F:\\networkCourse\\audits"
filenames = os.listdir(audits_path)

class MainWindow(QMainWindow):

    def __init__(self):
        QWidget.__init__(self)
        uic.loadUi("mainwindow.ui", self)
        self.title = 'Network Audit'
        audits_path = "F:\\networkCourse\\audits"
        os.chdir(audits_path)


        filenames = os.listdir(audits_path)
        for f in filenames:
            item = QListWidgetItem(f.split("-")[0])
            self.device_list.addItem(item)
            self.device_list.itemClicked.connect(self.show_device_info)

    def show_device_info(self, item, files=filenames, path=audits_path):
        print('\n\n' + item.text())
        for f in files:
            print(f)
            if f.split('-')[0] == item.text():
                sys_data, processor_data, memory_data, \
                    motherboard_data, sound_data, video_card_data, network_data = \
                    parse_client_response(path + '\\' + f)

                self.system_info.clear()
                self.processor_info.clear()
                self.memory_info.clear()
                self.sound_info.clear()
                self.graphics_info.clear()
                self.network_info.clear()

                self.system_info.insertPlainText(sys_data)
                self.processor_info.insertPlainText(processor_data)
                self.memory_info.insertPlainText(memory_data)
                self.sound_info.insertPlainText(sound_data)
                self.graphics_info.insertPlainText(video_card_data)
                self.network_info.insertPlainText(network_data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())