import threading
import time
import traceback


def worker(event):
    while not event.is_set():
        print('{} Waiting for server to be ready'.format(time.ctime()))
        event.wait(2)
    print('{} Server is ready now, start doing some stuff'.format(time.ctime()))
    time.sleep(1)


def main():
    server_ready = threading.Event()
    t1 = threading.Thread(target=worker, args=(server_ready,), name='t1')
    t1.start()
    t2 = threading.Thread(target=worker, args=(server_ready,), name='t2')
    t2.start()
    print('{} Start run worker'.format(time.ctime()))
    time.sleep(5)
    server_ready.set()


if __name__ == "__main__":
    main()
