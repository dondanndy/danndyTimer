'''
    This file contains an IO class which takes care of dealing with external
    files.
    
    Initially, it will just read the times from a file, later it should be
    able to handle a full export/import of database.
'''
import re


class IO:
    def __init__(self, path):

        self.path = path

    def read_and_parse(self):

        with open('times.txt', 'r') as file:
            times = file.readlines()

        parsed_lines = []

        for line in times:
            parsed_line = self.parse_line(line)
            parsed_lines.append(parsed_line)

        return parsed_lines

    def parse_line(self, line):
        '''
            Parses a line, returning an array of time and scramble.
        '''

        try:
            re_time = re.compile(r"((\d{2}\.)?(\d{2}\.\d+))")
            time = re_time.search(line).group(0)
        except AttributeError:
            return None

        try:
            re_scramble = re.compile(r"((R|L|U|D|F|B|x|y|z)(\'|2)?(\s|$|\n))+")
            scramble = re_scramble.search(line).group(0)
        except AttributeError:
            return None

        return [scramble, time]