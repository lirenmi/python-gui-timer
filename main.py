from PySide2.QtCore import Slot
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMainWindow
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('计时器')
        # self.resize(320, 480)
        self.setFixedSize(320, 480)

        self.start_button = QPushButton('START')
        self.start_button.setCheckable(True)
        # 信号和插槽连接
        self.start_button.clicked.connect(self.start_timer)

        self.setCentralWidget(self.start_button)

    @Slot()
    def start_timer(self, checked):
        print('start timer, ', checked)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()

# import time
#
# print('请输入时长：')
# target_time = input()
#
#
# def timer():
#     for i in range(int(target_time), 0, -1):
#         # 00:23
#         print(format_show(i))
#         time.sleep(1)
#
#
# def format_show(seconds):
#     if seconds > 0:
#         minutes = seconds // 60
#         minutes = '{}{}'.format(0, minutes) if minutes < 10 else str(minutes)
#         rest_seconds = seconds % 60
#         rest_seconds = '{}{}'.format(0, rest_seconds) if rest_seconds < 10 else str(rest_seconds)
#         return '{}:{}'.format(minutes, rest_seconds)
#     else:
#         return '00:00'
#
#
# timer()
