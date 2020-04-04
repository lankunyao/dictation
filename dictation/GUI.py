# coding:utf-8

import sys
import qtawesome
from PyQt5 import QtGui, QtCore, QtWidgets


class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_layout = QtWidgets.QGridLayout()

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.book', color='white'), "单词本")
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.search', color='white'), "查询单词")
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.bookmark', color='white'), "收藏夹")

        self.right_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.right_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.right_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.right_button_start = QtWidgets.QPushButton("开始")
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(640, 480)
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget.setObjectName('left_widget')
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget.setObjectName('right_widget')
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 3, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 3, 6)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_button_1.setObjectName('left_button')
        self.left_button_2.setObjectName('left_button')
        self.left_button_3.setObjectName('left_button')

        self.right_button_start.setObjectName('right_start')

        self.left_layout.addWidget(self.left_button_1, 0, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 2, 0, 1, 3)

        self.right_layout.addWidget(self.right_button_start, 0, 2, 3, 3)
        self.QSS()

    def QSS(self):
        self.left_widget.setStyleSheet('''
        QPushButton{
        color: rgb(137, 221, 255);
        background-color: rgb(37, 121, 255);
        border-style:none;
        border:1px solid rgb(37, 121, 255); 

        padding:5px;
        min-height:20px;
        border-radius:15px;
        }
        ''')

        self.right_widget.setStyleSheet('''
        QPushButton#right_start{
        font-family: "KaiTi";
        font-weight: bold;
        font-size: 60px;
        
        color: rgb(137, 221, 255);
        background-color: rgb(84, 255, 159);
        border-style:none;
        border:1px solid rgb(84, 255, 159); 
        
        padding:5px;
        min-height:30px;
        border-radius:30px;
        }
        ''')


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
