from PyQt5 import QtCore, QtGui, QtWidgets
import os
import hashlib
from dotenv import load_dotenv

load_dotenv()


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1187, 843)
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "    background: white;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
                                         "    background: white;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(250, 200))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.login_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.login_page)
        self.widget.setMinimumSize(QtCore.QSize(250, 200))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.email_line = QtWidgets.QLineEdit(self.widget)
        self.email_line.setMaximumSize(QtCore.QSize(250, 35))
        self.email_line.setStyleSheet("QLineEdit{\n"
                                      "    font: 10pt \"MS Shell Dlg 2\";\n"
                                      "    color: rgba(60, 70, 190, 0.8);\n"
                                      "    outline: none;\n"
                                      "    border: none;\n"
                                      "    border-bottom: 1px solid rgb(192,192,168);\n"
                                      "    background-color:  rgba(192,192,168,0.2);\n"
                                      "    padding-bottom: 3;\n"
                                      "    border-radius: 2\n"
                                      "}\n"
                                      "")
        self.email_line.setText("")
        self.email_line.setObjectName("email_line")
        self.verticalLayout_3.addWidget(self.email_line)
        self.email_line.setPlaceholderText('Email')
        self.password_line = QtWidgets.QLineEdit(self.widget)
        self.password_line.setMaximumSize(QtCore.QSize(250, 35))
        self.password_line.setStyleSheet("QLineEdit{\n"
                                         "    font: 10pt \"MS Shell Dlg 2\";\n"
                                         "    color: rgba(60, 70, 190, 0.8);\n"
                                         "    outline: none;\n"
                                         "    border: none;\n"
                                         "    border-bottom: 1px solid rgb(192,192,168);\n"
                                         "    background-color:  rgba(192,192,168,0.2);\n"
                                         "    padding-bottom: 3;\n"
                                         "    border-radius: 2\n"
                                         "}\n"
                                         "")
        self.password_line.setText("")
        self.password_line.setObjectName("password_line")
        self.password_line.setObjectName("password")
        self.password_line.setEchoMode(self.password_line.Password)
        self.password_line.setPlaceholderText('Password')
        self.verticalLayout_3.addWidget(self.password_line)
        self.message_label = QtWidgets.QLabel(self.widget)
        self.message_label.setMaximumSize(QtCore.QSize(250, 35))
        self.message_label.setStyleSheet("QLabel{font: 10pt \"Rockwell\";\n"
                                         "    color: rgb(190,40,21)\n"
                                         "}")
        self.message_label.setObjectName("message_label")
        self.verticalLayout_3.addWidget(self.message_label)
        self.LogInButton = QtWidgets.QPushButton(self.widget)
        self.LogInButton.setMinimumSize(QtCore.QSize(150, 35))
        self.LogInButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.LogInButton.setStyleSheet("QPushButton{\n"
                                       "    font: 10pt \"Rockwell\";\n"
                                       "    color: #fff;\n"
                                       "    border: none;\n"
                                       "    border-radius: 6;\n"
                                       "    background: rgba(60, 70, 190, 0.8);\n"
                                       "    cursor: pointer;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "    oppacity: 0.7;\n"
                                       "}")
        self.LogInButton.setObjectName("LogInButton")
        self.LogInButton.clicked.connect(self.authorization)
        self.verticalLayout_3.addWidget(self.LogInButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.login_page)
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.home_page)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.home_page)
        self.label.setMinimumSize(QtCore.QSize(200, 200))
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("media/spongebob.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.home_page)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1187, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.message_label.setText(_translate("MainWindow", ""))
        self.LogInButton.setText(_translate("MainWindow", "Log In"))

    def authorization(self):
        entered_email = self.email_line.text()
        entered_password = hashlib.sha256(self.password_line.text().encode('utf-8')).hexdigest()
        if entered_email == '' or self.password_line.text() == '':
            self.message_label.setText("Enter All Fields")
        elif entered_email == os.getenv("EMAIL1") and entered_password == os.getenv("PASSWORD1") \
                or entered_email == os.getenv("EMAIL2") and entered_password == os.getenv("PASSWORD2"):
            self.stackedWidget.setCurrentIndex(1)
        elif entered_email == os.getenv("EMAIL1") and entered_password != os.getenv("PASSWORD1"):
            self.message_label.setText("Incorrect Password")
        elif entered_email == os.getenv("EMAIL2") and entered_password != os.getenv("PASSWORD2"):
            self.message_label.setText("Incorrect Password")
        else:
            self.message_label.setText("The Email Does Not Exist")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
