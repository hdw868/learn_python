import time


def before():
    ts = time.time()
    value = [len(x) for x in open('tmp/test.log')]
    print(value)
    te = time.time()
    print(te - ts)


def after():
    # ts = time.time()
    value = (len(x) for x in open('tmp/test.log'))
    print(next(value))
    # te = time.time()
    # print(te - ts)


before()
for _ in xrange(len(open('tmp/test.log').readlines())):
    after()
