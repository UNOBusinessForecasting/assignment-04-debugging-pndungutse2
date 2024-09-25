class Matrix(object):
    """
    Read the matrix and store as part of the class object
    """

    def __init__(self, value=None, dim=(1, 1)):
        if value is None:
            value = []
        if isinstance(value, list):
            if len(value) > 0:
                if  type(value[0]) is int or type(value[0]) is float:
                     row = (int, float)
                else:
                    row = type(value[0])
                for i in value:
                    if not isinstance(i, (int, float, list)):
                        raise RuntimeError("Matrix is invalid. Please ensure that all elements share a type.")
                if row in list:
                    lenInner = len(value[0])
                    for i in value:
                        if len(i) != lenInner:
                            raise RuntimeError("Matrix is invalid. Please ensure that all rows have uniform length.")
                        for j in i:
                            if not isinstance(j, (int, float)):
                                raise RuntimeError("Matrix is invalid. Please ensure that all elements are numeric (either float or int).")
                self.value = value
                self.shape = (len(value), len(value[0]) if value else 0)

            try:
                self.shape = (len(value), len(value[0]))
            except:
                self.shape = (len(value), 1)
                matrix = []
                for i in range(dim[0]):
                    row = []
                    for j in range(dim[1]):
                        row.append(1)
                        matrix.append(row)

                    self.value = matrix
                    self.shape = dim

    """
    Print the matrix to screen
    """

    def __repr__(self):
        string = " "
        for i in range(self.shape[0]):
            if self.shape[1] > 1:
                string += "["
                string += " ".join(str(self.value[i][j]) for j in range(self.shape[1]))
                string += "]\n " if i < self.shape[0] - 1 else "]\n\n"
            else:
                string += "[" + str(self.value[i]) +"]\n  " if i < self.shape[0] - 1 else str(self.value[i]) + " "
        return string

mat = Matrix(dim=(10, 10))
print(mat)
#print(type(mat))