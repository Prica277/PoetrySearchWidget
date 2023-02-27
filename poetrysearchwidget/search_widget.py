from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QWidget, 
                             QLabel, QHBoxLayout, QLineEdit, 
                             QPushButton, QTextEdit)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt
import sys
import controller

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
        title_label.setFont(QFont("Calibri", 22))

        description = "Search the PoetryDB database by"
        description += " title, author, or lines."
        description_label = QLabel(description)
        description_label.setFont(QFont("Calibri", 14))

        search_layout = QHBoxLayout()
        self.search_field = QLineEdit()
        self.search_field.setFont(QFont("Calibri", 12))
        self.search_field.setPlaceholderText("title, author, or lines")

        search_button = QPushButton("Search")
        search_button.setFont(QFont("Calibri", 14))
        search_button.clicked.connect(self.search)

        search_layout.addWidget(self.search_field)
        search_layout.addWidget(search_button)

        results_text = QTextEdit("Results.")
        results_text.setFont(QFont("Calibri", 12))

        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addLayout(search_layout)
        layout.addWidget(results_text)

    def search(self):
        # get the user input
        search_text = self.search_field.text()

        # Make an API call with the controller script
        search_results = controller.makek_call(search_text)

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

    #https://poetrydb.org/title/Ozymandias/lines.json