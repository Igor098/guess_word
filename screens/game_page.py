# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gamePage.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
                               QLabel, QLineEdit, QListView, QListWidget,
                               QPushButton, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)

class Ui_gamePage(object):
    def setupUi(self, gamePage):
        if not gamePage.objectName():
            gamePage.setObjectName(u"gamePage")
        gamePage.resize(1100, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(gamePage.sizePolicy().hasHeightForWidth())
        gamePage.setSizePolicy(sizePolicy)
        gamePage.setMinimumSize(QSize(1100, 600))
        gamePage.setStyleSheet(u"#gamePage {\n"
"	font-family: \"Nunito Sans Normal\";\n"
"	background-color: #FFC13A;\n"
"}")
        self.verticalLayout = QVBoxLayout(gamePage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gameHeader = QFrame(gamePage)
        self.gameHeader.setObjectName(u"gameHeader")
        self.gameHeader.setStyleSheet(u"#gameHeader{\n"
"	background-color: #2BAD80;\n"
"}")
        self.gameHeader.setFrameShape(QFrame.StyledPanel)
        self.gameHeader.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.gameHeader)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gameTitle = QLabel(self.gameHeader)
        self.gameTitle.setObjectName(u"gameTitle")
        self.gameTitle.setStyleSheet(u"#gameTitle {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 68px;\n"
"	font-weight: 600;\n"
"	color: #FEF5D6;\n"
"}")
        self.gameTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.gameTitle)


        self.verticalLayout.addWidget(self.gameHeader)

        self.gameMainContainer = QWidget(gamePage)
        self.gameMainContainer.setObjectName(u"gameMainContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.gameMainContainer.sizePolicy().hasHeightForWidth())
        self.gameMainContainer.setSizePolicy(sizePolicy1)
        self.gameMainContainer.setStyleSheet(u"#gameMainContainer{\n"
"	background-color: #FFC13A;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #1C1C1C;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.gameMainContainer)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(24, 24, 24, 0)
        self.gameFieldContainer = QWidget(self.gameMainContainer)
        self.gameFieldContainer.setObjectName(u"gameFieldContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.gameFieldContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.gameFieldWrapper = QWidget(self.gameFieldContainer)
        self.gameFieldWrapper.setObjectName(u"gameFieldWrapper")
        sizePolicy1.setHeightForWidth(self.gameFieldWrapper.sizePolicy().hasHeightForWidth())
        self.gameFieldWrapper.setSizePolicy(sizePolicy1)
        self.verticalLayout_3 = QVBoxLayout(self.gameFieldWrapper)
        self.verticalLayout_3.setSpacing(24)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gameInfoContainer = QWidget(self.gameFieldWrapper)
        self.gameInfoContainer.setObjectName(u"gameInfoContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gameInfoContainer.sizePolicy().hasHeightForWidth())
        self.gameInfoContainer.setSizePolicy(sizePolicy2)
        self.gameInfoContainer.setMinimumSize(QSize(0, 100))
        self.gameInfoContainer.setStyleSheet(u"#gameInfoContainer {\n"
"	background-color: #FFF6D5;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 20px;\n"
"	font-weight: 400;\n"
"}\n"
"\n"
"#gameCategoryLb, #gameHintLb {\n"
"	font-weight: 500;\n"
"}")
        self.gridLayout = QGridLayout(self.gameInfoContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setContentsMargins(24, -1, 24, -1)
        self.gameCategoryText = QLabel(self.gameInfoContainer)
        self.gameCategoryText.setObjectName(u"gameCategoryText")

        self.gridLayout.addWidget(self.gameCategoryText, 0, 1, 1, 1)

        self.gameHintText = QLabel(self.gameInfoContainer)
        self.gameHintText.setObjectName(u"gameHintText")

        self.gridLayout.addWidget(self.gameHintText, 1, 1, 1, 1)

        self.gameCategoryLb = QLabel(self.gameInfoContainer)
        self.gameCategoryLb.setObjectName(u"gameCategoryLb")
        self.gameCategoryLb.setStyleSheet(u"#gameCategoryLb {\n"
"	font-family: \"NunitoSans\";\n"
"	font-weight: 600;\n"
"}")

        self.gridLayout.addWidget(self.gameCategoryLb, 0, 0, 1, 1)

        self.gameHintLb = QLabel(self.gameInfoContainer)
        self.gameHintLb.setObjectName(u"gameHintLb")
        self.gameHintLb.setStyleSheet(u"#gameHintLb {\n"
"	font-family: \"NunitoSans\";\n"
"	font-weight: 600;\n"
"}")

        self.gridLayout.addWidget(self.gameHintLb, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.gameInfoContainer)

        self.gameWrapper = QWidget(self.gameFieldWrapper)
        self.gameWrapper.setObjectName(u"gameWrapper")
        sizePolicy1.setHeightForWidth(self.gameWrapper.sizePolicy().hasHeightForWidth())
        self.gameWrapper.setSizePolicy(sizePolicy1)
        self.horizontalLayout_3 = QHBoxLayout(self.gameWrapper)
        self.horizontalLayout_3.setSpacing(32)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gameField = QWidget(self.gameWrapper)
        self.gameField.setObjectName(u"gameField")
        self.gameField.setMinimumSize(QSize(600, 0))
        self.gameField.setMaximumSize(QSize(1100, 16777215))
        self.gameField.setStyleSheet(u"#gameField {\n"
"	background-color: #FFF6D5;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 20px;\n"
"	font-weight: 400;\n"
"	color: #1C1C1C;\n"
"}\n"
"\n"
"#encryptedWordText {\n"
"	color: #1C1C1C;\n"
"	font-size: 18px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius: 12px;\n"
"	font-size: 20px;\n"
"	padding: 0 12px;\n"
"	background-color: #FFFDF4;\n"
"	color: #1C1C1C;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border: 2px solid #D5DEFF;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #F59428;\n"
"	padding: 8px 16px;\n"
"	border-radius: 12px;\n"
"	font-size: 20px;\n"
"	font-weight: 400;\n"
"	color: #EDEBD6;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 172, 29);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(220, 131, 35);\n"
"}")
        self.gridLayout_2 = QGridLayout(self.gameField)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(24)
        self.gridLayout_2.setContentsMargins(16, 24, 16, 0)
        self.gameWordLb = QLabel(self.gameField)
        self.gameWordLb.setObjectName(u"gameWordLb")

        self.gridLayout_2.addWidget(self.gameWordLb, 2, 0, 1, 1)

        self.buttonCheckChar = QPushButton(self.gameField)
        self.buttonCheckChar.setObjectName(u"buttonCheckChar")

        self.gridLayout_2.addWidget(self.buttonCheckChar, 1, 2, 1, 1)

        self.buttonCheckWord = QPushButton(self.gameField)
        self.buttonCheckWord.setObjectName(u"buttonCheckWord")

        self.gridLayout_2.addWidget(self.buttonCheckWord, 2, 2, 1, 1)

        self.gameCharLb = QLabel(self.gameField)
        self.gameCharLb.setObjectName(u"gameCharLb")

        self.gridLayout_2.addWidget(self.gameCharLb, 1, 0, 1, 1)

        self.gameWordInput = QLineEdit(self.gameField)
        self.gameWordInput.setObjectName(u"gameWordInput")
        sizePolicy2.setHeightForWidth(self.gameWordInput.sizePolicy().hasHeightForWidth())
        self.gameWordInput.setSizePolicy(sizePolicy2)
        self.gameWordInput.setMinimumSize(QSize(300, 0))

        self.gridLayout_2.addWidget(self.gameWordInput, 2, 1, 1, 1)

        self.gameCharInput = QLineEdit(self.gameField)
        self.gameCharInput.setObjectName(u"gameCharInput")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gameCharInput.sizePolicy().hasHeightForWidth())
        self.gameCharInput.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.gameCharInput, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 3, 1, 1)

        self.encryptedWordText = QLabel(self.gameField)
        self.encryptedWordText.setObjectName(u"encryptedWordText")
        self.encryptedWordText.setStyleSheet(u"")
        self.encryptedWordText.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.encryptedWordText, 0, 0, 1, 4)


        self.horizontalLayout_3.addWidget(self.gameField)

        self.gameStatistics = QWidget(self.gameWrapper)
        self.gameStatistics.setObjectName(u"gameStatistics")
        self.gameStatistics.setMinimumSize(QSize(300, 0))
        self.gameStatistics.setMaximumSize(QSize(800, 16777215))
        self.gameStatistics.setStyleSheet(u"#gameStatistics {\n"
"	background-color: #FFF6D5;\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QLabel {\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 20px;\n"
"	font-weight: 400;\n"
"}\n"
"\n"
"#statisticsTitle {\n"
"	font-size: 24px;\n"
"	font-weight: 500;\n"
"	margin-bottom: 8px;\n"
"}\n"
"\n"
"#errorCharList {\n"
"	font-size: 16px;\n"
"	font-weight: 400;\n"
"	background-color: #FFFDF4;\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"	color: #1C1C1C;\n"
"}\n"
"\n"
"#errorCharList::item {\n"
"	padding: 2px;\n"
"}\n"
"\n"
"#errorCharList::item:selected {\n"
"	padding: 2px;\n"
"    background-color: #2ABf9E;\n"
"	color: #1C1C1C;\n"
"	underline: none;\n"
"}\n"
"\n"
"#errorCharList::item:hover {\n"
"	padding: 1px;\n"
"	border: 1px solid #D5DEFF;\n"
"}\n"
"\n"
"#errorCharList::item:focus {\n"
"	padding: 2px;\n"
"	border: none;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.gameStatistics)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(16, 16, 16, 16)
        self.gameErrorCountLb = QLabel(self.gameStatistics)
        self.gameErrorCountLb.setObjectName(u"gameErrorCountLb")

        self.gridLayout_3.addWidget(self.gameErrorCountLb, 1, 0, 1, 1)

        self.gameUsedCharsLb = QLabel(self.gameStatistics)
        self.gameUsedCharsLb.setObjectName(u"gameUsedCharsLb")

        self.gridLayout_3.addWidget(self.gameUsedCharsLb, 2, 0, 1, 1)

        self.gameErrorCountText = QLabel(self.gameStatistics)
        self.gameErrorCountText.setObjectName(u"gameErrorCountText")

        self.gridLayout_3.addWidget(self.gameErrorCountText, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.errorCharList = QListWidget(self.gameStatistics)
        self.errorCharList.setObjectName(u"errorCharList")
        sizePolicy2.setHeightForWidth(self.errorCharList.sizePolicy().hasHeightForWidth())
        self.errorCharList.setSizePolicy(sizePolicy2)
        self.errorCharList.setFlow(QListView.LeftToRight)
        self.errorCharList.setProperty(u"isWrapping", True)
        self.errorCharList.setSpacing(8)
        self.errorCharList.setViewMode(QListView.IconMode)
        self.errorCharList.setUniformItemSizes(False)
        self.errorCharList.setWordWrap(False)
        self.errorCharList.setSortingEnabled(True)

        self.gridLayout_3.addWidget(self.errorCharList, 3, 0, 1, 3)

        self.statisticsTitle = QLabel(self.gameStatistics)
        self.statisticsTitle.setObjectName(u"statisticsTitle")
        self.statisticsTitle.setStyleSheet(u"#statisticsTitle {\n"
"	font-family: \"NunitoSans\";\n"
"	font-weight: 600;\n"
"}")
        self.statisticsTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.statisticsTitle, 0, 0, 1, 3)


        self.horizontalLayout_3.addWidget(self.gameStatistics)


        self.verticalLayout_3.addWidget(self.gameWrapper)

        self.gameButtons = QFrame(self.gameFieldWrapper)
        self.gameButtons.setObjectName(u"gameButtons")
        self.gameButtons.setStyleSheet(u"#gameButtons{\n"
"	background-color: #FFC13A;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #2BAD80;\n"
"	padding: 12px 24px;\n"
"	border-radius: 12px;\n"
"	font-family: \"NunitoSans\";\n"
"	font-size: 24px;\n"
"	font-weight: 400;\n"
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
        self.gameButtons.setFrameShape(QFrame.StyledPanel)
        self.gameButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.gameButtons)
        self.horizontalLayout_2.setSpacing(16)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gameButtonLuze = QPushButton(self.gameButtons)
        self.gameButtonLuze.setObjectName(u"gameButtonLuze")

        self.horizontalLayout_2.addWidget(self.gameButtonLuze)

        self.gameButtonRepeat = QPushButton(self.gameButtons)
        self.gameButtonRepeat.setObjectName(u"gameButtonRepeat")

        self.horizontalLayout_2.addWidget(self.gameButtonRepeat)

        self.gameButtonMainMenu = QPushButton(self.gameButtons)
        self.gameButtonMainMenu.setObjectName(u"gameButtonMainMenu")

        self.horizontalLayout_2.addWidget(self.gameButtonMainMenu)


        self.verticalLayout_3.addWidget(self.gameButtons)


        self.horizontalLayout_4.addWidget(self.gameFieldWrapper)

        self.horizontalSpacer_4 = QSpacerItem(5, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.gameFieldContainer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.verticalLayout.addWidget(self.gameMainContainer)


        self.retranslateUi(gamePage)

        self.errorCharList.setCurrentRow(-1)


        QMetaObject.connectSlotsByName(gamePage)
    # setupUi

    def retranslateUi(self, gamePage):
        gamePage.setWindowTitle(QCoreApplication.translate("gamePage", u"Form", None))
        self.gameTitle.setText(QCoreApplication.translate("gamePage", u"\u0423\u0433\u0430\u0434\u0430\u0439 \u0441\u043b\u043e\u0432\u043e", None))
        self.gameCategoryText.setText("")
        self.gameHintText.setText("")
        self.gameCategoryLb.setText(QCoreApplication.translate("gamePage", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.gameHintLb.setText(QCoreApplication.translate("gamePage", u"\u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430:", None))
        self.gameWordLb.setText(QCoreApplication.translate("gamePage", u"\u0421\u043b\u043e\u0432\u043e:", None))
        self.buttonCheckChar.setText(QCoreApplication.translate("gamePage", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.buttonCheckWord.setText(QCoreApplication.translate("gamePage", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c", None))
        self.gameCharLb.setText(QCoreApplication.translate("gamePage", u"\u0411\u0443\u043a\u0432\u0430:", None))
        self.encryptedWordText.setText("")
        self.gameErrorCountLb.setText(QCoreApplication.translate("gamePage", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0448\u0438\u0431\u043e\u043a: ", None))
        self.gameUsedCharsLb.setText(QCoreApplication.translate("gamePage", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u043d\u044b\u0435 \u0431\u0443\u043a\u0432\u044b: ", None))
        self.gameErrorCountText.setText("")
        self.statisticsTitle.setText(QCoreApplication.translate("gamePage", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.gameButtonLuze.setText(QCoreApplication.translate("gamePage", u"\u0421\u0434\u0430\u0442\u044c\u0441\u044f", None))
        self.gameButtonRepeat.setText(QCoreApplication.translate("gamePage", u"\u0421\u044b\u0433\u0440\u0430\u0442\u044c \u0441\u043d\u043e\u0432\u0430", None))
        self.gameButtonMainMenu.setText(QCoreApplication.translate("gamePage", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
    # retranslateUi

