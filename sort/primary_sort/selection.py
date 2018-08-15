# -*- coding: utf-8 -*-
class Selection(object):
    """
    选择排序，将第i小的元素放到list[i]
    """
    def sort(self, list):
        n = len(list)  #数组长度
        for i in range(n):
            min = i  #最小元素索引，第i小元素依次放到list[0],list[1]...list[i]
            for j in range(i+1, n):   #list[i]和数组list[i+1...n]中的最小元素交换
                if self.less(list[j], list[min]):
                    min = j
            self.exch(list, i, min)
    def less(self, v, w):
        return v < w
    def exch(self, list, i, j):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
    def show(self, list):
        for i in list:
            print i,
    def is_sorted(self, list):
        for i in range(1, len(list)):
            if self.less(list[i], list[i-1]):
                return False
            return True
if __name__ == "__main__":
    example = Selection()
    list = [3,7,1,2,0]
    example.sort(list)
    assert example.is_sorted(list)
    example.show(list)