import os
try:
    from PySide6.QtWidgets import QApplication #  controller
except ImportError as e:
    #  incase PySide6 can't be loaded, despide environment checks in main script, revert to console app
    print(f"can't load the gui app (Failed to load PySide6)"
    print(f"raw error message: {e}")
    #  ask the user if they want to run the consoleApp 
    while True:
        answer = input("do you want to launch the console app (y/n)?_")
        if answer.lower() == 'n':
            break
        elif answer.lower() == 'y':
            #  run the consoleApp
            from ConsoleApp import ConsoleApp
            app = ConsoleApp()
            app.run()

from ..Model.Document import Document
from ..View.view import MainWindow


class ReaderApp(QApplication):
    def __init__(self, data_folder_path=''):
        super(ReaderApp, self).__init__()
        #  The Reader app holds a Model instance (Document) 
        self.data_folder_path = data_folder_path
        self.document = Document(os.path.join(data_folder_path, 'declaration1789.txt'), head_length=2)
        #  The Reader app holds a Viewer instance (MainWindow)
        self.ui = MainWindow(self.document)
        self.ui.setupUi(self.ui)  # Ensure this method call matches your implementation
        #  Connect 'click pushButton' event to a method 
        self.ui.pushButton.clicked.connect(self.display_article)

    def display_article(self):
        article_number = self.ui.spinBox.value()  
        text_to_display = self.document.get_article(article_number)
        self.ui.plainTextEdit.setPlainText(text_to_display)

    def run(self):
        self.ui.show()
