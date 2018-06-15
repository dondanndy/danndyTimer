import sqlite3
import datetime

'''
    This file contais every method dedicated to the management of the
    storage of times.
'''


class Storage:
    def __init__(self):
        self.conn = sqlite3.connect('times.db')
        self.c = self.conn.cursor()

        tables = ['c2x2', 'c3x3', 'c4x4']

        for table in tables:
            self.c.execute(f'CREATE TABLE IF NOT EXISTS {table} (Date TEXT,' +
                            'Scramble TEXT, Time TEXT)')
            self.conn.commit()

    # def clear_database():
    #     pass

    def insert_line(self, data, table):
        '''
            This function gets the parsed data to get into de database and it
            inserts it with the date
        '''

        day = datetime.date.today().isoformat()

        self.c.execute(f"INSERT INTO {table} VALUES(?,?,?)", [day] + data)
        self.conn.commit()

    def get_times(self, table):
        '''
            Get the times from a specific table
        '''

        self.c.execute(f"SELECT Time FROM {table}")
        data = self.c.fetchall()

        return data
