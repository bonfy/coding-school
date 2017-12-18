# coding: utf-8

'''
Log with name
'''

import logging
from contextlib import contextmanager


@contextmanager
def log_level(level, name):
    """ log level """
    _logger = logging.getLogger(name)
    old_level = _logger.getEffectiveLevel()
    _logger.setLevel(level)

    try:
        yield _logger
    finally:
        _logger.setLevel(old_level)


with log_level(logging.DEBUG, 'my-log') as logger:
    logging.debug('This is global logger')
    logger.debug('This is my-log logger')

logger = logging.getLogger('my-log')
logger.debug('Does not print anything')
logger.error('this will')
