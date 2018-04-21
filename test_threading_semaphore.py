import threading
import time

semaphore = threading.Semaphore(5)


def func():
    if semaphore.acquire():
        print(time.ctime() + threading.currentThread().getName() + ' get semaphore')
        time.sleep(2)
        semaphore.release()


for i in range(20):
    t1 = threading.Thread(target=func)
    t1.start()
