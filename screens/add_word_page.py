# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addWordPage.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_addWordPage(object):
    def setupUi(self, addWordPage):
        if not addWordPage.objectName():
            addWordPage.setObjectName(u"addWordPage")
        addWordPage.resize(1024, 634)
        addWordPage.setMinimumSize(QSize(1024, 600))
        addWordPage.setStyleSheet(u"#addWord {\n"
"	background-color: rgb(255, 208, 82);\n"
"	font-family: \"Nunito Sans\";	\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(addWordPage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.addWordMain = QWidget(addWordPage)
        self.addWordMain.setObjectName(u"addWordMain")
        self.addWordMain.setMinimumSize(QSize(600, 0))
        self.addWordMain.setStyleSheet(u"#addWordMain {\n"
"\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.addWordMain)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.addWordContainer = QWidget(self.addWordMain)
        self.addWordContainer.setObjectName(u"addWordContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addWordContainer.sizePolicy().hasHeightForWidth())
        self.addWordContainer.setSizePolicy(sizePolicy)
        self.addWordContainer.setMinimumSize(QSize(0, 0))
        self.addWordContainer.setStyleSheet(u"#addWordContainer {\n"
"	background-color: rgb(255, 247, 213);\n"
"	border-radius: 32px;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.addWordContainer)
        self.verticalLayout_2.setSpacing(24)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.addWordHeader = QFrame(self.addWordContainer)
        self.addWordHeader.setObjectName(u"addWordHeader")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.addWordHeader.sizePolicy().hasHeightForWidth())
        self.addWordHeader.setSizePolicy(sizePolicy1)
        self.addWordHeader.setStyleSheet(u"background-color: rgb(255, 170, 214);\n"
"border-top-left-radius: 32px;\n"
"border-top-right-radius: 32px;")
        self.addWordHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.addWordHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.addWordHeader)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.addWordTitle = QLabel(self.addWordHeader)
        self.addWordTitle.setObjectName(u"addWordTitle")
        font = QFont()
        font.setPointSize(36)
        font.setWeight(QFont.ExtraBold)
        self.addWordTitle.setFont(font)
        self.addWordTitle.setStyleSheet(u"background-color: rgb(43, 171, 126);\n"
"padding: 16px;\n"
"font-weight:800;")
        self.addWordTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.addWordTitle)


        self.verticalLayout_2.addWidget(self.addWordHeader, 0, Qt.AlignmentFlag.AlignTop)

        self.addWordMainContainer = QFrame(self.addWordContainer)
        self.addWordMainContainer.setObjectName(u"addWordMainContainer")
        self.addWordMainContainer.setStyleSheet(u"background-color: transparent;")
        self.addWordMainContainer.setFrameShape(QFrame.Shape.Panel)
        self.addWordMainContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.addWordMainContainer.setLineWidth(1)
        self.verticalLayout = QVBoxLayout(self.addWordMainContainer)
        self.verticalLayout.setSpacing(24)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(60, 30, 60, 60)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.addWordWordLb = QLabel(self.addWordMainContainer)
        self.addWordWordLb.setObjectName(u"addWordWordLb")
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.addWordWordLb.setFont(font1)
        self.addWordWordLb.setStyleSheet(u"color: rgb(30, 76, 91);\n"
"font-weight: 700;")

        self.verticalLayout_4.addWidget(self.addWordWordLb)

        self.addWordWordInput = QLineEdit(self.addWordMainContainer)
        self.addWordWordInput.setObjectName(u"addWordWordInput")
        sizePolicy1.setHeightForWidth(self.addWordWordInput.sizePolicy().hasHeightForWidth())
        self.addWordWordInput.setSizePolicy(sizePolicy1)
        self.addWordWordInput.setMinimumSize(QSize(0, 60))
        self.addWordWordInput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"color: #C1C1C1;\n"
"font-size: 24px;")

        self.verticalLayout_4.addWidget(self.addWordWordInput)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(self.addWordMainContainer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(30, 76, 91);\n"
"font-weight: 700;")

        self.verticalLayout_5.addWidget(self.label_3)

        self.comboBox = QComboBox(self.addWordMainContainer)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 60))
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"color: #C1C1C1;\n"
"font-size: 24px;")

        self.verticalLayout_5.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.btnCreateWord = QPushButton(self.addWordMainContainer)
        self.btnCreateWord.setObjectName(u"btnCreateWord")
        font2 = QFont()
        font2.setPointSize(24)
        self.btnCreateWord.setFont(font2)
        self.btnCreateWord.setStyleSheet(u"#btnCreateWord {\n"
"	background-color: rgb(246, 153, 42);\n"
"	padding: 20px 24px;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"#btnCreateWord:hover {\n"
"	background-color: rgb(226, 153, 42);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btnCreateWord, 0, Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.addWordMainContainer)


        self.verticalLayout_6.addWidget(self.addWordContainer)


        self.horizontalLayout_2.addWidget(self.addWordMain)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.retranslateUi(addWordPage)

        QMetaObject.connectSlotsByName(addWordPage)
    # setupUi

    def retranslateUi(self, addWordPage):
        addWordPage.setWindowTitle(QCoreApplication.translate("addWordPage", u"Form", None))
        self.addWordTitle.setText(QCoreApplication.translate("addWordPage", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u043b\u043e\u0432\u043e", None))
        self.addWordWordLb.setText(QCoreApplication.translate("addWordPage", u"\u0421\u043b\u043e\u0432\u043e:", None))
        self.label_3.setText(QCoreApplication.translate("addWordPage", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("addWordPage", u"\u0416\u0438\u0432\u043e\u0442\u043d\u044b\u0435", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("addWordPage", u"\u0422\u0440\u0430\u043d\u0441\u043f\u043e\u0440\u0442", None))

        self.btnCreateWord.setText(QCoreApplication.translate("addWordPage", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

