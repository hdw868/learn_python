import logging

logging.basicConfig(level=logging.DEBUG, filename='test.log')
logger = logging.getLogger(__name__)


def test():
    try:
        int('A/N')
        return 0
    except Exception as error:
        logger.exception(error)
        print('Before raise')
        return 1
        raise ValueError from error
        print('After raise')

    finally:
        print('Finally')
        # return 2


print(test())
