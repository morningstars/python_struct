from threading import Thread
from time import ctime, sleep


class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs={}, name='TT'):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.name = name

    def run(self):
        self.target(*self.args, **self.kwargs)


"""
完成上面的MyThread类 使得整个程序可以正常执行

"""


def player(sec, song):
    for i in range(2):
        print("Playing %s : %s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={'song': '凉凉'}, name='happy')
t.start()
t.join()
