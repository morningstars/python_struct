from threading import Thread


class MyThread(Thread):
    def __init__(self):
        super().__init__()
        print("init")

    def run(self) -> None:
        pass
