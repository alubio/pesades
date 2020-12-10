# -*- coding: utf-8 -*-
#
# Copyright 2021 Iván Paniagua Barrilero
#
# This file is part of PESADES.
#
# PESADES is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PESADES is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PESADES.  If not, see <https://www.gnu.org/licenses/>.

"""
PESADES main module.
"""

# Generic imports
from re import match
from time import sleep
from threading import Event

# GUI
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
#from PyQt5.QtCore import QRegExp
#from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox
_translate = QtCore.QCoreApplication.translate
from main_window_ui import *
from about_ui import *
from yes_no_dialog_ui import *
from info_dialog_ui import *
from new_operator_ui import *
from new_case_ui import *
from password_dialog_ui import *

# Logging
class Logger(QThread):
    """Logger thread"""
    update = pyqtSignal()

    def __init__(self, event):
        QThread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(1):    
            self.update.emit()

# Initial background tasks
class InitTasks(QThread):
    """Background initial tasks"""
    ended = pyqtSignal()

    def run(self):
        fsession.log("Initial tasks started")
        fsession.start()
        fsession.log("Initial tasks ended")
        self.ended.emit()

# Final background tasks
class FinalTasks(QThread):
    """Background final tasks"""
    def run(self):
        fsession.log("Final tasks started")
        fsession.end()
        fsession.log("Final tasks ended")


def criticalmessage(message, title="PESADES"):
    fsession.log("Error: "+message)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

# PESADES
from pesades_config import *
from forensic_session import *
from pesades_crypto import *
from operators_ds import *
from cases_ds import *

fsession = ForensicSession()
"""Forensic session related information"""

# 0.1.1 Initial version
# 0.1.2 License modified to GPLv3
__version__ = "0.1.2"
"""str: Major.Minor.Patch versioning"""

class AboutDlg(QDialog):
    """About dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.ui = Ui_About()
        self.ui.setupUi(self)

    def setversion(self, version):
        """Change the verion label"""
        self.ui.Version.setText(_translate("About", "Version "+version+" - GNU GPLv3 License - Copyright 2021 Iván Paniagua Barrilero"))

class NewCaseDlg(QDialog):
    """New operator dialog"""
    def __init__(self, parent=None, edit=False):
        """Initializer"""
        super().__init__(parent)
        self.ui = Ui_NewCase()
        self.ui.setupUi(self)
        self.ui.Name.setFocus()
        self.edit = edit
        if edit:
            # Case editing
            self.old_name = fsession.case
            case = get_casebyname(self.old_name)
            self.ui.Name.setText(case.name)
            self.ui.ID_external.setText(str(case.id_external))
            self.ui.Description.setText(str(case.description))
            self.ui.Notary_name.setText(str(case.notary_name))
            self.ui.Notary_phone.setText(str(case.notary_phone))
            self.ui.Notary_email.setText(str(case.notary_email))

    def accept(self):
        # Validate name
        if len(self.ui.Name.text()) < 11:
            criticalmessage("Invalid name, please use more than ten characters", "Validation error")
            self.ui.Name.setFocus()
            return
        if self.ui.Name.text() == "testnotuse":
            criticalmessage("Invalid username, please use another one", "Validation error")
            self.ui.Name.setFocus()
            return
        # Validate external ID
        if len(self.ui.ID_external.text()) < 3:
            criticalmessage("Invalid external ID, please use more than two characters", "Validation error")
            self.ui.ID_external.setFocus()
            return
        # Validate description
        if len(self.ui.Description.toPlainText()) < 11:
            criticalmessage("Invalid description, please use more than ten characters", "Validation error")
            self.ui.Description.setFocus()
            return
        # Validate notary name
        if len(self.ui.Notary_name.text()) < 7:
            criticalmessage("Invalid notary name, please use more than six characters", "Validation error")
            self.ui.Notary_name.setFocus()
            return
        # Validate notary phone
        if not match(r"\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$", self.ui.Notary_phone.text()):
            criticalmessage("Invalid notary phone, please use international format (e.g. +34918808888)", "Validation error")
            self.ui.Notary_phone.setFocus()
            return
        # Validate email
        if not match(r"[^@]+@[^@]+\.[^@]+", self.ui.Notary_email.text()):
            criticalmessage("Invalid notary email, please correct it", "Validation error")
            self.ui.Notary_email.setFocus()
            return

        # Validation OK

        if self.edit:
            # Edit case
            result = update_case(self.old_name, self.ui.Name.text(), self.ui.ID_external.text(), self.ui.Description.toPlainText(), self.ui.Notary_name.text(), self.ui.Notary_phone.text(), self.ui.Notary_email.text())
            if result == "OK":
                super().accept()
            else:
                criticalmessage(result, "Validation error")
        else:
            # Store new case
            result = store_case(self.ui.Name.text(), self.ui.ID_external.text(), self.ui.Description.toPlainText(), self.ui.Notary_name.text(), self.ui.Notary_phone.text(), self.ui.Notary_email.text())
            if result == "OK":
                fsession.set_case(self.ui.Name.text())
                super().accept()
            else:
                criticalmessage(result, "Validation error")

class NewOperatorDlg(QDialog):
    """New operator dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.ui = Ui_NewOperator()
        self.ui.setupUi(self)
        self.ui.Username.setFocus()
        
    def accept(self):
        from re import match
        # Validate username
        if len(self.ui.Username.text()) < 4:
            criticalmessage("Invalid username, please use more than three characters", "Validation error")
            self.ui.Username.setFocus()
            return
        if self.ui.Username.text() == "testnotuse" or self.ui.Username.text() == "admin":
            criticalmessage("Invalid username, please use another one", "Validation error")
            self.ui.Username.setFocus()
            return
        # Validate fullname
        if len(self.ui.Fullname.text()) < 7:
            criticalmessage("Invalid full name, please use more than six characters", "Validation error")
            self.ui.Fullname.setFocus()
            return
        # Validate organization
        if len(self.ui.Organization.text()) < 4:
            criticalmessage("Invalid organization, please use more than three characters", "Validation error")
            self.ui.Organization.setFocus()
            return
        # Validate phone
        if not match(r"\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$", self.ui.Phone.text()):
            criticalmessage("Invalid phone, please use international format (e.g. +34918808888)", "Validation error")
            self.ui.Phone.setFocus()
            return
        # Validate email
        if not match(r"[^@]+@[^@]+\.[^@]+", self.ui.Email.text()):
            criticalmessage("Invalid email, please correct it", "Validation error")
            self.ui.Email.setFocus()
            return
        # Validate passwords
        if self.ui.Password1.text() != self.ui.Password2.text():
            criticalmessage("Passwords do not match", "Validation error")
            self.ui.Password1.setFocus()
            return
        # TODO Change by isweakpassword
        if is_weakpassword_dummy(self.ui.Password1.text()):
            criticalmessage("Weak password. Please use more than ten characters. Include lowercase and uppercase alphabetic characters, numbers and symbols (-_@$.,*#)", "Validation error")
            self.ui.Password1.setFocus()
            return

        # Validation OK
        # Store new operator
        result = store_operator(self.ui.Username.text(), self.ui.Fullname.text(), self.ui.Organization.text(), self.ui.Phone.text(), self.ui.Email.text(), get_hashedpassword(self.ui.Password1.text()))
        if result == "OK":
            fsession.log("Operator "+self.ui.Username.text()+" created")
            fsession.operator = self.ui.Username.text()
            super().accept()
        else:
            criticalmessage(result, "Validation error")

