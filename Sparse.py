# This is a simple Sparse Matrix class
class SM:
    def __init__(self, r, c):
        self.r = r  # rows
        self.c = c  # cols
        self.d = {}  # data in dictionary

    def set(self, i, j, v):
        # Set value v at row i, col j
        if v != 0:
            self.d[(i, j)] = v
        elif (i, j) in self.d:
            del self.d[(i, j)]  # remove if zero

    def get(self, i, j):
        # Get value at row i, col j
        return self.d.get((i, j), 0)

    def items(self):
        # Get all non-zero values
        return self.d.items()
