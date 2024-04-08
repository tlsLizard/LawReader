import os
try:
    from PySide6.QtWidgets import QApplication #  controller
except ImportError as e:
    print(f"can't load the gui app (Failed to load PySide6), {e}")
    while True:
        answer = input("do you want to launch the console app (y/n)?_")
        if answer.lower() == 'n':
            break
        elif answer.lower() == 'y':
            from ConsoleApp import ConsoleApp
            app = ConsoleApp()
            app.run()

from ..Model.Document import Document
from ..View.view import MainWindow


class ReaderApp(QApplication):
    def __init__(self, data_folder_path=''):
        super(ReaderApp, self).__init__()
        self.data_folder_path = data_folder_path
        # Assuming 'declaration1789.txt' is in 'data_folder_path' and Document is your model
        self.document = Document(os.path.join(data_folder_path, 'declaration1789.txt'), head_length=2)

        self.ui = MainWindow(self.document)
        self.ui.setupUi(self.ui)  # Ensure this method call matches your implementation

        self.ui.pushButton.clicked.connect(self.display_article)

    def display_article(self):
        article_number = self.ui.spinBox.value()  # Assuming spinBox is correctly defined in MainWindow
        text_to_display = self.document.get_article(article_number)  # Assuming this is a method in Document
        self.ui.plainTextEdit.setPlainText(text_to_display)  # Assuming plainTextEdit is correctly defined in MainWindow

    def run(self):
        self.ui.show()
