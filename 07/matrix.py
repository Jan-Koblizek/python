class Matrix():
    """
    Class representing matrix
    """
    def __init__(self, values):
        super().__init__()
        self._values = values

    def __repr__(self):
        return self._values.__repr__()

    def __getitem__(self, item):
        return self._values[item]

    def __add__(self, other):
        mat_sum = []
        for i in range(len(self._values)):
            row = []
            for j in range(len(self._values[0])):
                row.append(self[i][j] + other[i][j])
            mat_sum.append(row)
        return Matrix(mat_sum)

    def __mul__(self, other):
        mat_sum = []
        for i in range(len(self._values)):
            row = []
            for j in range(len(self._values[0])):
                value = 0
                for k in range(len(self._values)):
                    value += self[i][k] * other[k][j]
                row.append(value)
            mat_sum.append(row)
        return Matrix(mat_sum)


mat1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat1 + mat2)
print(mat1 * mat2)
