import sys
import os
from check_env import check_env

if not check_env():
    while True:
        answer = input("do you want to launch the console app (y/n)?_")
        if answer.lower() == 'n':
            break
        elif answer.lower() == 'y':
            from src.Controller.ConsoleApp import ConsoleApp
            app = ConsoleApp()
            app.run()
else:
    from src.Controller.ReaderApp import ReaderApp

    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to data folder
    data_folder_path = os.path.join(current_dir, 'data')

    app = ReaderApp(data_folder_path=data_folder_path)
    app.document.file_name = 'declaration1789.txt'
    app.run()
    sys.exit(app.exec())
