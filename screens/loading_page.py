# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loadingPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_loadingPage(object):
    def setupUi(self, loadingPage):
        if not loadingPage.objectName():
            loadingPage.setObjectName(u"loadingPage")
        loadingPage.resize(1024, 600)
        loadingPage.setMinimumSize(QSize(1024, 600))
        loadingPage.setMaximumSize(QSize(16777215, 16777215))
        loadingPage.setStyleSheet(u"#loadingPage {\n"
"	background-color: rgb(255, 208, 82);\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(loadingPage)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.loadingWidget = QWidget(loadingPage)
        self.loadingWidget.setObjectName(u"loadingWidget")
        self.loadingWidget.setStyleSheet(u"#loadingWidget {\n"
"	background-color: rgb(255, 208, 82);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.loadingWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.loadingMain = QWidget(self.loadingWidget)
        self.loadingMain.setObjectName(u"loadingMain")
        self.loadingMain.setMinimumSize(QSize(400, 0))
        self.loadingMain.setMaximumSize(QSize(600, 16777215))
        self.loadingMain.setStyleSheet(u"#loadingMain {\n"
"	border-radius: 32px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.loadingMain)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.loadingHeader = QFrame(self.loadingMain)
        self.loadingHeader.setObjectName(u"loadingHeader")
        self.loadingHeader.setStyleSheet(u"#loadingHeader {\n"
"	border-top-left-radius: 32px;\n"
"	border-top-right-radius: 32px;\n"
"\n"
"	background-color: rgb(43, 171, 126);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.loadingHeader)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loadingTitle = QLabel(self.loadingHeader)
        self.loadingTitle.setObjectName(u"loadingTitle")
        self.loadingTitle.setStyleSheet(u"#loadingTitle {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 32px ;\n"
"	padding: 16px;\n"
"	font-weight: 600;\n"
"}")
        self.loadingTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.loadingTitle)


        self.verticalLayout_2.addWidget(self.loadingHeader)

        self.loadingContent = QFrame(self.loadingMain)
        self.loadingContent.setObjectName(u"loadingContent")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadingContent.sizePolicy().hasHeightForWidth())
        self.loadingContent.setSizePolicy(sizePolicy)
        self.loadingContent.setMinimumSize(QSize(500, 0))
        self.loadingContent.setSizeIncrement(QSize(0, 0))
        self.loadingContent.setStyleSheet(u"#loadingContent {\n"
"	border-bottom-left-radius: 32px;\n"
"	border-bottom-right-radius: 32px;\n"
"\n"
"	background-color: rgb(235, 244, 255);\n"
"}")
        self.loadingContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.loadingContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.loadingContent)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.connectLb = QLabel(self.loadingContent)
        self.connectLb.setObjectName(u"connectLb")
        self.connectLb.setStyleSheet(u"#connectLb {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 24px ;\n"
"	font-weight: 600;\n"
"	color: #1C1C1C;\n"
"}")
        self.connectLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.connectLb, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_2.addWidget(self.loadingContent)


        self.horizontalLayout_2.addWidget(self.loadingMain)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addWidget(self.loadingWidget)


        self.retranslateUi(loadingPage)

        QMetaObject.connectSlotsByName(loadingPage)
    # setupUi

    def retranslateUi(self, loadingPage):
        loadingPage.setWindowTitle(QCoreApplication.translate("loadingPage", u"Form", None))
#if QT_CONFIG(tooltip)
        self.loadingHeader.setToolTip(QCoreApplication.translate("loadingPage", u"<html><head/><body><p>G</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.loadingHeader.setWhatsThis(QCoreApplication.translate("loadingPage", u"<html><head/><body><p>\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.loadingTitle.setText(QCoreApplication.translate("loadingPage", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.connectLb.setText(QCoreApplication.translate("loadingPage", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435 \u043a \u0441\u0435\u0440\u0432\u0435\u0440\u0443", None))
    # retranslateUi

