from PySide2.QtCore import Slot, Qt, QTimer
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QSlider
)


def format_show(seconds):
    if seconds > 0:
        minutes = seconds // 60
        minutes = '{}{}'.format(0, minutes) if minutes < 10 else str(minutes)
        rest_seconds = seconds % 60
        rest_seconds = '{}{}'.format(0, rest_seconds) if rest_seconds < 10 else str(rest_seconds)
        return '{}:{}'.format(minutes, rest_seconds)
    else:
        return '00:00'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('计时器')
        # self.resize(320, 480)
        self.setFixedSize(320, 480)

        # 布局
        layout = QVBoxLayout()

        # 时间显示
        self.show_time = QLabel('00:00')
        self.show_time.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.show_time)

        # 时间控制
        self.setting_time = QSlider(Qt.Horizontal)
        self.setting_time.setRange(0, 60)
        self.setting_time.valueChanged.connect(self.setting_change)
        layout.addWidget(self.setting_time)

        # 开始按钮
        self.start_button = QPushButton('START')
        # 信号和插槽连接
        self.start_button.clicked.connect(self.start_timer)
        layout.addWidget(self.start_button)

        # 停止按钮
        self.stop_button = QPushButton('STOP')
        self.stop_button.clicked.connect(self.stop_timer)
        layout.addWidget(self.stop_button)

        # space
        space = QWidget()
        space.setFixedHeight(10)
        layout.addWidget(space)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # 计时器
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.refresh_show)

        # 自定义的属性
        # 秒
        self.current_time = 0

        # QSS
        self.setStyleSheet("""
            QLabel {
                font-size: 80px;
                font-weight: bold;
                border: 1px solid #000;
            }
            
            QSlider {
                margin: 20
            }
            
            QPushButton {
                height: 35px;
                font-weight: bold;
                font-size: 16px;
            }
            
        """)

    @Slot()
    def start_timer(self):
        print('start timer')
        self.timer.start()
        self.start_button.setEnabled(False)
        self.start_button.repaint()
        self.setting_time.setEnabled(False)
        self.setting_time.repaint()

    @Slot()
    def stop_timer(self):
        print('stop timer')
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.start_button.repaint()
        self.setting_time.setEnabled(True)
        self.setting_time.repaint()

    @Slot()
    def setting_change(self, value):
        print('setting change:', value)
        self.current_time = value
        show = format_show(value)
        self.show_time.setText(show)

    @Slot()
    def refresh_show(self):
        self.current_time -= 1
        self.setting_time.setValue(self.current_time)
        if self.current_time >= 0:
            show = format_show(self.current_time)
            print(show)
            self.show_time.setText(show)
        else:
            self.stop_timer()


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
