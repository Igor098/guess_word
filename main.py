import sys

import requests
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot, QThread, Signal
from PySide6.QtGui import QFontDatabase, QFont
from PySide6.QtWidgets import QMainWindow, QWidget, QStackedWidget, QApplication

from helpers.constants import max_errors
from helpers.decrypt_word import replace_char_at_index
from screens.result_page import Ui_resultPage
from screens.game_page import Ui_gamePage
from screens.loading_page import Ui_loadingPage
from screens.main_page import Ui_mainPage

from resources import resources_rc


class ApiRequestThread(QThread):
    data_received = Signal(dict)
    error_occurred = Signal(str)

    def run(self):
        try:
            params = {"category": "Животные"}
            response = requests.get("http://172.16.1.223:8001/v1/word/random", params=params)
            response.raise_for_status()
            data = response.json()
            self.data_received.emit(data)
        except Exception as e:
            self.error_occurred.emit(str(e))

class MainPage(QWidget, Ui_mainPage):
    def __init__(self):
        super(MainPage, self).__init__()
        self.setupUi(self)

class LoadingPage(QWidget, Ui_loadingPage):
    def __init__(self):
        super(LoadingPage, self).__init__()
        self.setupUi(self)

class GamePage(QWidget, Ui_gamePage):
    is_final = Signal()
    stop = Signal()

    def __init__(self):
        super(GamePage, self).__init__()
        self.setupUi(self)
        self.word = ''
        self.encrypted = ''
        self.max_errors = 0
        self.buttonCheckChar.clicked.connect(self.check_char)
        self.buttonCheckWord.clicked.connect(self.check_word)
        self.errors = 6

    def add_error(self, item):
        is_found = self.errorCharList.findItems(item, Qt.MatchFlag.MatchContains)
        if not is_found:
            self.errorCharList.addItem(item)

        count = self.errorCharList.count()

        self.gameErrorCountText.setText(f"{count} из {self.max_errors}")

        if count >= self.errors:
            print("count >>>", count, "\nerrors >>>", self.errors)
            self.stop.emit()

    def check_char(self):
        answer = self.gameCharInput.text().upper()
        if answer in self.word:
            print(f"Буква {answer} есть в слове!")
            indexes = [i for i, letter in enumerate(self.word) if answer in letter]
            self.encrypted = replace_char_at_index(self.encrypted, indexes, answer)
            if "❓" not in self.encrypted:
                print(f"Вы угадали, это {self.encrypted}")
                self.encryptedWordText.setText(self.encrypted)
                self.is_final.emit()
            else:
                self.encryptedWordText.setText(self.encrypted)
                print(f'Загаданное слово: {self.encrypted}')

        else:
            self.add_error(answer)


    def check_word(self):
        answer = self.gameWordInput.text().upper()
        if answer == self.word:
            self.encrypted = answer
            self.encryptedWordText.setText(answer)
            self.is_final.emit()
        else:
            self.add_error(answer)

class ResultPage(QWidget, Ui_resultPage):
    def __init__(self):
        super(ResultPage, self).__init__()
        self.setupUi(self)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_page = MainPage()
        self.game_page = GamePage()
        self.loading_page = LoadingPage()
        self.result_page = ResultPage()

        self.game_page.is_final.connect(self.check_final)
        self.game_page.stop.connect(self.check_errors)

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.main_page)
        self.stackedWidget.addWidget(self.game_page)
        self.stackedWidget.addWidget(self.loading_page)
        self.stackedWidget.addWidget(self.result_page)

        self.setCentralWidget(self.stackedWidget)

        self.main_page.btnMainExit.clicked.connect(self.close)
        self.main_page.btnStart.clicked.connect(self.start_game)
        self.game_page.gameButtonMainMenu.clicked.connect(self.main_menu)
        self.result_page.resultBtnMainMenu.clicked.connect(self.main_menu)


    def start_game(self):
        self.stackedWidget.setCurrentIndex(1)

        self.thread = ApiRequestThread()
        self.thread.data_received.connect(self.show_data)
        self.thread.error_occurred.connect(self.show_error)
        self.thread.start()

    def main_menu(self):
        self.stackedWidget.setCurrentIndex(0)

    @Slot()
    def check_final(self):
        if "❓" not in self.game_page.encrypted:
            print(f"Вы угадали, это {self.game_page.encrypted}")
            self.stackedWidget.setCurrentIndex(3)
            self.game_page.gameCharInput.clear()
            self.game_page.gameWordInput.clear()
            self.game_page.errorCharList.clear()

    @Slot()
    def check_errors(self):
        self.stackedWidget.setCurrentIndex(3)
        self.game_page.gameCharInput.clear()
        self.game_page.gameWordInput.clear()
        self.game_page.errorCharList.clear()

    @Slot()
    def load_data(self):

        self.thread = ApiRequestThread()
        self.thread.data_received.connect(self.show_data)
        self.thread.error_occurred.connect(self.show_error)
        self.thread.start()

    @Slot(dict)
    def show_data(self, data):
        print(data)
        self.game_page.word = data.get("word", "Ошибка")
        self.game_page.gameCategoryText.setText(data.get("category", "Неизвестно"))
        self.game_page.gameHintText.setText(data.get("tell", "Отсутствует"))
        self.game_page.encrypted = '❓' * len(self.game_page.word)
        self.game_page.encryptedWordText.setText(self.game_page.encrypted)
        difficulty = data.get("difficulty", None)

        if difficulty:
            self.game_page.max_errors = max_errors.get(difficulty, 0)
            self.game_page.gameErrorCountText.setText(f"0 из {self.game_page.max_errors}")

    @Slot(str)
    def show_error(self, error):
        self.label.setText(f"Ошибка: {error}")
        self.button.setEnabled(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    fonts = [QFontDatabase.addApplicationFont("resources/fonts/NunitoSans-SemiBold.ttf"),
             QFontDatabase.addApplicationFont("resources/fonts/NunitoSans-Regular.ttf"), ]

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
