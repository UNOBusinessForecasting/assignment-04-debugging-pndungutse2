class Matrix(object):
    """
    Class to store and represent a matrix.
    """

    def __init__(self, value=None, dim=(1, 1)):
        if value is None:
            # If no value provided, create a matrix of ones with given dimensions
            self.value = [[1 for _ in range(dim[1])] for _ in range(dim[0])]
            self.shape = dim
        elif isinstance(value, list):
            if len(value) > 0:
                if isinstance(value[0], (int, float)):
                    # Value is a vector (single-column matrix)
                    for i in value:
                        if not isinstance(i, (int, float)):
                            raise RuntimeError(
                                "Matrix is invalid. Please ensure all elements are numeric (int or float).")
                    self.value = [[i] for i in value]
                    self.shape = (len(value), 1)
                elif isinstance(value[0], list):
                    # Value is a 2D matrix
                    row_len = len(value[0])
                    for row in value:
                        if len(row) != row_len:
                            raise RuntimeError("Matrix is invalid. Ensure all rows have the same length.")
                        for elem in row:
                            if not isinstance(elem, (int, float)):
                                raise RuntimeError("Matrix is invalid. Ensure all elements are numeric (int or float).")
                    self.value = value
                    self.shape = (len(value), row_len)
                else:
                    raise RuntimeError("Matrix is invalid. Unsupported data structure.")
            else:
                raise RuntimeError("Matrix is invalid. Empty list provided.")
        else:
            raise RuntimeError("Matrix is invalid. Unsupported data structure.")

    def __repr__(self):
        """
        Print the matrix to screen
        """
        result = ""
        for row in self.value:
            result += "[ " + " ".join(map(str, row)) + " ]\n"
        return result
