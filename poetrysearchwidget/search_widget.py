from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QWidget, 
                             QLabel, QHBoxLayout, QLineEdit, 
                             QPushButton, QTextEdit)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        self.resources = "poetrysearchwidget/resources/"
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle("The Poetry Widget")
        self.setWindowIcon(QIcon(self.resources + "icon.jpg"))
        self.UI()

    def UI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Creating Widgets
        title_label = QLabel("Poetry Search Widget")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        description = "Search the PoetryDB database by"
        description += " title, author, lines, linecount,"
        description += " or poetrycount."
        description_label = QLabel(description)

        search_layout = QHBoxLayout()
        self.search_field = QLineEdit()
        search_button = QPushButton("Search")
        search_layout.addWidget(self.search_field)
        search_layout.addWidget(search_button)

        results_text = QTextEdit("Results.")

        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addLayout(search_layout)
        layout.addWidget(results_text)

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()