# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resultPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_resultPage(object):
    def setupUi(self, resultPage):
        if not resultPage.objectName():
            resultPage.setObjectName(u"resultPage")
        resultPage.resize(1025, 600)
        resultPage.setMinimumSize(QSize(1024, 600))
        resultPage.setStyleSheet(u"#resultPage {\n"
"	background-color: rgb(255, 208, 82);\n"
"}")
        self.horizontalLayout = QHBoxLayout(resultPage)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.resultWidget = QWidget(resultPage)
        self.resultWidget.setObjectName(u"resultWidget")
        self.resultWidget.setStyleSheet(u"#resultWidget {\n"
"	background-color: rgb(255, 208, 82);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.resultWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.resultMain = QWidget(self.resultWidget)
        self.resultMain.setObjectName(u"resultMain")
        self.resultMain.setMinimumSize(QSize(500, 0))
        self.resultMain.setMaximumSize(QSize(16777215, 16777215))
        self.resultMain.setStyleSheet(u"#resultMain {\n"
"	border-radius: 32px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.resultMain)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.resultHeader = QFrame(self.resultMain)
        self.resultHeader.setObjectName(u"resultHeader")
        self.resultHeader.setStyleSheet(u"#resultHeader {\n"
"	border-top-left-radius: 32px;\n"
"	border-top-right-radius: 32px;\n"
"\n"
"	background-color: rgb(43, 171, 126);\n"
"}")
        self.resultHeader.setFrameShape(QFrame.Shape.StyledPanel)
        self.resultHeader.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.resultHeader)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.resultTitle = QLabel(self.resultHeader)
        self.resultTitle.setObjectName(u"resultTitle")
        self.resultTitle.setStyleSheet(u"#resultTitle {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 32px ;\n"
"	padding: 16px;\n"
"	font-weight: 600;\n"
"}")
        self.resultTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.resultTitle)


        self.verticalLayout.addWidget(self.resultHeader, 0, Qt.AlignmentFlag.AlignTop)

        self.resultContent = QFrame(self.resultMain)
        self.resultContent.setObjectName(u"resultContent")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultContent.sizePolicy().hasHeightForWidth())
        self.resultContent.setSizePolicy(sizePolicy)
        self.resultContent.setStyleSheet(u"#resultContent {\n"
"	border-bottom-left-radius: 32px;\n"
"	border-bottom-right-radius: 32px;\n"
"\n"
"	background-color: rgb(235, 244, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #1C1C1C;\n"
"}")
        self.resultContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.resultContent.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.resultContent)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setContentsMargins(-1, -1, -1, 48)
        self.resultWordValue = QLabel(self.resultContent)
        self.resultWordValue.setObjectName(u"resultWordValue")
        self.resultWordValue.setStyleSheet(u"#resultWordValue {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 24px ;\n"
"	font-weight: 400;\n"
"	color: #1C1C1C;\n"
"}")

        self.gridLayout.addWidget(self.resultWordValue, 1, 2, 1, 1)

        self.resultErrorValue = QLabel(self.resultContent)
        self.resultErrorValue.setObjectName(u"resultErrorValue")
        self.resultErrorValue.setStyleSheet(u"#resultErrorValue {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 24px ;\n"
"	font-weight: 400;\n"
"	color: #1C1C1C;\n"
"}")

        self.gridLayout.addWidget(self.resultErrorValue, 2, 2, 1, 1)

        self.resultTimeLb = QLabel(self.resultContent)
        self.resultTimeLb.setObjectName(u"resultTimeLb")
        self.resultTimeLb.setStyleSheet(u"#resultTimeLb {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 24px ;\n"
"	font-weight: 600;\n"
"	color: #1C1C1C;\n"
"}")

        self.gridLayout.addWidget(self.resultTimeLb, 3, 1, 1, 1)

        self.resultWordLb = QLabel(self.resultContent)
        self.resultWordLb.setObjectName(u"resultWordLb")
        self.resultWordLb.setStyleSheet(u"#resultWordLb {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 24px ;\n"
"	font-weight: 600;\n"
"	color: #1C1C1C;\n"
"}")

        self.gridLayout.addWidget(self.resultWordLb, 1, 1, 1, 1)

        self.resultErrorLb = QLabel(self.resultContent)
        self.resultErrorLb.setObjectName(u"resultErrorLb")
        self.resultErrorLb.setStyleSheet(u"#resultErrorLb {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 24px ;\n"
"	font-weight: 600;\n"
"	color: #1C1C1C;\n"
"}")

        self.gridLayout.addWidget(self.resultErrorLb, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 2, 0, 1, 1)

        self.resultImage = QLabel(self.resultContent)
        self.resultImage.setObjectName(u"resultImage")
        self.resultImage.setStyleSheet(u"#resultLb4 {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 24px ;\n"
"	font-weight: 600;\n"
"	color: #1C1C1C;\n"
"}")

        self.gridLayout.addWidget(self.resultImage, 0, 1, 1, 2)

        self.resultTimeValue = QLabel(self.resultContent)
        self.resultTimeValue.setObjectName(u"resultTimeValue")
        self.resultTimeValue.setStyleSheet(u"#resultTimeValue {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 24px ;\n"
"	font-weight: 400;\n"
"	color: #1C1C1C;\n"
"}")

        self.gridLayout.addWidget(self.resultTimeValue, 3, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)

        self.resultBtnMainMenu = QPushButton(self.resultContent)
        self.resultBtnMainMenu.setObjectName(u"resultBtnMainMenu")
        self.resultBtnMainMenu.setStyleSheet(u"#resultBtnMainMenu {\n"
"	background-color: #2BAD80;\n"
"	padding: 12px 24px;\n"
"	border-radius: 12px;\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 24px;\n"
"	font-weight: 400;\n"
"	color: #EDEBD6;\n"
"}\n"
"\n"
"#resultBtnMainMenu:hover{\n"
"	background-color: rgb(47, 193, 142);\n"
"}\n"
"\n"
"#resultBtnMainMenu:pressed{\n"
"background-color: rgb(39, 158, 116);\n"
"}")

        self.gridLayout.addWidget(self.resultBtnMainMenu, 5, 1, 1, 2)


        self.verticalLayout.addWidget(self.resultContent)


        self.horizontalLayout_2.addWidget(self.resultMain)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addWidget(self.resultWidget)


        self.retranslateUi(resultPage)

        QMetaObject.connectSlotsByName(resultPage)
    # setupUi

    def retranslateUi(self, resultPage):
        resultPage.setWindowTitle(QCoreApplication.translate("resultPage", u"Form", None))
        self.resultTitle.setText(QCoreApplication.translate("resultPage", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b", None))
        self.resultWordValue.setText("")
        self.resultErrorValue.setText("")
        self.resultTimeLb.setText(QCoreApplication.translate("resultPage", u"\u041f\u043e\u0442\u0440\u0430\u0447\u0435\u043d\u043e \u0432\u0440\u0435\u043c\u0435\u043d\u0438:", None))
        self.resultWordLb.setText(QCoreApplication.translate("resultPage", u"\u0417\u0430\u0433\u0430\u0434\u0430\u043d\u043d\u043e\u0435 \u0441\u043b\u043e\u0432\u043e:", None))
        self.resultErrorLb.setText(QCoreApplication.translate("resultPage", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0448\u0438\u0431\u043e\u043a:", None))
        self.resultImage.setText("")
        self.resultTimeValue.setText("")
        self.resultBtnMainMenu.setText(QCoreApplication.translate("resultPage", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
    # retranslateUi

