# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/uis/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Log = QtWidgets.QListWidget(self.centralwidget)
        self.Log.setGeometry(QtCore.QRect(9, 309, 621, 111))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Log.setFont(font)
        self.Log.setObjectName("Log")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 290, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Operator = QtWidgets.QGroupBox(self.centralwidget)
        self.Operator.setGeometry(QtCore.QRect(10, 0, 311, 51))
        self.Operator.setFlat(False)
        self.Operator.setObjectName("Operator")
        self.Op_new = QtWidgets.QPushButton(self.Operator)
        self.Op_new.setGeometry(QtCore.QRect(210, 20, 91, 23))
        self.Op_new.setObjectName("Op_new")
        self.Op_auth = QtWidgets.QPushButton(self.Operator)
        self.Op_auth.setEnabled(False)
        self.Op_auth.setGeometry(QtCore.QRect(160, 20, 41, 23))
        self.Op_auth.setObjectName("Op_auth")
        self.Op_username = QtWidgets.QLineEdit(self.Operator)
        self.Op_username.setGeometry(QtCore.QRect(10, 20, 141, 20))
        self.Op_username.setObjectName("Op_username")
        self.Case = QtWidgets.QGroupBox(self.centralwidget)
        self.Case.setEnabled(False)
        self.Case.setGeometry(QtCore.QRect(340, 0, 291, 51))
        self.Case.setFlat(False)
        self.Case.setObjectName("Case")
        self.Case_select = QtWidgets.QComboBox(self.Case)
        self.Case_select.setGeometry(QtCore.QRect(10, 20, 191, 22))
        self.Case_select.setCurrentText("")
        self.Case_select.setObjectName("Case_select")
        self.Case_new = QtWidgets.QPushButton(self.Case)
        self.Case_new.setGeometry(QtCore.QRect(210, 20, 71, 23))
        self.Case_new.setObjectName("Case_new")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(70, 70, 20, 20))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(320, 20, 16, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 280, 621, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Discovery = QtWidgets.QPushButton(self.centralwidget)
        self.Discovery.setEnabled(False)
        self.Discovery.setGeometry(QtCore.QRect(10, 90, 141, 41))
        self.Discovery.setDefault(False)
        self.Discovery.setFlat(False)
        self.Discovery.setObjectName("Discovery")
        self.Acquire_Evidence = QtWidgets.QPushButton(self.centralwidget)
        self.Acquire_Evidence.setEnabled(False)
        self.Acquire_Evidence.setGeometry(QtCore.QRect(10, 160, 141, 41))
        self.Acquire_Evidence.setDefault(False)
        self.Acquire_Evidence.setFlat(False)
        self.Acquire_Evidence.setObjectName("Acquire_Evidence")
        self.Store_Protect = QtWidgets.QPushButton(self.centralwidget)
        self.Store_Protect.setEnabled(False)
        self.Store_Protect.setGeometry(QtCore.QRect(330, 160, 141, 41))
        self.Store_Protect.setDefault(False)
        self.Store_Protect.setFlat(False)
        self.Store_Protect.setObjectName("Store_Protect")
        self.Print_Doc = QtWidgets.QPushButton(self.centralwidget)
        self.Print_Doc.setEnabled(False)
        self.Print_Doc.setGeometry(QtCore.QRect(170, 160, 141, 41))
        self.Print_Doc.setDefault(False)
        self.Print_Doc.setFlat(False)
        self.Print_Doc.setObjectName("Print_Doc")
        self.Send_Doc = QtWidgets.QPushButton(self.centralwidget)
        self.Send_Doc.setEnabled(False)
        self.Send_Doc.setGeometry(QtCore.QRect(410, 230, 141, 41))
        self.Send_Doc.setDefault(False)
        self.Send_Doc.setFlat(False)
        self.Send_Doc.setObjectName("Send_Doc")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setEnabled(True)
        self.Exit.setGeometry(QtCore.QRect(570, 230, 51, 41))
        self.Exit.setDefault(False)
        self.Exit.setFlat(False)
        self.Exit.setObjectName("Exit")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(440, 50, 20, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(80, 60, 371, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(70, 130, 20, 31))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(150, 170, 21, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(120, 220, 241, 20))
        self.line_9.setLineWidth(1)
        self.line_9.setMidLineWidth(0)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(310, 170, 21, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(350, 200, 20, 31))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(550, 240, 21, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(430, 200, 20, 31))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(110, 200, 20, 31))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Op_new, self.Case_select)
        MainWindow.setTabOrder(self.Case_select, self.Case_new)
        MainWindow.setTabOrder(self.Case_new, self.Discovery)
        MainWindow.setTabOrder(self.Discovery, self.Acquire_Evidence)
        MainWindow.setTabOrder(self.Acquire_Evidence, self.Print_Doc)
        MainWindow.setTabOrder(self.Print_Doc, self.Store_Protect)
        MainWindow.setTabOrder(self.Store_Protect, self.Send_Doc)
        MainWindow.setTabOrder(self.Send_Doc, self.Exit)
        MainWindow.setTabOrder(self.Exit, self.Log)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PESADES"))
        self.label.setText(_translate("MainWindow", "Session log"))
        self.Operator.setTitle(_translate("MainWindow", "Operator"))
        self.Op_new.setText(_translate("MainWindow", "New operator"))
        self.Op_auth.setText(_translate("MainWindow", "Init"))
        self.Case.setTitle(_translate("MainWindow", "Case"))
        self.Case_new.setText(_translate("MainWindow", "New case"))
        self.Discovery.setText(_translate("MainWindow", "Start discovery"))
        self.Acquire_Evidence.setText(_translate("MainWindow", "Acquire evidence"))
        self.Store_Protect.setText(_translate("MainWindow", "Store and protect"))
        self.Print_Doc.setText(_translate("MainWindow", "Print documentation"))
        self.Send_Doc.setText(_translate("MainWindow", "Send documentation"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

