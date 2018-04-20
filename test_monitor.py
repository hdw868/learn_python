import collections
import csv
import logging
import os
import time


def log_to_console(level=logging.INFO):
    """output log to console, the default level is info"""
    console = logging.StreamHandler()
    console.setLevel(level)
    formatter = logging.Formatter('%(asctime)s %(levelname)-s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def monitor(desc):
    """Decorator which will log the timestamp of function"""
    def decorator(func):
        def wrapper(*args, **kw):
            # TODO mark step with global id
            logging.info('[STEP] ' + desc + ' start!')
            ts = time.time()
            result = func(*args, **kw)
            te = time.time()
            logging.info('[STEP] ' + desc + ' finished!')
            logging.info('Timing: run "%s.%s" in %2.3f sec' %
                         (func.__module__, func.__name__, te - ts))
            func_name = func.__name__
            arg_test_suite = kw.get('ts')
            time_cost = te - ts
            performance_writer(func_name, arg_test_suite, time_cost)
            return result
        return wrapper
    return decorator


def performance_writer(func_name, arg_test_suite, time_cost,
                       filename='performance_watcher.csv', delimiter=','):
    """Generate performance data in perormance_watcher.csv"""
    file_empty = (os.stat(filename).st_size == 0)
    with open(filename, 'ab') as csvfile:
        fieldnames = ['Cat.', 'Func_name', 'Test_suite', 'Time_cost']
        writer = csv.DictWriter(
            csvfile, dialect="excel", delimiter=delimiter, fieldnames=fieldnames)

        if file_empty:
            writer.writeheader()
        if func_name == 'main':
            writer.writerow(
                {'Cat.': 'Total', 'Func_name': func_name,
                 'Test_suite': arg_test_suite, 'Time_cost': time_cost})
            writer.writerow({})

        else:
            writer.writerow(
                {'Cat.': '', 'Func_name': func_name,
                 'Test_suite': arg_test_suite, 'Time_cost': time_cost})


def performance_reporter(test_suites, filename='performance_watcher.csv', delimiter=','):
    """"Generate performance report"""
    test_suites_dict = {test_suite: [] for test_suite in test_suites}
    misc_time = []
    with open(filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile, dialect="excel", delimiter=delimiter)
        reversed_reader = reversed(list(reader))
        for row in reversed_reader:
            # print(repr(row))
            if row['Func_name'] == '':
                break
            if row['Test_suite'] and row['Cat.'] != 'Total':
                test_suites_dict[row['Test_suite']].append(
                    float(row['Time_cost']))
                print(repr(row))
        print('time_cost_list:', test_suites_dict)
    with open(filename, 'ab') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        writer.writerow(['Total', '', '', sum(misc_time)])
        for test_suite in test_suites:
            writer.writerow(
                ['Total', '', test_suite, sum(test_suites_dict[test_suite])])
        # writer.writerow([])


@monitor('test1')
def fun_1(tt):
    for i in range(4000000):
        i += 1
    print('test1 ended!')


@monitor('test2')
def fun_2(tt, ts):
    for i in range(6000000):
        i += 1
    print('test2 ended!')


@monitor('test3')
def fun_3(tt, ts):
    for i in range(8000000):
        i += 1
    print('test3 ended!')


@monitor('main')
def main():
    fun_1('ccc')
    fun_1('ddd')
    fun_2('ccc', ts='ts2')
    fun_3('ccc', ts='ts2')
    fun_2('ccc', ts='ts3')
    fun_3('ccc', ts='ts3')
    performance_reporter(['ts2', 'ts3'])


if __name__ == '__main__':
    log_to_console()
    main()
