class Insertion():
    def sort(self, list):
        n = len(list)
        for i in range(1, n):
            for j in range(i, -1, -1):
                if j > 0 and self.less(list[j], list[j-1]):
                    self.exch(list, j, j-1)

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
            if self.less(list[i], list[i - 1]):
                return False
            return True
if __name__ == "__main__":
    example = Insertion()
    list = [3, 7, 1, 2, 0, 9, 5, 6]
    example.sort(list)
    assert example.is_sorted(list)
    example.show(list)