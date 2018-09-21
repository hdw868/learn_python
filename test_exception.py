import logging
import sys
import traceback

logging.basicConfig(level=logging.DEBUG, filename='test.log')
logger = logging.getLogger(__name__)


def test():
    try:
        int('A/N')
        return 0
    except Exception as error:
        logger.exception(error)
        print('Before raise')
        # return 1
        raise ValueError('0 division error')
        print('After raise')

    finally:
        print('Finally')
        # return 2


def tt():
    try:
        test()
    except:
        traceback.print_exc()
        sys.exit(3)


if __name__ == '__main__':
    tt()
