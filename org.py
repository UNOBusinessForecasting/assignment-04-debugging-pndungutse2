#si-matrix

class Matrix(object):
    def __init__(self, value=None, dim=(1, 1)):
        if value is None:
            value = []
        if isinstance(value, list):
            if len(value) > 0:
                if isinstance(value[0], (int, float)):
                    for i in value:
                        if not isinstance(i, (int, float)):
                            raise RuntimeError("Matrix is invalid. Please ensure that all elements are numeric (either float or int).")
                elif isinstance(value[0], list):
                    lenInner = len(value[0])
                    for row in value:
                        if len(row) != lenInner:
                            raise RuntimeError("Matrix is invalid. Please ensure that all rows have uniform length.")
                        for elem in row:
                            if not isinstance(elem, (int, float)):
                                raise RuntimeError("Matrix is invalid. Please ensure that all elements are numeric (either float or int).")
                else:
                    raise RuntimeError("Matrix is invalid. Unsupported data type.")
                self.value = value
                self.shape = (len(value), len(value[0]) if isinstance(value[0], list) else 1)
            else:
                matrix = [[1] * dim[1] for _ in range(dim[0])]
                self.value = matrix
                self.shape = dim
        else:
            raise TypeError("Matrix must be initialized with a list or left empty.")

    def __repr__(self):
        string = ""
        for i in range(self.shape[0]):
            string += "  [ "
            string += " ".join(str(self.value[i][j]) for j in range(self.shape[1]))
            string += " ]\n"
        return string + "\n"

mat = Matrix(dim = (3, 10))
print(mat)