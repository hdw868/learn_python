import threading
import time
import traceback
import logging


def t_log():
    while True:
        time.sleep(0.01)
        logging.error("I'm logging...")


def t_print():
    while True:
        time.sleep(0.01)
        print("I'm print...")


t1 = threading.Thread(target=t_log, args=())
t2 = threading.Thread(target=t_print, args=())
t1.setDaemon(True)
# t2.setDaemon(True)
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
