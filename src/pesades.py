# -*- coding: utf-8 -*-
"""
PESADES main module.
"""
# Logging
from logging import basicConfig, debug, warning, error, DEBUG, WARNING
from PyQt5.QtCore import QRunnable, pyqtSlot, QThreadPool
from time import sleep
import datetime
class Logger(QRunnable):
    """Logger thread"""

    def __init__(self, logdlg):
        """Initializer"""
        super(Logger, self).__init__()
        self.logdlg = logdlg
        self.lastlogitem = 0

    @pyqtSlot()
    def run(self):
        """Logger activities"""
        while True:
            if self.lastlogitem < len(fsession.sessionlog):
                for m in fsession.sessionlog[self.lastlogitem:]:
                    self.lastlogitem += 1
                    self.logdlg.addItem(str(datetime.datetime.now())+": "+m)
            sleep(1)

# GUI
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
from password_dialog_ui import *

def criticalmessage(message, title="PESADES"):
    fsession.log("Error: "+message)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText(message)
    msg.setWindowTitle(title)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

# PESADES
from forensic_session import *
from pesades_crypto import *
from operators_ds import *

fsession = ForensicSession()
fsession.log("Session created")
"""Forensic session related information"""
__version__ = "0.1.1"
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
        self.ui.Version.setText(_translate("About", "Version "+version))

class NewOperatorDlg(QDialog):
    """New operator dialog"""
    def __init__(self, parent=None):
        """Initializer"""
        super().__init__(parent)
        self.ui = Ui_NewOperator()
        self.ui.setupUi(self)
        self.ui.Username.setFocus()
        
    def getusername(self):
        """Get username"""
        return self.ui.Username.text()

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
        flag = 0
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

        self.threadpool = QThreadPool()
        """Threading engine"""

        self.forensicsesion = ForensicSession()
        """Forensic session"""

        # Logging
        self.logger = Logger(self.Log)
        self.threadpool.start(self.logger)

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

    def onHelpAbout(self):
        """Launch the about dialog"""
        dlg = AboutDlg(self)
        dlg.setversion(__version__)
        dlg.exec()

    def onExit(self):
        """Exit"""
        self.yesnodlg.setinfoquestion("No ha hecho nada", "Do you really want to exit?")
        result = self.yesnodlg.exec()
        if result:
            fsession.log("Session closed")
            self.close()

    def onNewOperator(self):
        """Launch new operator dialog"""
        fsession.log("Trying to create a new operator")
        dlg = NewOperatorDlg(self)
        if dlg.exec():
            # New operator created
            self.Discovery.setEnabled(True)
            self.Op_new.setEnabled(False)
            self.Op_username.setEnabled(False)
            self.Op_username.setText(dlg.getusername())
            self.Op_auth.setText("Close")
            self.Op_auth.setEnabled(True)
            fsession.operator = dlg.getusername()
            fsession.log("New operator created")
        else:
            fsession.log("New operator creation aborted")

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
                self.Discovery.setEnabled(True)
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
            fsession.log("Closed operator session")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindowDlg()
    window.show()
    app.exec_()