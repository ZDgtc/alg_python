class Shell():
    def sort(self, list):
        n = len(list)
        h = 1
        while (h < n / 3):
            h = 3 * h + 1
        while (h >= 1):
            for i in range(h, n):
                for j in range(i, 0, -h):
                    if j >= h and self.less(list[j], list[j - h]):
                        self.exch(list, j, j-h)
            h = h / 3

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