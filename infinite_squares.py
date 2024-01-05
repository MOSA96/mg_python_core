class InfiniteSquareIterator:
    def __init__(self):
        self.number = 1 

    def __iter__(self):
        return self

    def __next__(self):
        result = self.number ** 2
        self.number += 1
        return result

squares = InfiniteSquareIterator()
for i in range(10):
    print(next(squares))
