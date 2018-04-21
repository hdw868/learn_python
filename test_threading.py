import threading
import time
import traceback


def run_test(test_suite):
    print('Running test_suite [{}] started'.format(test_suite))
    time.sleep(10)
    print('Terminating test_suite [{}]!'.format(test_suite))


t1 = threading.Thread(target=run_test, args=('T01',))
t2 = threading.Thread(target=run_test, args=('T02',))
t1.setDaemon(True)
t2.setDaemon(True)
print('Before sub thread start: ' + str(threading.active_count()))
t1.start()
t2.start()
print('After sub thread start: ' + str(threading.active_count()))
try:
    while threading.active_count() > 1:
        time.sleep(0.1)
    print('After all sub thread terminated: ' + str(threading.active_count()))
    print('All test finished!')

except Exception as err:
    print(err, traceback.format_exc())
