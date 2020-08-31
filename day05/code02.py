"""

    排序算法

"""


class Sort(object):

    def __init__(self, list_target):
        self.list_ = list_target

    # 冒泡排序  O(n**2)

    def bubble(self):
        for i in range(len(self.list_) - 1):  # 第一个for循环表示需要循环比较的趟数
            # print(i)
            for j in range(len(self.list_) - i - 1):  # 第二个for循环表示从头开始比较，去掉末尾已经排好的个数
                if self.list_[j] > self.list_[j + 1]:
                    self.list_[j], self.list_[j + 1] = self.list_[j + 1], self.list_[j]
            # print(self.list_)
        return self.list_

    # 选择排序
    # 选择最小的放到前面  记录最小元素的下标 最后对换元素
    def select(self):
        for i in range(len(self.list_) - 1):
            min_index = i
            for j in range(i, len(self.list_)):
                if self.list_[j] < self.list_[min_index]:
                    min_index = j
            self.list_[i], self.list_[min] = self.list_[min_index], self.list_[i]
        return self.list_

    # 插入排序
    # 将元素插入到比自己小的元素后面  其他元素依次后移
    # 记录当前的元素
    def insert(self):
        for i in range(len(self.list_)):
            num = self.list_[i]
            j = i - 1
            while num < self.list_[j] and j >= 0:
                self.list_[j + 1] = self.list_[j]
                j -= 1
            self.list_[j + 1] = num
        return self.list_

    # 快速排序

    def quick(self):
        pass

    # 归并排序

    # 希尔排序

    # 堆排序

    # 基数排序


if __name__ == "__main__":
    li = [2, 1]
    # li = [2, 32, 123, 4, 211, 54, 0, 1]
    st = Sort(li)

    # st.bubble()
    # st.select()
    st.insert()
    print(li)
