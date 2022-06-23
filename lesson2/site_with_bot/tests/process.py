from multiprocessing import Process
from time import sleep
def f(name, i):
    print('hello', name, i)
    sleep(3)

if __name__ == '__main__':
    p = [Process(target=f, args=('bob', i)) for i in range(25)]
    for proc in p:
        proc.start()
        proc.join()

    