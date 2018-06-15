import re
import sys
from interface import MyWidget
from PySide2 import QtCore, QtWidgets, QtGui
from storage import Storage

'''
    This file contains the basic functionalities of the program:
    the main funcions reads all the data, then passes it to the
    parsing methods and once we have it correctly parsed, we head
    to the storage part where we... well, storage it.
'''


def parse_line(line):
    '''
        Parses a line, returning an array of time and scramble.
    '''

    try:
        re_time = re.compile(r"((\d{2}\.)?(\d{2}\.\d+))")
        time = re_time.search(line).group(0)
    except AttributeError:
        return None

    try:
        re_scramble = re.compile(r"((R|L|U|D|F|B)(\'|2)?(\s|$|\n))+")
        scramble = re_scramble.search(line).group(0)
    except AttributeError:
        return None

    return [scramble, time]


def main():
    '''
    Main function.

    At this stage, it's going to read some string of scramble + time from
    a file and storage it; later, we will be able to read it from a file
    and finally we will set the GUI to enter them easily.
    '''

    #Okay, this works :)

    # with open('times.txt', 'r') as file:
    #     times = file.readlines()

    # connection = Storage()
    # parsed_lines = []

    # for line in times:
    #     parsed_line = parse_line(line)
    #     if parsed_line is not None:
    #         connection.insert_line(parsed_line, 'c3x3')

    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(900, 600)
    widget.show()

    sys.exit(app.exec_())

    
if __name__ == '__main__':
    main()
