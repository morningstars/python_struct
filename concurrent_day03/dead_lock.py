from threading import Thread, Lock

from time import sleep


class Account:
    def __init__(self, id, balance, lock):
        self.id = id
        self.balance = balance
        self.lock = lock

    def withdraw(self, amount):
        self.balance -= amount

    def save(self, amount):
        self.balance += amount

    def get_balance(self):
        print(self.balance)
        return self.balance


# 转账
def transfer(from_, to, amount):
    # 上锁成功返回true
    if from_.lock.acquire():  # 锁住from账户
        from_.withdraw(amount)
        sleep(0.5)
        if to.lock.acquire():  # 锁住to账户
            to.save(amount)
            to.lock.release()
        from_.lock.release()
    print("转账完成")


# 创建两个账户
act1 = Account('zzz', 10000, Lock())
act2 = Account('lll', 20000, Lock())

t1 = Thread(target=transfer, args=(act1, act2, 1000))
t2 = Thread(target=transfer, args=(act2, act1, 1000))

t1.start()
t2.start()

t1.join()
t2.join()

act1.get_balance()
act2.get_balance()
