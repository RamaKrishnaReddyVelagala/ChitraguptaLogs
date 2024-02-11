import logging.config

logger = logging.getLogger("myapp")
# Here try to get name of the ml model we have.


logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': 'DEBUG',
            'stream': 'ext://sys.stdout',  # Use standard output
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}