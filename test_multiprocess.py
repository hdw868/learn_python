# coding:utf8
import platform
import time
import inspect
from functools import wraps
from multiprocessing import Process


def stop_watcher(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print('{}({}) takes {} seconds'.format(func.__name__, (args, kwargs), te - ts))
        return result
    return wrapper


@stop_watcher
def counter(start):
    i = start
    for _ in range(40000000):
        i = i + 1
    return True


def main():
    pool = []
    start_time = time.time()
    for i in range(3):
        t = Process(target=counter, args=(i,))
        t.start()
        pool.append(t)
    for t in pool:
        t.join()
    end_time = time.time()
    print("{} Total time: {}".format(platform.python_version(), end_time - start_time))


if __name__ == '__main__':
    main()
