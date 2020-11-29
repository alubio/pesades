# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './uis/info_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InfoDialog(object):
    def setupUi(self, InfoDialog):
        InfoDialog.setObjectName("InfoDialog")
        InfoDialog.resize(421, 99)
        font = QtGui.QFont()
        font.setPointSize(10)
        InfoDialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(InfoDialog)
        self.buttonBox.setGeometry(QtCore.QRect(320, 60, 91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Info = QtWidgets.QLabel(InfoDialog)
        self.Info.setGeometry(QtCore.QRect(10, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Info.setFont(font)
        self.Info.setAlignment(QtCore.Qt.AlignCenter)
        self.Info.setObjectName("Info")

        self.retranslateUi(InfoDialog)
        self.buttonBox.accepted.connect(InfoDialog.accept)
        self.buttonBox.rejected.connect(InfoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InfoDialog)

    def retranslateUi(self, InfoDialog):
        _translate = QtCore.QCoreApplication.translate
        InfoDialog.setWindowTitle(_translate("InfoDialog", "Information"))
        self.Info.setText(_translate("InfoDialog", "<Info>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InfoDialog = QtWidgets.QDialog()
    ui = Ui_InfoDialog()
    ui.setupUi(InfoDialog)
    InfoDialog.show()
    sys.exit(app.exec_())

