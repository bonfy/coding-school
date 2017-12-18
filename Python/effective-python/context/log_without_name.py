# coding: utf-8

'''
Log without name
'''

import logging
from contextlib import contextmanager

@contextmanager
def debug_logging(level):
    """ debug logging """
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)

    try:
        yield
    finally:
        logger.setLevel(old_level)

def my_function():
    """ my function """
    logging.debug('Some debug info')
    logging.error('A real error')
    logging.debug('More debug info')

with debug_logging(logging.DEBUG):
    my_function()

my_function()
