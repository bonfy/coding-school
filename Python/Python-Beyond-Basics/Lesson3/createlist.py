# coding: utf-8

import functools

def check_non_negative(index):
    """ check index non negative """
    def validator(f):
        @functools.wraps(f)
        def wrap(*args):
            if args[index] < 0:
                raise ValueError('Argument {} must be non-negative'.format(index))
            return f(*args)
        return wrap

    return validator

@check_non_negative(1)
def create_list(value, size):
    """ create list """
    return [value] * size
