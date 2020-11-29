# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './uis/password_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PasswordDialog(object):
    def setupUi(self, PasswordDialog):
        PasswordDialog.setObjectName("PasswordDialog")
        PasswordDialog.resize(421, 99)
        font = QtGui.QFont()
        font.setPointSize(10)
        PasswordDialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(PasswordDialog)
        self.buttonBox.setGeometry(QtCore.QRect(320, 60, 91, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Info = QtWidgets.QLabel(PasswordDialog)
        self.Info.setGeometry(QtCore.QRect(10, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Info.setFont(font)
        self.Info.setAlignment(QtCore.Qt.AlignCenter)
        self.Info.setObjectName("Info")
        self.Password = QtWidgets.QLineEdit(PasswordDialog)
        self.Password.setGeometry(QtCore.QRect(110, 60, 201, 20))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setAlignment(QtCore.Qt.AlignCenter)
        self.Password.setObjectName("Password")

        self.retranslateUi(PasswordDialog)
        self.buttonBox.accepted.connect(PasswordDialog.accept)
        self.buttonBox.rejected.connect(PasswordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PasswordDialog)

    def retranslateUi(self, PasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        PasswordDialog.setWindowTitle(_translate("PasswordDialog", "Password"))
        self.Info.setText(_translate("PasswordDialog", "<Info>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordDialog = QtWidgets.QDialog()
    ui = Ui_PasswordDialog()
    ui.setupUi(PasswordDialog)
    PasswordDialog.show()
    sys.exit(app.exec_())

