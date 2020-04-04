# coding:utf-8

import GUI
import dataset
from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import operation


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI.MainUI()
    gui.show()
    words = dataset.Dataset()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
