class Average(object):
    def __init__(self):
        self.total = 0
        self.count = 0

    def __call__(self, num):
        self.total += num
        self.count += 1
        return self.total / self.count
