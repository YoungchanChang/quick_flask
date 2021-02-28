# 참조 : https://docs.python.org/ko/3/howto/logging.html
# 로그 객체 : https://docs.python.org/ko/3/library/logging.html#logrecord-attributes
# 로그 핸들러 : https://docs.python.org/ko/3/library/logging.handlers.html
# 참조할만한 글 : https://www.daleseo.com/python-logging-config/
"""
로그 기능
- 로깅 config
- 로깅 쓰는 법
"""
import logging

def log_basic():
    """기본 로그"""
    logging.basicConfig(filename='test.log', level=logging.DEBUG)

    logging.critical('critical')
    logging.error('error')
    logging.warning('warning')
    logging.info('critical')
    logging.debug('debug')

    logging.info('info {}'.format('test'))
    logging.info('info %s %s' % ('test', 'test2'))
    logging.info('info %s %s', 'test', 'test2')


def log_formatter():
    """로그 포매터"""
    formatter = '%(levelname)s:%(message)s'
    formatter = '%(asctime)s:%(message)s'
    formatter = "%(asctime)s - %(name)s - [%(process)d] - [%(thread)d] - [%(levelname)s] (%(filename)s:%(lineno)d) > %(message)s"
    logging.basicConfig(filename='test.log', level=logging.DEBUG, format=formatter)

    logging.critical('critical')
    logging.error('error')
    logging.warning('warning')
    logging.info('critical')
    logging.debug('debug')

    logging.info('info {}'.format('test'))
    logging.info('info %s %s' % ('test', 'test2'))
    logging.info('info %s %s', 'test', 'test2')


def log_logger():
    """ logger - 로그를 쓰는 자, 실제로 로그를 쓰게된다.
    logging대신에 logger라고 불리게 된다. formatter의 %(name)s과 연관 """
    logging.basicConfig(level=logging.DEBUG)

    logging.info('info')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.debug('debug')

def log_handler():
    """ handler - 로그를 다루는 자. 로그가 어디에 적히게 할 것인가."""
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    h = logging.FileHandler('logtest.log')
    logger.addHandler(h)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.debug('dddd debug')

class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()

        return 'password' not in log_message

def log_filter():
    """패스워드 같은 문자열이 들어가있는 경우 필터링한다. """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.addFilter(NoPassFilter())
    logger.info('from main')
    logger.info('from main password = "test"')


""" Config를 쓴다."""

import logging.config

def logger_config_ini():
    """filter by name"""
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('simpleExample')

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

def simple_log_test():
    """fileConfig에 root를 쓴다."""
    import logging.config
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

def logging_config_dict():
    """딕셔너리 config"""
    logging.config.dictConfig({
        'version':1,
        'formatters' : {
            'sampleFormatter':{
                'format': '%(asctime)s %(name) - 12s %(levelname)-8s %(message)s'
            }
        },
        'handlers':{
            'sampleHandlers' : {
                'class' : 'logging.StreamHandler',
                'formatter' : 'sampleFormatter',
                'level': logging.DEBUG
            }
        },
        'root':{
            'handlers': ['sampleHandlers'],
            'level' : logging.DEBUG,
            'propagate' : 0
        },
        'loggers':{
            'simpleExample' : {
                'handlers' : ['sampleHandlers'],
                'level' : logging.DEBUG,
                'propagate' : 0
            }
        }
    })
    logger = logging.getLogger(__name__)
    logger.debug('debug message')
    logger.debug('info message')
    logger.debug('error message')
    logger.debug('critical message')
logging_config_dict()