class IterableWithGenerator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self.generator()

    def generator(self):
        for i in range(self.n):
            yield i
