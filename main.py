import sys

from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QApplication

from screens.game_page import Ui_gamePage
from screens.main_page import Ui_mainPage

from resources import resources_rc


class MainPage(QWidget, Ui_mainPage):
    def __init__(self):
        super(MainPage, self).__init__()
        self.setupUi(self)



class GamePage(QWidget, Ui_gamePage):
    def __init__(self):
        super(GamePage, self).__init__()
        self.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_page = MainPage()
        self.game_page = GamePage()

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.main_page)
        self.stackedWidget.addWidget(self.game_page)

        self.setCentralWidget(self.stackedWidget)

        self.main_page.btnMainExit.clicked.connect(self.close)
        self.main_page.btnStart.clicked.connect(self.start_game)
        self.game_page.gameButtonMainMenu.clicked.connect(self.main_menu)


    def start_game(self):
        self.stackedWidget.setCurrentIndex(1)

    def main_menu(self):
        self.stackedWidget.setCurrentIndex(0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    fonts = [QFontDatabase.addApplicationFont("resources/fonts/NunitoSans-SemiBold.ttf"),
             QFontDatabase.addApplicationFont("resources/fonts/NunitoSans-Regular.ttf"),]

    for font in fonts:
        if font == -1:
            print("Ошибка: не удалось загрузить шрифт")
        else:
            family = QFontDatabase.applicationFontFamilies(font)
            if family:
                print(f"Шрифт загружен: {family[0]}")

    app.setFont(QFont("NunitoSans"))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())
