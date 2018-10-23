
class Identity_Numbers:
    def __iter__(self):
        self.id = 1
        return self

    def __next__(self):
        id = self.id
        self.id += 1
        return id