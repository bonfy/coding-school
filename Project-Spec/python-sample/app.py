# -*- coding:utf-8 -*-

import os
from project import Model
from const import TIME_ZONE
from logger import log
from config import CONFIG

os.environ['TZ'] = TIME_ZONE

if __name__ == '__main__':
    m = Model()
    print(m)
    log(CONFIG, level='WARNING')
    log('Hello world')
