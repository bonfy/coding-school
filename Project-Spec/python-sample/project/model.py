# -*- coding:utf-8 -*-

import datetime


class Model:

    def __init__(self, data=None):
        self.data = data if data else 'Hello Project'
        self.tm = self.get_time()

    def __repr__(self):
        return f'<Model: {self.data} - {self.tm}>'

    def get_time(self):
        now_t = datetime.datetime.now()
        return f'Instance Time: {now_t}'
