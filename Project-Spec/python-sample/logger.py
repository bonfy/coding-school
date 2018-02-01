# -*- coding:utf-8 -*-

import logging
import logging.config as log_conf
from pathlib import Path
from const import LOG_PATH, PROJECT_NAME

__all__ = ['log', ]

'''
CRITICAL	50
ERROR	40
WARNING	30
INFO	20
DEBUG	10
NOTSET	0
'''

LEVELS = ['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
LEVELS_CRITICAL = ['WARNING', 'ERROR', 'CRITICAL']

path = Path(LOG_PATH)

log_file = str(path / f'{PROJECT_NAME}.log')
log_err_file = str(path / f'{PROJECT_NAME}_err.log')

log_config = {
    'version': 1.0,
    'formatters': {
        'detail': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S %Z"
        },
        'simple': {
            'format': '%(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'detail'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 10,
            'filename': log_file,
            'level': 'INFO',
            'formatter': 'detail',
            'encoding': 'utf-8',
        },
        'critical': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 10,
            'filename': log_err_file,
            'level': 'WARNING',
            'formatter': 'detail',
            'encoding': 'utf-8',
        }
    },
    'loggers': {

        'common': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },

        'critical': {
            'handlers': ['console', 'critical'],
            'level': 'DEBUG',
        }
    }
}


log_conf.dictConfig(log_config)


def log(msg, *, name='common', level='DEBUG', prefix=''):
    """
    log 通用方法

    如果 LEVEL 在warning 以上，自动多记录一个 project_err.log 文件，方便定位问题
    """
    level = level.upper()
    if level not in LEVELS:
        level = 'DEBUG'

    if prefix:
        msg = f'[{prefix}] {msg}'
    logger = logging.getLogger(name)
    logger.log(logging.getLevelName(level), msg)

    if level in LEVELS_CRITICAL:
        logger_critical = logging.getLogger('critical')
        logger_critical.log(logging.getLevelName(level), msg)
