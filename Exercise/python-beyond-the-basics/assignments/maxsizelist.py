# coding: utf-8


class MaxSizeList:

    def __init__(self, maxsize):
        self._lst = []
        if maxsize > 0:
            self._maxsize = maxsize
        else:
            raise Exception('Size must greater than 0')

    def push(self, value):

        size = len(self._lst)

        if size == self._maxsize:
            self._lst.pop(0)

        self._lst.append(value)

    def get_list(self):
        return self._lst
