# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainPage.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)


class Ui_mainPage(object):
    def setupUi(self, mainPage):
        if not mainPage.objectName():
            mainPage.setObjectName(u"mainPage")
        mainPage.resize(1024, 560)
        mainPage.setMinimumSize(QSize(1024, 560))
        mainPage.setStyleSheet(u"#mainPage {\n"
"	font-family: \"Nunito Sans Normal\";\n"
"	background-color: #FFC13A;\n"
"}")
        self.verticalLayout = QVBoxLayout(mainPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainHeader = QFrame(mainPage)
        self.mainHeader.setObjectName(u"mainHeader")
        self.mainHeader.setStyleSheet(u"#mainHeader{\n"
"	background-color: #2BAD80;\n"
"}")
        self.mainHeader.setFrameShape(QFrame.StyledPanel)
        self.mainHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.mainHeader)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainTitle = QLabel(self.mainHeader)
        self.mainTitle.setObjectName(u"mainTitle")
        self.mainTitle.setStyleSheet(u"#mainTitle {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 68px;\n"
"	font-weight: 600;\n"
"	color: #FEF5D6;\n"
"}")
        self.mainTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.mainTitle)


        self.verticalLayout.addWidget(self.mainHeader)

        self.mainContainer = QFrame(mainPage)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy)
        self.mainContainer.setStyleSheet(u"#mainContainer {\n"
"	background-color: #FFC13A;\n"
"}")
        self.mainContainer.setFrameShape(QFrame.StyledPanel)
        self.mainContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mainContainer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 32, -1, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.mainButtons = QWidget(self.mainContainer)
        self.mainButtons.setObjectName(u"mainButtons")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainButtons.sizePolicy().hasHeightForWidth())
        self.mainButtons.setSizePolicy(sizePolicy1)
        self.mainButtons.setMinimumSize(QSize(400, 0))
        self.mainButtons.setMaximumSize(QSize(16777215, 16777215))
        self.mainButtons.setStyleSheet(u"QPushButton {\n"
"	font-family: \"NunitoSans\";\n"
"	background-color: #2BAD80;\n"
"	padding: 16px 40px;\n"
"	border-radius: 12px;\n"
"	font-size: 32px;\n"
"	font-weight: 600;\n"
"	color: #EDEBD6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(47, 193, 142);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(39, 158, 116);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.mainButtons)
        self.verticalLayout_2.setSpacing(32)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, -1, 12, -1)
        self.btnStart = QPushButton(self.mainButtons)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setAutoFillBackground(False)
        self.btnStart.setText(u" \u041d\u0430\u0447\u0430\u0442\u044c \u0438\u0433\u0440\u0443")
        icon = QIcon()
        icon.addFile(u":/icons/play_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnStart.setIcon(icon)
        self.btnStart.setIconSize(QSize(32, 32))
        self.btnStart.setCheckable(False)
        self.btnStart.setAutoRepeat(False)
        self.btnStart.setAutoExclusive(False)
        self.btnStart.setFlat(False)

        self.verticalLayout_2.addWidget(self.btnStart)

        self.btnMainCategory = QPushButton(self.mainButtons)
        self.btnMainCategory.setObjectName(u"btnMainCategory")
        icon1 = QIcon()
        icon1.addFile(u":/icons/book_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMainCategory.setIcon(icon1)
        self.btnMainCategory.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btnMainCategory)

        self.btnTops = QPushButton(self.mainButtons)
        self.btnTops.setObjectName(u"btnTops")
        icon2 = QIcon()
        icon2.addFile(u":/icons/trophy_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnTops.setIcon(icon2)
        self.btnTops.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.btnTops)

        self.btnMainExit = QPushButton(self.mainButtons)
        self.btnMainExit.setObjectName(u"btnMainExit")
        icon3 = QIcon()
        icon3.addFile(u":/icons/close_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnMainExit.setIcon(icon3)
        self.btnMainExit.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.btnMainExit)


        self.horizontalLayout_2.addWidget(self.mainButtons, 0, Qt.AlignTop)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.mainContainer)


        self.retranslateUi(mainPage)

        self.btnStart.setDefault(False)


        QMetaObject.connectSlotsByName(mainPage)
    # setupUi

    def retranslateUi(self, mainPage):
        mainPage.setWindowTitle(QCoreApplication.translate("mainPage", u"Form", None))
        self.mainTitle.setText(QCoreApplication.translate("mainPage", u"\u0423\u0433\u0430\u0434\u0430\u0439 \u0441\u043b\u043e\u0432\u043e", None))
        self.btnMainCategory.setText(QCoreApplication.translate("mainPage", u" \u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.btnTops.setText(QCoreApplication.translate("mainPage", u" \u0420\u0435\u043a\u043e\u0440\u0434\u044b", None))
        self.btnMainExit.setText(QCoreApplication.translate("mainPage", u"\u0412\u044b\u0439\u0442\u0438", None))
#if QT_CONFIG(shortcut)
        self.btnMainExit.setShortcut(QCoreApplication.translate("mainPage", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

