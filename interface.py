'''
    This file contains the Qt implementation of our interface.

    Right now it's far from complete and it's pretty much just visual,
    later on we will add events and how everything is going to connect
    with the core functionalities.
'''


import random
from PySide2.QtWidgets import QMainWindow, QMenu, QApplication, QAction


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()

        self.toolbar()        

    def toolbar(self):
        menubar = self.menuBar()

        # File Menu.
        fileMenu = menubar.addMenu('File')

        file = QMenu('Open', self)
        fileMenu.addMenu(file)

        new_set_act = QAction('New set of times', self) 
        fileMenu.addAction(new_set_act)

        import_act = QAction('Import database', self)
        
        fileMenu.addAction(import_act)

        # Session Menu
        SessionMenu = menubar.addMenu('Session')

        stats_act = QAction('Statistics of the session', self)
        SessionMenu.addAction(stats_act)

        delete_last_act = QAction('Delete last time', self)
        SessionMenu.addAction(delete_last_act)
