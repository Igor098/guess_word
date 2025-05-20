from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PySide6.QtCore import QThread, Signal, Slot
import requests
import time


class ApiRequestThread(QThread):
    data_received = Signal(dict)
    error_occurred = Signal(str)

    def run(self):
        try:
            # Имитируем задержку, как будто долгий запрос
            params = {"category": "Животные"}
            response = requests.get("http://127.0.0.1:8001/v1/word/random", params=params)
            response.raise_for_status()
            data = response.json()
            self.data_received.emit(data)
        except Exception as e:
            self.error_occurred.emit(str(e))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Загрузка JSON")
        self.label = QLabel("Нажми, чтобы загрузить")
        self.button = QPushButton("Загрузить JSON")
        self.button.clicked.connect(self.load_data)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    @Slot()
    def load_data(self):
        self.label.setText("Загрузка...")
        self.button.setEnabled(False)

        self.thread = ApiRequestThread()
        self.thread.data_received.connect(self.show_data)
        self.thread.error_occurred.connect(self.show_error)
        self.thread.start()

    @Slot(dict)
    def show_data(self, data):
        self.label.setText(f"Загружено: {data}")
        self.button.setEnabled(True)

    @Slot(str)
    def show_error(self, error):
        self.label.setText(f"Ошибка: {error}")
        self.button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()