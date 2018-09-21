# encoding: utf-8
import logging
import os


def console_logger():
    """output log to console, the default level is info"""
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)-s %(message)s')
    ch.setFormatter(formatter)
    logger = logging.getLogger('')
    logger.addHandler(ch)
    return logger


def file_logger():
    fh = logging.FileHandler("test.log")
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(levelname)-s %(message)s')
    fh.setFormatter(formatter)
    logger = logging.getLogger('')
    logger.addHandler(fh)
    return logger


if __name__ == '__main__':
    _logger = console_logger()
    err = u'哇哈哈！'.encode('utf8').decode('gbk')
    print('print: '+err)
    _logger.warning(err)
    print(os.path.join(r'C:\w', r'a\b\c\d'))
