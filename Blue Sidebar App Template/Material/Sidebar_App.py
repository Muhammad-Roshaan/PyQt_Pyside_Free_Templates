# Form implementation generated from reading ui file 'Sidebar_App.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1338, 856)
        MainWindow.setStyleSheet("background-color: rgb(245, 250, 254);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Icon_Widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.Icon_Widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(31, 156, 233);\n"
"}\n"
"QPushButton{\n"
"    color:white;\n"
"    height:50px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:Checked{\n"
"    background-color:#f5fafe;\n"
"    color:#1f95ef;\n"
"    font-weight:bold;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"\n"
"")
        self.Icon_Widget.setObjectName("Icon_Widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Icon_Widget)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.Icon_Widget)
        self.label.setMinimumSize(QtCore.QSize(50, 60))
        self.label.setMaximumSize(QtCore.QSize(65, 80))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/profile 2white.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(13)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Dashboard_S = QtWidgets.QPushButton(parent=self.Icon_Widget)
        self.Dashboard_S.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/dashboard white.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(":/images/dashboard Blue.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.Dashboard_S.setIcon(icon)
        self.Dashboard_S.setCheckable(True)
        self.Dashboard_S.setAutoExclusive(True)
        self.Dashboard_S.setObjectName("Dashboard_S")
        self.verticalLayout_2.addWidget(self.Dashboard_S)
        self.Profile_S = QtWidgets.QPushButton(parent=self.Icon_Widget)
        self.Profile_S.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/user (white).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap(":/images/user (blue).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.Profile_S.setIcon(icon1)
        self.Profile_S.setCheckable(True)
        self.Profile_S.setAutoExclusive(True)
        self.Profile_S.setObjectName("Profile_S")
        self.verticalLayout_2.addWidget(self.Profile_S)
        self.Messages_S = QtWidgets.QPushButton(parent=self.Icon_Widget)
        self.Messages_S.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/comments white.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap(":/images/comments.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.Messages_S.setIcon(icon2)
        self.Messages_S.setCheckable(True)
        self.Messages_S.setAutoExclusive(True)
        self.Messages_S.setObjectName("Messages_S")
        self.verticalLayout_2.addWidget(self.Messages_S)
        self.Notifications_S = QtWidgets.QPushButton(parent=self.Icon_Widget)
        self.Notifications_S.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/Notification white.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap(":/images/Notification Blue.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.Notifications_S.setIcon(icon3)
        self.Notifications_S.setCheckable(True)
        self.Notifications_S.setAutoExclusive(True)
        self.Notifications_S.setObjectName("Notifications_S")
        self.verticalLayout_2.addWidget(self.Notifications_S)
        self.Settings_S = QtWidgets.QPushButton(parent=self.Icon_Widget)
        self.Settings_S.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/Setting white.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon4.addPixmap(QtGui.QPixmap(":/images/Setting Blue.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.Settings_S.setIcon(icon4)
        self.Settings_S.setCheckable(True)
        self.Settings_S.setAutoExclusive(True)
        self.Settings_S.setObjectName("Settings_S")
        self.verticalLayout_2.addWidget(self.Settings_S)
        spacerItem = QtWidgets.QSpacerItem(20, 548, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.SignOut_S = QtWidgets.QPushButton(parent=self.Icon_Widget)
        self.SignOut_S.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/power white.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.SignOut_S.setIcon(icon5)
        self.SignOut_S.setCheckable(True)
        self.SignOut_S.setObjectName("SignOut_S")
        self.verticalLayout_2.addWidget(self.SignOut_S)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.Icon_Widget, 0, 0, 1, 1)
        self.Icon_Name_Widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.Icon_Name_Widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(31, 156, 233);\n"
"}\n"
"QPushButton{\n"
"    color:white;\n"
"    text-align:left;\n"
"    height:30px;\n"
"    border:None;\n"
"    padding:8px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:Checked{\n"
"    background-color:#f5fafe;\n"
"    color:#1f95ef;\n"
"    font-weight:bold;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.Icon_Name_Widget.setObjectName("Icon_Name_Widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Icon_Name_Widget)
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.Icon_Name_Widget)
        self.label_2.setMinimumSize(QtCore.QSize(75, 75))
        self.label_2.setMaximumSize(QtCore.QSize(75, 75))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/profile 2white.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.Icon_Name_Widget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold Condensed")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:White")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Dashboard_B = QtWidgets.QPushButton(parent=self.Icon_Name_Widget)
        self.Dashboard_B.setIcon(icon)
        self.Dashboard_B.setCheckable(True)
        self.Dashboard_B.setAutoExclusive(True)
        self.Dashboard_B.setObjectName("Dashboard_B")
        self.verticalLayout.addWidget(self.Dashboard_B)
        self.Profile_B = QtWidgets.QPushButton(parent=self.Icon_Name_Widget)
        self.Profile_B.setIcon(icon1)
        self.Profile_B.setCheckable(True)
        self.Profile_B.setAutoExclusive(True)
        self.Profile_B.setObjectName("Profile_B")
        self.verticalLayout.addWidget(self.Profile_B)
        self.Messages_B = QtWidgets.QPushButton(parent=self.Icon_Name_Widget)
        self.Messages_B.setIcon(icon2)
        self.Messages_B.setCheckable(True)
        self.Messages_B.setAutoExclusive(True)
        self.Messages_B.setObjectName("Messages_B")
        self.verticalLayout.addWidget(self.Messages_B)
        self.Notifications_B = QtWidgets.QPushButton(parent=self.Icon_Name_Widget)
        self.Notifications_B.setIcon(icon3)
        self.Notifications_B.setCheckable(True)
        self.Notifications_B.setAutoExclusive(True)
        self.Notifications_B.setObjectName("Notifications_B")
        self.verticalLayout.addWidget(self.Notifications_B)
        self.Settings_B = QtWidgets.QPushButton(parent=self.Icon_Name_Widget)
        self.Settings_B.setIcon(icon4)
        self.Settings_B.setCheckable(True)
        self.Settings_B.setAutoExclusive(True)
        self.Settings_B.setObjectName("Settings_B")
        self.verticalLayout.addWidget(self.Settings_B)
        spacerItem1 = QtWidgets.QSpacerItem(20, 548, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.SignOut_B = QtWidgets.QPushButton(parent=self.Icon_Name_Widget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/power white.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon6.addPixmap(QtGui.QPixmap(":/images/power blue.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.SignOut_B.setIcon(icon6)
        self.SignOut_B.setCheckable(True)
        self.SignOut_B.setObjectName("SignOut_B")
        self.verticalLayout.addWidget(self.SignOut_B)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addWidget(self.Icon_Name_Widget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Header = QtWidgets.QWidget(parent=self.widget_3)
        self.Header.setObjectName("Header")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Menu = QtWidgets.QPushButton(parent=self.Header)
        self.Menu.setStyleSheet("border:none;")
        self.Menu.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/menu-bar blue.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Menu.setIcon(icon7)
        self.Menu.setIconSize(QtCore.QSize(30, 30))
        self.Menu.setCheckable(True)
        self.Menu.setObjectName("Menu")
        self.horizontalLayout_2.addWidget(self.Menu)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.Header)
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Search = QtWidgets.QPushButton(parent=self.Header)
        self.Search.setStyleSheet("border:none;")
        self.Search.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/Search Icon Blue.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Search.setIcon(icon8)
        self.Search.setIconSize(QtCore.QSize(100, 20))
        self.Search.setObjectName("Search")
        self.horizontalLayout.addWidget(self.Search)
        self.Profile = QtWidgets.QPushButton(parent=self.Header)
        self.Profile.setStyleSheet("border:none;")
        self.Profile.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/user (blue).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Profile.setIcon(icon9)
        self.Profile.setIconSize(QtCore.QSize(30, 20))
        self.Profile.setObjectName("Profile")
        self.horizontalLayout.addWidget(self.Profile)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.Header)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget_3)
        self.stackedWidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Dashboard_Page = QtWidgets.QWidget()
        self.Dashboard_Page.setStyleSheet("")
        self.Dashboard_Page.setObjectName("Dashboard_Page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Dashboard_Page)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.Dashboard_Page)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.stackedWidget.addWidget(self.Dashboard_Page)
        self.Profile_Page = QtWidgets.QWidget()
        self.Profile_Page.setObjectName("Profile_Page")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.Profile_Page)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(parent=self.Profile_Page)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.stackedWidget.addWidget(self.Profile_Page)
        self.Messages_Page = QtWidgets.QWidget()
        self.Messages_Page.setObjectName("Messages_Page")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.Messages_Page)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(parent=self.Messages_Page)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.stackedWidget.addWidget(self.Messages_Page)
        self.Notifications_Page = QtWidgets.QWidget()
        self.Notifications_Page.setObjectName("Notifications_Page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Notifications_Page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(parent=self.Notifications_Page)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.stackedWidget.addWidget(self.Notifications_Page)
        self.Settings_Page = QtWidgets.QWidget()
        self.Settings_Page.setObjectName("Settings_Page")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Settings_Page)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(parent=self.Settings_Page)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.567, y2:0.590545, stop:0 rgba(31, 156, 233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.stackedWidget.addWidget(self.Settings_Page)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.Menu.toggled['bool'].connect(self.Icon_Widget.setHidden) # type: ignore
        self.Menu.toggled['bool'].connect(self.Icon_Name_Widget.setVisible) # type: ignore
        self.Settings_S.toggled['bool'].connect(self.Settings_B.setChecked) # type: ignore
        self.Notifications_S.toggled['bool'].connect(self.Notifications_B.setChecked) # type: ignore
        self.Messages_S.toggled['bool'].connect(self.Messages_B.setChecked) # type: ignore
        self.Profile_S.toggled['bool'].connect(self.Profile_B.setChecked) # type: ignore
        self.Dashboard_S.toggled['bool'].connect(self.Dashboard_B.setChecked) # type: ignore
        self.SignOut_S.toggled['bool'].connect(self.SignOut_B.setChecked) # type: ignore
        self.Dashboard_B.toggled['bool'].connect(self.Dashboard_S.setChecked) # type: ignore
        self.Profile_B.toggled['bool'].connect(self.Profile_S.setChecked) # type: ignore
        self.Messages_B.toggled['bool'].connect(self.Messages_S.setChecked) # type: ignore
        self.Notifications_B.toggled['bool'].connect(self.Notifications_S.setChecked) # type: ignore
        self.Settings_B.toggled['bool'].connect(self.Settings_S.setChecked) # type: ignore
        self.SignOut_B.toggled['bool'].connect(self.SignOut_S.setChecked) # type: ignore
        self.SignOut_B.toggled['bool'].connect(MainWindow.close) # type: ignore
        self.SignOut_S.toggled['bool'].connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Side Bar"))
        self.Dashboard_B.setText(_translate("MainWindow", "Dashboard"))
        self.Profile_B.setText(_translate("MainWindow", "Profile"))
        self.Messages_B.setText(_translate("MainWindow", "Messages"))
        self.Notifications_B.setText(_translate("MainWindow", "Notifications"))
        self.Settings_B.setText(_translate("MainWindow", "Settings"))
        self.SignOut_B.setText(_translate("MainWindow", "SignOut"))
        self.label_4.setText(_translate("MainWindow", "Dashboard"))
        self.label_5.setText(_translate("MainWindow", "Profile"))
        self.label_6.setText(_translate("MainWindow", "Messages"))
        self.label_7.setText(_translate("MainWindow", "Notifications"))
        self.label_8.setText(_translate("MainWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())