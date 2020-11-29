# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './uis/yes_no_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_YesNoDialog(object):
    def setupUi(self, YesNoDialog):
        YesNoDialog.setObjectName("YesNoDialog")
        YesNoDialog.resize(421, 99)
        font = QtGui.QFont()
        font.setPointSize(10)
        YesNoDialog.setFont(font)
        self.buttonBox = QtWidgets.QDialogButtonBox(YesNoDialog)
        self.buttonBox.setGeometry(QtCore.QRect(250, 60, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.Info = QtWidgets.QLabel(YesNoDialog)
        self.Info.setGeometry(QtCore.QRect(10, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Info.setFont(font)
        self.Info.setAlignment(QtCore.Qt.AlignCenter)
        self.Info.setObjectName("Info")
        self.Question = QtWidgets.QLabel(YesNoDialog)
        self.Question.setGeometry(QtCore.QRect(20, 60, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Question.setFont(font)
        self.Question.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.Question.setObjectName("Question")

        self.retranslateUi(YesNoDialog)
        self.buttonBox.accepted.connect(YesNoDialog.accept)
        self.buttonBox.rejected.connect(YesNoDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(YesNoDialog)

    def retranslateUi(self, YesNoDialog):
        _translate = QtCore.QCoreApplication.translate
        YesNoDialog.setWindowTitle(_translate("YesNoDialog", "Question"))
        self.Info.setText(_translate("YesNoDialog", "<Info>"))
        self.Question.setText(_translate("YesNoDialog", "<Question>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YesNoDialog = QtWidgets.QDialog()
    ui = Ui_YesNoDialog()
    ui.setupUi(YesNoDialog)
    YesNoDialog.show()
    sys.exit(app.exec_())

