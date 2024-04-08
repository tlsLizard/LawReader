"""
console app to display the head of a text file,
or pick a line to display in the body of file
"""
import os
from src.Model.Document import Document

class ConsoleApp:
    def __init__(self, document_file='declaration1789.txt', document_head_length=2):
        self.document_file = document_file
        self.document_head_length = document_head_length
        self.document_file_path = os.path.join(
                                               os.getcwd(),
                                               'data',
                                               self.document_file,
                                               )
        self.document=Document(self.document_file_path, self.document_head_length)

    def run(self):
        print('*'*40)
        print("Bienvenue dans l'application console de lecture de document!")
        print('*'*40)
        print(f"document: {str(self.document)}")
        print("head of document:")
        for line in self.document.head:
            print(line)
        print('-'*40)
        #print("body of document:")
        #for line in self.document.body:
        #    print(line)

        while True :

            exit_loop = int(input("Voulez vous continuer ? \n (1) - Oui \n (2) - Non \n"))

            if exit_loop == 2 :
                break

            response = int(input("Quel article de la constitution voulez-vous afficher ? \n (1) - (17) \n"))

            if response < 1 or response > 17 :
                print("\n La saisie est incorrecte \n")
            else :
                print("\n Vous avez choisi l'article ", response, "\n")
                print(self.document.articles[response-1], "\n")


if __name__ == "__main__":
    print("test de launch_console_app()")
    import os
    import sys

    file_name = 'declaration1789.txt'  # Adjust here
    file_path = os.path.join(os.pardir, 'data', file_name)
    head_length = 2
    app = ConsoleApp(file_path, head_length)
    app.run()
    del app
