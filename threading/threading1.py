
import threading,time


def f():

    print("1")
    time.sleep(5)
    print("2")
    print(threading.current_thread().getName())


def f1():

    print("5")
    time.sleep(5)
    print("6")
    print(threading.current_thread().getName())


t1 = threading.Thread(target=f, name="Profun", daemon=True)
t2 = threading.Thread(target=f1, name='Jesu')
# print("3")
t1.start()
# print("4")
t2.start()

