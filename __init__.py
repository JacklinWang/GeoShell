import sys

from PyQt5.QtWidgets import QApplication,QMainWindow

from core.frame import mainwindow

import os

if __name__ == "__main__":
    print(os.getcwd())
    app = QApplication(sys.argv)# #创建QApplication类实例
    MainWindow = QMainWindow()#创建一个主窗口
    ui = mainwindow.Ui_MainWindow()#调用ui转换的代码
    ui.setupUi(MainWindow)#主窗口调用控件方法

    MainWindow.show()#进行显示
    sys.exit(app.exec_())#进入程序的主循环，并通过exit函数确保主程序安全结束