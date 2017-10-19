# coding: utf-8

import abc
import time


class Writer:

    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    def write(self, content):
        _content = self.gen_content(content)
        with open(self.filename, 'a+') as f:
            f.write(_content)
            f.write('\n')

    @abc.abstractmethod
    def gen_content(self, content):
        return


class LogFile(Writer):

    def gen_content(self, content):
        return '{}    {}'.format(time.asctime(), content)


class DelimFile(Writer):

    def __init__(self, filename, sep):
        super(DelimFile, self).__init__(filename)

        self.sep = sep

    def gen_content(self, content):
        if not isinstance(content, list):
            raise Exception('Content must be list')
        return self.sep.join(content)
