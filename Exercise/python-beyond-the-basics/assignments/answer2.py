# coding: utf-8

import abc
from datetime import datetime


class Writer:

    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        with open(self.filename, 'a') as f:
            f.write(text + '\n')

    @abc.abstractmethod
    def write(self):
        return


class LogFile(Writer):

    def write(self, text):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        self.write_line('{}    {}'.format(date_str, text))


class DelimFile(Writer):

    def __init__(self, filename, sep):
        super(DelimFile, self).__init__(filename)
        self.sep = sep

    def write(self, lst):
        if not isinstance(lst, list):
            raise Exception('Content must be list')
        line = self.sep.join(lst)
        self.write_line(line)