class PasswordDlg(QDialog):
    """New password dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.ui = Ui_PasswordDialog()
        self.ui.setupUi(self)
        self.ui.Password.setFocus()

    def get_password(self):
        """Return hashed typed password"""
        return self.ui.Password.text()

    def set_info(self, info):
        """Change info label"""
        self.ui.Info.setText(_translate("PasswordDialog", info))
        self.ui.Password.setText("")

class YesNoDlg(QDialog):
    """Yes No dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.ui = Ui_YesNoDialog()
        self.ui.setupUi(self)

    def setinfoquestion(self, info, question):
        """Change the info and question labels"""
        self.ui.Info.setText(_translate("YesNoDialog", info))
        self.ui.Question.setText(_translate("YesNoDialog", question))

class InfoDlg(QDialog):
    """Info dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.ui = Ui_InfoDialog()
        self.ui.setupUi(self)

    def setinfo(self, info):
        """Change the info label"""
        fsession.log("Info: "+info)
        self.ui.Info.setText(_translate("InfoDialog", info))

class MainWindowDlg(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main window of the user interface"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.forensicsesion = ForensicSession()
        """Forensic session"""

        # Logging
        self.stop_flag = Event()
        self.lastlogitem = 0
        self.logger = Logger(self.stop_flag)
        self.logger.update.connect(self.updateLog)
        self.logger.start()

        # Status bar
        self.statusBar = QtWidgets.QStatusBar()
        self.statusBar.setStyleSheet('QStatusBar::item {border: None;}')
        self.setStatusBar(self.statusBar)
        self.statuslabel = QtWidgets.QLabel()
        self.statuslabel.setAlignment(QtCore.Qt.AlignLeft)
        self.clocklabel = QtWidgets.QLabel()
        self.clocklabel.setAlignment(QtCore.Qt.AlignRight)
        self.qwstatusbar = QtWidgets.QWidget()
        self.qwstatusbar.setLayout(QtWidgets.QHBoxLayout())
        self.qwstatusbar.layout().addWidget(self.statuslabel)
        self.qwstatusbar.layout().addWidget(self.clocklabel)
        self.statusBar.addPermanentWidget(self.qwstatusbar, 2)
        self.updateClock()
        self.clocktimer = QtCore.QTimer(self)
        self.clocktimer.setInterval(1000)
        self.clocktimer.timeout.connect(self.updateClock)
        self.clocktimer.start()

        #  Initial background tasks
        self.inittasks = InitTasks()
        self.inittasks.ended.connect(self.initTasksEnded)
        self.inittasks.start()

        # Init generic dialogs
        self.yesnodlg = YesNoDlg(self)
        self.infodlg = InfoDlg(self)
        self.passworddlg = PasswordDlg(self)

        # Connectors
        self.actionAbout.triggered.connect(self.onHelpAbout)
        self.Exit.clicked.connect(self.onExit)
        self.Op_new.clicked.connect(self.onNewOperator)
        self.Op_username.textEdited.connect(self.onOpEdited)
        self.Op_username.returnPressed.connect(self.onOpAuth)
        self.Op_username.setFocus()
        self.Op_auth.clicked.connect(self.onOpAuth)
        self.Case_new.clicked.connect(self.onNewCase)
        self.Case_select.currentTextChanged.connect(self.onCaseChange)

    def initTasksEnded(self):
        # Init controls
        self.Case_select.addItem("")
        for casename in get_listcasenames():
            self.Case_select.addItem(casename)

    def updateClock(self):
        self.clocklabel.setText(QtCore.QDateTime.currentDateTime().toString("HH:mm:ss"))

    def updateLog(self):
        if self.lastlogitem < len(fsession.sessionlog):
            for m in fsession.sessionlog[self.lastlogitem:]:
                self.lastlogitem += 1
                self.Log.addItem(m)
                self.Log.scrollToBottom()

    def onHelpAbout(self):
        """Launch the about dialog"""
        dlg = AboutDlg(self)
        dlg.setversion(__version__)
        dlg.exec()

    def onExit(self):
        """Exit"""
        self.yesnodlg.setinfoquestion("Nothing done", "Do you really want to exit?")
        result = self.yesnodlg.exec()
        if result:
            fsession.log("Session closed")
            #  Initial background tasks
            finaltasks = FinalTasks()
            finaltasks.start()
            finaltasks.wait()
            self.close()

    def onNewOperator(self):
        """Launch new operator dialog"""
        fsession.log("Trying to create a new operator")
        dlg = NewOperatorDlg(self)
        if dlg.exec():
            # New operator created
            self.Case.setEnabled(True)
            self.Op_new.setEnabled(False)
            self.Op_username.setEnabled(False)
            self.Op_username.setText(dlg.getusername())
            self.Op_auth.setText("Close")
            self.Op_auth.setEnabled(True)
            fsession.log("New operator created and logged")
        else:
            fsession.log("New operator creation aborted")

    def onNewCase(self):
        """Launch new case dialog"""
        if self.Case_new.text() == "New case":
            fsession.log("Trying to create a new case")
            dlg = NewCaseDlg(self, False)
            if dlg.exec():
                # New case created
                self.Discovery.setEnabled(True)
                fsession.log("New case created")
                # Update cases list
                self.Case_select.clear()
                self.Case_select.addItem("")
                for casename in get_listcasenames():
                    self.Case_select.addItem(casename)
            else:
                fsession.log("New case creation aborted")
        else:
            fsession.log("Trying to update "+self.Case_select.currentText()+" case")
            dlg = NewCaseDlg(self, True)
            if dlg.exec():
                # New case created
                self.Discovery.setEnabled(True)
                fsession.log("Case updated")
                # Update cases list
                self.Case_select.clear()
                self.Case_select.addItem("")
                for casename in get_listcasenames():
                    self.Case_select.addItem(casename)
            else:
                fsession.log("Case editing aborted")
        
    def onCaseChange(self, casename):
        """Case changed"""
        if casename != "":
            fsession.set_case(casename)
            self.Discovery.setEnabled(True)
            self.Case_new.setText("Edit case")
        else:
            fsession.set_case(None)
            self.Discovery.setEnabled(False)
            self.Case_new.setText("New case")

    def onOpEdited(self):
        """Operator edited, enable authentication"""
        self.Op_auth.setEnabled(True)

    def onOpAuth(self):
        global fsession
        """Authenticate/Close operator"""
        if not fsession.operator:
            self.passworddlg.set_info(self.Op_username.text()+" password:")
            self.passworddlg.exec()
            if check_userpassword(self.Op_username.text(), self.passworddlg.get_password()):
                self.Case.setEnabled(True)
                self.Op_new.setEnabled(False)
                self.Op_username.setEnabled(False)
                self.Op_auth.setText("Close")
                self.Op_auth.setEnabled(True)
                fsession.operator = self.Op_username.text()
                fsession.log("Operator "+self.Op_username.text()+" login")
            else:
                fsession.log("Operator "+self.Op_username.text()+" failed login")
                criticalmessage("Wrong password", "Validation error")
        else:
            fsession.operator = None
            self.Op_new.setEnabled(True)
            self.Op_username.setEnabled(True)
            self.Op_username.setText("")
            self.Op_username.setFocus()
            self.Op_auth.setText("Init")
            self.Op_auth.setEnabled(False)
            fsession.log("Closed operator's session")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindowDlg()
    window.show()
    app.exec_()
