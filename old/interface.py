import sys
import requests
from random import choice

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QListWidget
from PySide6.QtCore import Qt

def fetch_categories():
    response = requests.get("http://172.16.1.223:8000/v1/category/all")
    return response.json()


def fetch_word_data(categories: dict):
    r_cat = choice(categories.get("categories"))
    response = requests.get("http://172.16.1.223:8000/v1/word/random", params={"category": r_cat})
    return response.json()

def replace_char_at_index(original_string, indices, new_char):
    new_word = list(original_string)  # Преобразуем строку в список, чтобы можно было менять элементы
    for index in indices:
        if 0 <= index < len(new_word) and new_word[index] == '*':  # Дополнительная проверка
            new_word[index] = new_char  # Заменяем символ в списке
    return "".join(new_word)  # Преобразуем список обратно в строку
    

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        main_widget = QWidget()

        self.word_lb = QLabel()
        self.category_lb = QLabel()
        self.hint_lb = QLabel()
        self.word_entry = QLineEdit()
        self.letter_entry = QLineEdit()
        self.word_button = QPushButton("Ввести слово")
        self.letter_button = QPushButton("Ввести букву")
        self.used_letters = QListWidget()

        self.letter_button.clicked.connect(self.check_word)

        layout = QVBoxLayout()
        layout.addWidget(self.category_lb)
        layout.addWidget(self.hint_lb)
        layout.addWidget(self.word_lb)
        layout.addWidget(self.used_letters)
        layout.addWidget(self.letter_entry)
        layout.addWidget(self.letter_button)
        layout.addWidget(self.word_entry)
        layout.addWidget(self.word_button)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        categories = fetch_categories()
        word_obj = fetch_word_data(categories=categories)
        self.word = word_obj.get("word")
        self.encrypted = '*' * len(self.word)

        self.hint_lb.setText(word_obj.get("tell"))
        self.category_lb.setText(word_obj.get("category"))
        self.word_lb.setText(self.encrypted)

        print(self.word)

    def check_word(self):
        answer = self.letter_entry.text();
        if answer in self.word:
            print(f"Буква {answer} есть в слове!")
            indexes = [i for i, letter in enumerate(self.word) if answer in letter]
            self.encrypted = replace_char_at_index(self.encrypted, indexes, answer)
            if "*" not in self.encrypted:
                print(f"Вы угадали, это {self.encrypted}")
                self.word_lb.setText(self.encrypted)
            else:
                self.word_lb.setText(self.encrypted)
                print(f'Загаданное слово: {self.encrypted}')


        else:
            print(f"Буквы {answer} нет в слове!")
            isFinded = self.used_letters.findItems(answer, Qt.MatchContains)
            count = self.used_letters.count()
            if not isFinded:
                self.used_letters.addItem(answer)
            if count == 6:
                self.close()



app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()