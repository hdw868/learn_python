import time

import gevent


def foo():
    print("running in foo")
    gevent.sleep(2)
    print("switch to foo again")


def bar():
    print("switch to bar")
    gevent.sleep(5)
    print("switch to bar again")


start = time.time()

gevent.joinall(
    [gevent.spawn(foo),
     gevent.spawn(bar)]
)

print(time.time() - start)
