# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/uis/new_operator.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewOperator(object):
    def setupUi(self, NewOperator):
        NewOperator.setObjectName("NewOperator")
        NewOperator.resize(460, 316)
        font = QtGui.QFont()
        font.setPointSize(10)
        NewOperator.setFont(font)
        NewOperator.setSizeGripEnabled(False)
        NewOperator.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewOperator)
        self.buttonBox.setGeometry(QtCore.QRect(160, 280, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(NewOperator)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 421, 244))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.formLayoutWidget.setFont(font)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.Username = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Username.setFont(font)
        self.Username.setObjectName("Username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Username)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Fullname = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Fullname.setFont(font)
        self.Fullname.setObjectName("Fullname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Fullname)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Phone = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Phone.setFont(font)
        self.Phone.setObjectName("Phone")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Phone)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Email = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Email.setFont(font)
        self.Email.setObjectName("Email")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Email)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Password1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password1.setFont(font)
        self.Password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password1.setObjectName("Password1")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Password1)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Password2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password2.setFont(font)
        self.Password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password2.setObjectName("Password2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Password2)
        self.Organization = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Organization.setFont(font)
        self.Organization.setObjectName("Organization")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Organization)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Role = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Role.setFont(font)
        self.Role.setObjectName("Role")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Role)

        self.retranslateUi(NewOperator)
        self.buttonBox.accepted.connect(NewOperator.accept)
        self.buttonBox.rejected.connect(NewOperator.reject)
        QtCore.QMetaObject.connectSlotsByName(NewOperator)
        NewOperator.setTabOrder(self.Username, self.Fullname)
        NewOperator.setTabOrder(self.Fullname, self.Organization)
        NewOperator.setTabOrder(self.Organization, self.Role)
        NewOperator.setTabOrder(self.Role, self.Phone)
        NewOperator.setTabOrder(self.Phone, self.Email)
        NewOperator.setTabOrder(self.Email, self.Password1)
        NewOperator.setTabOrder(self.Password1, self.Password2)

    def retranslateUi(self, NewOperator):
        _translate = QtCore.QCoreApplication.translate
        NewOperator.setWindowTitle(_translate("NewOperator", "New operator"))
        self.label.setText(_translate("NewOperator", "Username"))
        self.label_2.setText(_translate("NewOperator", "Fullname"))
        self.label_3.setText(_translate("NewOperator", "Organization"))
        self.label_4.setText(_translate("NewOperator", "Phone"))
        self.label_5.setText(_translate("NewOperator", "Email"))
        self.label_6.setText(_translate("NewOperator", "Password"))
        self.label_7.setText(_translate("NewOperator", "Password confirm"))
        self.label_8.setText(_translate("NewOperator", "Role"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewOperator = QtWidgets.QDialog()
    ui = Ui_NewOperator()
    ui.setupUi(NewOperator)
    NewOperator.show()
    sys.exit(app.exec_())
