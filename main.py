import sys
from IO import IO
from interface import Interface
from PySide2.QtWidgets import QApplication
from storage import Storage

'''
    This file contains the basic functionalities of the program:
    the main funcions reads all the data, then passes it to the
    parsing methods and once we have it correctly parsed, we head
    to the storage part where we... well, storage it.
'''


def main():
    '''
    Main function.

    At this stage, it's going to read some string of scramble + time from
    a file and storage it; later, we will be able to read it from a file
    and finally we will set the GUI to enter them easily.
    '''

    app = QApplication([])
    widget = Interface()

    widget.resize(900, 600)
    widget.show()

    sys.exit(app.exec_())

    
if __name__ == '__main__':
    main()
