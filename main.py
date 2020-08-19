import PySide2.QtCore

# Prints PySide2 version
# e.g. 5.11.1a1
print(PySide2.__version__)

# Gets a tuple with each version component
# e.g. (5, 11, 1, 'a', 1)
print(PySide2.__version_info__)

# Prints the Qt version used to compile PySide2
# e.g. "5.11.2"
print(PySide2.QtCore.__version__)

# Gets a tuple with each version components of Qt used to compile PySide2
# e.g. (5, 11, 2)
print(PySide2.QtCore.__version_info__)



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
