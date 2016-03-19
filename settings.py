
PROJECT_ROOT = '/media/thomas/Partition/Web/tornado-sqlalchemy'
DEBUG = True

def init_logging_mode(name):
    import logging
    if DEBUG == True: 
        log_level = logging.DEBUG
    else: 
        log_level = logging.NONSET
    logging.basicConfig(level=log_level)
    logger = logging.getLogger(__name__)
    logger.info('module {} loaded'.format(__name__))
    logger.info('module {} loaded'.format(name))
    return logger
