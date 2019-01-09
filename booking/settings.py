# encoding: utf8

import os

INIT_DONE = False

COOKIES = {}
PAY_FILEPATH = './{date}-{order_no}-{bank_id}.html'
STATION_CODE_MAP = {}

CHROME_APP_OPEN_CMD_MacOS = 'open -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome {filepath}'
CHROME_APP_OPEN_CMD_LINUX = None    # TODO Linux Chrome 打开文件cmd
CHROME_APP_OPEN_CMD_WINDOWS = None  # TODO Windows Chrome 打开文件cmd
CHROME_APP_OPEN_CMD = CHROME_APP_OPEN_CMD_MacOS

LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s|%(levelname)s|%(message)s'
        },
        'app': {
            'format': '%(asctime)s|%(levelname)s|%(module)s|%(funcName)s|%(lineno)d|%(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'INFO',
        },
        'app': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'app.log',
            'formatter': 'app',
            'level': 'DEBUG',
        }
    },
    'loggers': {
        'booking': {
            'handlers': ['console', 'app'],
            'level': os.getenv('BOOKING_LOG_LEVEL', 'INFO'),
        }
    },
}
