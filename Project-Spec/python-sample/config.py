# -*- coding:utf-8 -*-

import yaml
from const import CONFIG_FILE

__all__ = ['CONFIG']


def read_config_file(filename=CONFIG_FILE):
    with open(filename, 'r') as f:
        config = yaml.load(f)
    return config


CONFIG = read_config_file()
