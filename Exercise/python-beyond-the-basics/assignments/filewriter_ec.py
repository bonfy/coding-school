# coding: utf-8

from datetime import datetime


class WriteFile:

    def __init__(self, filename, formatter):
        self.fw = open(filename, 'a')
        self.formatter = formatter()

    def write(self, line):
        self.fw.write(self.formatter.format(line))
        self.fw.write('\n')

    def close(self):
        self.fw.close()


class CSVFormatter:

    def __init__(self):
        self.sep = ','

    def format(self, lst):
        if not isinstance(lst, list):
            raise Exception('lst must be list')
        new_lst = [str(i) for i in lst]
        return self.sep.join(new_lst)


class LogFormatter:

    def format(self, text):
        dt = datetime.now()
        date_str = dt.strftime('%Y-%m-%d %H:%M')
        return '{0}    {1}'.format(date_str, text)
