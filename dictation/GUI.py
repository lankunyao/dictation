# coding:utf-8

import sys
import qtawesome
from PyQt5 import QtGui, QtCore, QtWidgets
import dataset
import random


class MainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.database = dataset.Dataset()
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget_2 = QtWidgets.QWidget()
        self.right_layout_2 = QtWidgets.QGridLayout()
        self.right_widget_3 = QtWidgets.QWidget()
        self.right_layout_3 = QtWidgets.QGridLayout()
        self.right_widget_4 = QtWidgets.QWidget()
        self.right_layout_4 = QtWidgets.QGridLayout()

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.book', color='white'), "单词本")
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.search', color='white'), "查询单词")
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.bookmark', color='white'), "收藏夹")

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.right_button_start = QtWidgets.QPushButton("开始")

        self.right_label = QtWidgets.QLabel("")
        self.right_button_1 = QtWidgets.QPushButton("")
        self.right_button_2 = QtWidgets.QPushButton("")
        self.right_button_3 = QtWidgets.QPushButton("")
        self.right_button_4 = QtWidgets.QPushButton("")
        self.right_label_2 = QtWidgets.QLabel("")
        self.right_label_3 = QtWidgets.QLabel("")
        self.right_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.chevron-right'), "下一个")

        self.right_number = 0

        self.init_ui()

    def init_ui(self):
        self.setFixedSize(400, 420)
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget.setObjectName('left_widget')
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget.setObjectName('right_widget')
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.right_widget_2.setObjectName('right_widget_2')
        self.right_widget_2.setLayout(self.right_layout_2)

        self.right_widget_3.setObjectName('right_widget_3')
        self.right_widget_3.setLayout(self.right_layout_3)

        self.right_widget_4.setObjectName('right_widget_4')
        self.right_widget_4.setLayout(self.right_layout_4)

        self.main_layout.addWidget(self.left_widget, 0, 0, 8, 3)
        self.main_layout.addWidget(self.right_widget, 0, 3, 8, 9)
        self.main_layout.addWidget(self.right_widget_2, 0, 3, 8, 9)
        self.main_layout.addWidget(self.right_widget_3, 0, 3, 8, 9)
        self.main_layout.addWidget(self.right_widget_4, 0, 3, 8, 9)
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.right_widget.show()
        self.right_widget_2.hide()
        self.right_widget_3.hide()
        self.right_widget_4.hide()

        self.left_button_1.setObjectName('left_button')
        self.left_button_2.setObjectName('left_button')
        self.left_button_3.setObjectName('left_button')

        self.right_button_start.setObjectName('right_start')

        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)

        self.left_layout.addWidget(self.left_button_1, 2, 0, 2, 3)
        self.left_layout.addWidget(self.left_button_2, 4, 0, 2, 3)
        self.left_layout.addWidget(self.left_button_3, 6, 0, 2, 3)

        self.right_layout.addWidget(self.right_button_start)

        self.right_button_start.setFixedSize(200, 200)
        self.left_close.setFixedSize(30, 30)
        self.left_mini.setFixedSize(30, 30)

        self.setWindowOpacity(0.9)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.main_layout.setSpacing(0)

        self.left_close.clicked.connect(self.close)
        self.left_mini.clicked.connect(self.showMinimized)
        self.right_button_start.clicked.connect(self.dictation)

        self.right_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.right_label_2.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.right_label_3.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        self.right_button_5.clicked.connect(self.dictation)

        self.right_label.adjustSize()
        self.right_label_2.adjustSize()
        self.right_label_2.adjustSize()

        self.left_button_1.clicked.connect(self.show_words)
        self.left_button_2.clicked.connect(self.search_words)
        self.left_button_3.clicked.connect(self.favorite_words)

        self.QSS()

    def dictation(self):
        self.right_widget.hide()
        self.right_widget_2.show()
        self.right_widget_3.hide()
        self.right_widget_4.hide()

        self.right_button_1.setObjectName('right_button')
        self.right_button_2.setObjectName('right_button')
        self.right_button_3.setObjectName('right_button')
        self.right_button_4.setObjectName('right_button')

        self.right_label.setObjectName('right_label')
        self.right_label_2.setObjectName('right_label_2')
        self.right_label_2.setObjectName('right_label_3')

        self.right_layout_2.addWidget(self.right_label)
        self.right_layout_2.addWidget(self.right_button_1)
        self.right_layout_2.addWidget(self.right_button_2)
        self.right_layout_2.addWidget(self.right_button_3)
        self.right_layout_2.addWidget(self.right_button_4)

        self.choose_right_choice()

    def choose_right_choice(self):
        self.database.random_select()
        self.database.wrong_choice_select()
        self.right_label.setText(self.database.word)
        self.right_number = random.randint(1, 4)
        print(self.right_number)
        if self.right_number == 1:
            self.right_button_1.setText(self.database.right_choice)
            self.right_button_2.setText(self.database.wrong_choice[0])
            self.right_button_3.setText(self.database.wrong_choice[1])
            self.right_button_4.setText(self.database.wrong_choice[2])
            self.right_button_1.clicked.connect(self.right_answer)
            self.right_button_2.clicked.connect(self.wrong_answer)
            self.right_button_3.clicked.connect(self.wrong_answer)
            self.right_button_4.clicked.connect(self.wrong_answer)
        elif self.right_number == 2:
            self.right_button_2.setText(self.database.right_choice)
            self.right_button_1.setText(self.database.wrong_choice[0])
            self.right_button_3.setText(self.database.wrong_choice[1])
            self.right_button_4.setText(self.database.wrong_choice[2])
            self.right_button_2.clicked.connect(self.right_answer)
            self.right_button_1.clicked.connect(self.wrong_answer)
            self.right_button_3.clicked.connect(self.wrong_answer)
            self.right_button_4.clicked.connect(self.wrong_answer)
        elif self.right_number == 3:
            self.right_button_3.setText(self.database.right_choice)
            self.right_button_2.setText(self.database.wrong_choice[0])
            self.right_button_1.setText(self.database.wrong_choice[1])
            self.right_button_4.setText(self.database.wrong_choice[2])
            self.right_button_3.clicked.connect(self.right_answer)
            self.right_button_2.clicked.connect(self.wrong_answer)
            self.right_button_1.clicked.connect(self.wrong_answer)
            self.right_button_4.clicked.connect(self.wrong_answer)
        elif self.right_number == 4:
            self.right_button_4.setText(self.database.right_choice)
            self.right_button_2.setText(self.database.wrong_choice[0])
            self.right_button_3.setText(self.database.wrong_choice[1])
            self.right_button_1.setText(self.database.wrong_choice[2])
            self.right_button_4.clicked.connect(self.right_answer)
            self.right_button_2.clicked.connect(self.wrong_answer)
            self.right_button_3.clicked.connect(self.wrong_answer)
            self.right_button_1.clicked.connect(self.wrong_answer)

    def right_answer(self):
        if self.right_number == 1:
            self.right_button_1.clicked.disconnect(self.right_answer)
            self.right_button_2.clicked.disconnect(self.wrong_answer)
            self.right_button_3.clicked.disconnect(self.wrong_answer)
            self.right_button_4.clicked.disconnect(self.wrong_answer)
        elif self.right_number == 2:
            self.right_button_2.clicked.disconnect(self.right_answer)
            self.right_button_1.clicked.disconnect(self.wrong_answer)
            self.right_button_3.clicked.disconnect(self.wrong_answer)
            self.right_button_4.clicked.disconnect(self.wrong_answer)
        elif self.right_number == 3:
            self.right_button_3.clicked.disconnect(self.right_answer)
            self.right_button_1.clicked.disconnect(self.wrong_answer)
            self.right_button_2.clicked.disconnect(self.wrong_answer)
            self.right_button_4.clicked.disconnect(self.wrong_answer)
        elif self.right_number == 4:
            self.right_button_4.clicked.disconnect(self.right_answer)
            self.right_button_1.clicked.disconnect(self.wrong_answer)
            self.right_button_3.clicked.disconnect(self.wrong_answer)
            self.right_button_2.clicked.disconnect(self.wrong_answer)
        print("right!")
        self.right_widget.hide()
        self.right_widget_2.hide()
        self.right_widget_3.show()
        self.right_widget_4.hide()
        self.right_layout_3.addWidget(self.right_label)
        self.right_label_2.setText(self.database.right_choice)
        self.right_layout_3.addWidget(self.right_label_2)
        self.right_layout_3.addWidget(self.right_button_5)

    def wrong_answer(self):
        if self.right_number == 1:
            self.right_button_1.clicked.disconnect(self.right_answer)
            self.right_button_2.clicked.disconnect(self.wrong_answer)
            self.right_button_3.clicked.disconnect(self.wrong_answer)
            self.right_button_4.clicked.disconnect(self.wrong_answer)
        elif self.right_number == 2:
            self.right_button_2.clicked.disconnect(self.right_answer)
            self.right_button_1.clicked.disconnect(self.wrong_answer)
            self.right_button_3.clicked.disconnect(self.wrong_answer)
            self.right_button_4.clicked.disconnect(self.wrong_answer)
        elif self.right_number == 3:
            self.right_button_3.clicked.disconnect(self.right_answer)
            self.right_button_1.clicked.disconnect(self.wrong_answer)
            self.right_button_2.clicked.disconnect(self.wrong_answer)
            self.right_button_4.clicked.disconnect(self.wrong_answer)
        elif self.right_number == 4:
            self.right_button_4.clicked.disconnect(self.right_answer)
            self.right_button_1.clicked.disconnect(self.wrong_answer)
            self.right_button_3.clicked.disconnect(self.wrong_answer)
            self.right_button_2.clicked.disconnect(self.wrong_answer)
        print("wrong!")
        self.right_widget.hide()
        self.right_widget_2.hide()
        self.right_widget_3.show()
        self.right_widget_4.show()
        self.right_layout_4.addWidget(self.right_label)
        self.right_label_3.setText(self.database.right_choice)
        self.right_layout_4.addWidget(self.right_label_3)
        self.right_layout_4.addWidget(self.right_button_5)

    def show_words(self):
        pass

    def search_words(self):
        pass

    def favorite_words(self):
        pass

    def QSS(self):
        self.left_close.setStyleSheet('''
        QPushButton{
        background:#F76677;
        border-radius:15px;
        }
        
        QPushButton:hover{
        background:red;
        image:url(resource/close.png);
        }
        ''')

        self.left_mini.setStyleSheet('''
        QPushButton{
        background:#6DDF6D;
        border-radius:15px;
        }

        QPushButton:hover{
        background:green;
        image:url(resource/mini.png);
        }
        ''')

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
        
        QPushButton:hover{
        background:blue;
        }
        
        QWidget#left_widget{
        background:#ebe6e6;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-left:1px solid white;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;
        }
        ''')

        self.right_widget.setStyleSheet('''
        QPushButton{
        font-family: "KaiTi";
        font-weight: bold;
        font-size: 60px;
        
        color: rgb(39, 72, 98);
        background-color: rgb(147, 224, 255);
        border-style:none;
        border:1px solid rgb(147, 224, 255); 
        
        padding:5px;
        min-height:30px;
        border-radius:100px;
        }
        
        QPushButton:hover{
        background:#00bcd4;
        }
        
        QWidget#right_widget{
        background:#f3f3f3;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-right:1px solid white;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;
        }
        ''')

        self.right_widget_2.setStyleSheet('''
        QWidget#right_widget_2{
        background:#f3f3f3;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-right:1px solid white;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;
        }
        
        QPushButton{ 
        background-color:#a6e3e9;
        border-style:none;
        border:1px solid #a6e3e9; 
        
        padding:5px;
        min-height:30px;
        border-radius:15px;
        }
        
        QPushButton:hover{
        background:#71c9ce;
        }
        
        QLabel{
        font-family: "Times New Roman";
        font-weight: bold;
        font-size: 30px;
        background-color:#a6e3e9;
        border-style:none;
        border:1px solid #a6e3e9;
        
        border-radius:15px;
        }
        ''')

        self.right_widget_3.setStyleSheet('''
        QWidget#right_widget_3{
        background:#f3f3f3;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-right:1px solid white;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;
        }
        
        QLabel{
        background-color:#30e3ca;
        border-style:none;
        border:1px solid #30e3ca;
        
        border-radius:15px;
        }
        
        QLabel#right_label{
        font-family: "Times New Roman";
        font-weight: bold;
        font-size: 30px;
        }
        
        QLabel#right_label_3{
        font-family: "KaiTi";
        font-size: 20px;
        }
        ''')

        self.right_widget_4.setStyleSheet('''
        QWidget#right_widget_4{
        background:#f3f3f3;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-right:1px solid white;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px;
        }
        
        QLabel{
        background-color:#ff2e63;
        border-style:none;
        border:1px solid #ff2e63;
        
        border-radius:15px;
        }
        
        QLabel#right_label{
        font-family: "Times New Roman";
        font-weight: bold;
        font-size: 30px;
        }
        
        QLabel#right_label_4{
        font-family: "KaiTi";
        font-size: 20px;
        }
        ''')


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
