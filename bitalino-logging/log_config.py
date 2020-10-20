from logging.config import dictConfig

import logging

LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s]: %(message)s'
        }
    },
    'handlers': {
        'h': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': logging.DEBUG
        }
    },
    'root': {
        'handlers': ['h'],
        'level': logging.DEBUG,
    }
}

def configure_logging():
    dictConfig(LOG_CONFIG)
