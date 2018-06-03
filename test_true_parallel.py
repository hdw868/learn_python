import time
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor


def gcd(pair):
    """Find the greatest common divisor """
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Running "%s" in %.3f seconds' % (func.__name__, (end - start)))
        return result

    return wrapper


@time_it
def run(numbers):
    results = list(map(gcd, numbers))
    return results


@time_it
def run_with_threads(numbers):
    pool = ThreadPoolExecutor(max_workers=4)
    results = list(pool.map(gcd, numbers))
    return results


@time_it
def run_with_processes(numbers):
    pool = ProcessPoolExecutor(max_workers=4)
    results = list(pool.map(gcd, numbers))
    return results


if __name__ == '__main__':
    _numbers = [(1963309, 2265973), (2030677, 3814172),
                (1551645, 2229620), (2039045, 2020802)]
    run(_numbers)
    run_with_threads(_numbers)
    run_with_processes(_numbers)
