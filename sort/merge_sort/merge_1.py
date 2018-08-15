class Merge():
    def merge(self, list, lo, mid, hi):
        i = lo
        j = mid + 1
        aux = {}
        for k in range(lo, hi + 1):
            aux[k] = list[k]
        for k in range(lo, hi + 1):
            if i > mid:
                list[k] = aux[j]
                j = j + 1
            elif j > hi:
                list[k] = aux[i]
                i = i + 1
            elif self.less(aux[j], aux[i]):
                list[k] = aux[j]
                j = j + 1
            else:
                list[k] = aux[i]
                i = i + 1

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
    example = Shell()
    list = [3, 7, 1, 2, 0, 9, 5, 6, 12, 11, 63, 56, 32]
    example.sort(list)
    assert example.is_sorted(list)
    example.show(list)