"""

    队列  先进先出

    队列的顺序存储

"""

class QueueError(Exception):
    pass


class SQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def enqueue(self, ele):
        self.elements.append(ele)

    def dequeue(self):
        if self.is_empty():
            raise QueueError("队列为空")

        return self.elements.pop(0)


if __name__ == "__main__":
    sq = SQueue()
    print(sq.is_empty())
    sq.enqueue(12)
    sq.enqueue(121)
    sq.enqueue(122)
    while not sq.is_empty():
        print(sq.dequeue())


