from threading import Thread
from Queue import Queue
import random
import time

_sentinel = object()


def producer(num, name, out_q):
    data = 0
    for i in range(num * 100000):
        data += i
    time.sleep(random.randint(3, 7))
    print('Thread-{}:  {} is generated!'.format(name, data))
    out_q.put(data)


def consumer(in_q):
    while True:
        data = in_q.get(block=True)
        if data == _sentinel:
            break
        time.sleep(1)
        print('Consumer:{}'.format(data))


def generator(out_q):
    threads = [Thread(name=i,
                      target=producer,
                      args=(i, ('Thread-' + str(i)), out_q,)
                      ) for i in range(1, 5)]
    for t in threads:
        # t.setDaemon(True)
        t.start()
    # Do remenber that join method should be in another loop,
    # otherwise, it stucks to start() the next thread.
    for t in threads:
        t.join()
    print('Generator: All data generated!')
    out_q.put(_sentinel)


try:
    q = Queue()
    t = Thread(target=generator, args=(q,))
    t.start()
    consumer(q)
    print("main process over..")

except (SystemExit, KeyboardInterrupt):
    sys.exit()
