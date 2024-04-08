### LawReader

python app to read a text file and display its content:
 - read a document's head and body
 - display article chosen by the user (within the document's body)
 
 
### Requirements
 - the gui mode requires Python 3.8+ and PySide6
 - LawReader reverts to cmd mode if requirements are not met
   (tested under Python 3.6, without Pyside6)

### Install required dependencies

'''
pip install -r requirements.txt
'''
or

install PySide6 directly in the virtual environment:
'''
pip install PySide6
'''

### Developer's info
with PySide6, you can modify .ui files with:
'''
pyside6-designer
'''
then generate automatically the python class reprensenting the interface, like so:
'''
pyside6-uic mainwindow.ui -o ui_mainwindow.py
'''

### License
This project is licensed under the **TBD_Licence**. [Learn more](https://choosealicense.com/licenses/)
The utilization of PySide6 requires mentionning LGPL in License notes
comes as it, no warranty

