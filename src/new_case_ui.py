# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_case.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewCase(object):
    def setupUi(self, NewCase):
        NewCase.setObjectName("NewCase")
        NewCase.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(10)
        NewCase.setFont(font)
        NewCase.setSizeGripEnabled(False)
        NewCase.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewCase)
        self.buttonBox.setGeometry(QtCore.QRect(340, 430, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(NewCase)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 30, 301, 41))
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
        self.Name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Name)
        self.formLayoutWidget_2 = QtWidgets.QWidget(NewCase)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(330, 70, 291, 92))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(5)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.Notary_name = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Notary_name.setFont(font)
        self.Notary_name.setObjectName("Notary_name")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Notary_name)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Notary_phone = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Notary_phone.setFont(font)
        self.Notary_phone.setObjectName("Notary_phone")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Notary_phone)
        self.Notary_email = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Notary_email.setFont(font)
        self.Notary_email.setObjectName("Notary_email")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Notary_email)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.formLayoutWidget_3 = QtWidgets.QWidget(NewCase)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(20, 160, 561, 261))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(10, 10, 10, 10)
        self.formLayout_3.setSpacing(5)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Evidences = QtWidgets.QListWidget(self.formLayoutWidget_3)
        self.Evidences.setObjectName("Evidences")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Evidences)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Storage_media = QtWidgets.QListWidget(self.formLayoutWidget_3)
        self.Storage_media.setObjectName("Storage_media")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Storage_media)
        self.formLayoutWidget_4 = QtWidgets.QWidget(NewCase)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(20, 70, 301, 80))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(10, 10, 10, 10)
        self.formLayout_4.setSpacing(5)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Description = QtWidgets.QTextEdit(self.formLayoutWidget_4)
        self.Description.setObjectName("Description")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Description)
        self.Add_device = QtWidgets.QPushButton(NewCase)
        self.Add_device.setGeometry(QtCore.QRect(590, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Add_device.setFont(font)
        self.Add_device.setObjectName("Add_device")
        self.Del_device = QtWidgets.QPushButton(NewCase)
        self.Del_device.setEnabled(False)
        self.Del_device.setGeometry(QtCore.QRect(590, 200, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Del_device.setFont(font)
        self.Del_device.setObjectName("Del_device")
        self.Del_storage = QtWidgets.QPushButton(NewCase)
        self.Del_storage.setEnabled(False)
        self.Del_storage.setGeometry(QtCore.QRect(590, 290, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Del_storage.setFont(font)
        self.Del_storage.setObjectName("Del_storage")
        self.Add_storage = QtWidgets.QPushButton(NewCase)
        self.Add_storage.setGeometry(QtCore.QRect(590, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Add_storage.setFont(font)
        self.Add_storage.setObjectName("Add_storage")
        self.Add_picture = QtWidgets.QPushButton(NewCase)
        self.Add_picture.setGeometry(QtCore.QRect(590, 340, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Add_picture.setFont(font)
        self.Add_picture.setObjectName("Add_picture")
        self.Del_picture = QtWidgets.QPushButton(NewCase)
        self.Del_picture.setEnabled(False)
        self.Del_picture.setGeometry(QtCore.QRect(590, 380, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Del_picture.setFont(font)
        self.Del_picture.setObjectName("Del_picture")
        self.formLayoutWidget_5 = QtWidgets.QWidget(NewCase)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(330, 30, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.formLayoutWidget_5.setFont(font)
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_6 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_6.setContentsMargins(10, 10, 10, 10)
        self.formLayout_6.setSpacing(5)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.ID_external = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ID_external.setFont(font)
        self.ID_external.setObjectName("ID_external")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ID_external)

        self.retranslateUi(NewCase)
        self.buttonBox.accepted.connect(NewCase.accept)
        self.buttonBox.rejected.connect(NewCase.reject)
        QtCore.QMetaObject.connectSlotsByName(NewCase)
        NewCase.setTabOrder(self.Name, self.ID_external)
        NewCase.setTabOrder(self.ID_external, self.Description)
        NewCase.setTabOrder(self.Description, self.Notary_name)
        NewCase.setTabOrder(self.Notary_name, self.Notary_phone)
        NewCase.setTabOrder(self.Notary_phone, self.Notary_email)
        NewCase.setTabOrder(self.Notary_email, self.Evidences)
        NewCase.setTabOrder(self.Evidences, self.Add_device)
        NewCase.setTabOrder(self.Add_device, self.Del_device)
        NewCase.setTabOrder(self.Del_device, self.Storage_media)
        NewCase.setTabOrder(self.Storage_media, self.Add_storage)
        NewCase.setTabOrder(self.Add_storage, self.Del_storage)
        NewCase.setTabOrder(self.Del_storage, self.Add_picture)
        NewCase.setTabOrder(self.Add_picture, self.Del_picture)

    def retranslateUi(self, NewCase):
        _translate = QtCore.QCoreApplication.translate
        NewCase.setWindowTitle(_translate("NewCase", "New case"))
        self.label.setText(_translate("NewCase", "Name"))
        self.label_3.setText(_translate("NewCase", "Notary name"))
        self.label_4.setText(_translate("NewCase", "Notary phone"))
        self.label_5.setText(_translate("NewCase", "Notary email"))
        self.label_6.setText(_translate("NewCase", "Evidences"))
        self.label_7.setText(_translate("NewCase", "Evidence\n"
"storage media"))
        self.label_2.setText(_translate("NewCase", "Description"))
        self.Add_device.setText(_translate("NewCase", "+"))
        self.Del_device.setText(_translate("NewCase", "-"))
        self.Del_storage.setText(_translate("NewCase", "-"))
        self.Add_storage.setText(_translate("NewCase", "+"))
        self.Add_picture.setText(_translate("NewCase", "+"))
        self.Del_picture.setText(_translate("NewCase", "-"))
        self.label_10.setText(_translate("NewCase", "ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewCase = QtWidgets.QDialog()
    ui = Ui_NewCase()
    ui.setupUi(NewCase)
    NewCase.show()
    sys.exit(app.exec_())
