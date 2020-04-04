# coding:utf-8

import GUI
import sys
from PyQt5 import QtWidgets
import dataset


class Operate(GUI.MainUI, dataset.Dataset):
    def __init__(self):
        super.__init__()

    def get_question(self):
        print("")


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI.MainUI()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
