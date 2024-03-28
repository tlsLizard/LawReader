import sys
import re
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QVBoxLayout, QWidget

class ArticleWindow(QMainWindow):
    def __init__(self, article_text):
        super().__init__()
        self.setWindowTitle("Article")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        article_label = QLabel(article_text)
        layout.addWidget(article_label)
        self.central_widget.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Déclaration des droits de l'Homme")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        welcome_label = QLabel("Bienvenue ! Veuillez choisir un article :")
        layout.addWidget(welcome_label)

        self.article_combobox = QComboBox()
        for i in range(1, 18):
            self.article_combobox.addItem(str(i))

        self.article_combobox.currentIndexChanged.connect(self.show_article_window)

        layout.addWidget(self.article_combobox)

        self.central_widget.setLayout(layout)

        self.article_window = None
    def show_article_window(self):
            article_index = self.article_combobox.currentIndex() + 1
            article_text = read_file(article_index)
            if self.article_window:
                self.article_window.close()
            self.article_window = ArticleWindow(article_text)
            self.article_window.show()

def read_file(num_article):
    fichier = "declaration1789.txt"
    with open(fichier, 'r', encoding='utf-8') as file:
        current_article_num = None
        current_article_text = ''
        for line in file:
            line = line.strip()
            if line.startswith("Art. "):
                if current_article_num == num_article:
                    return current_article_text
                match = re.match(r'Art\. (\d+)', line)
                if match:
                    current_article_num = int(match.group(1))
                current_article_text = line
            else:
                current_article_text += line + '\n'

        if current_article_num == num_article:
            return current_article_text
        else:
            return "Article not found."

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())