import numpy


def diagonal_sum(matrix):
    total = 0

    # data = range(len(matrix))

    for i in range(len(matrix)):
        total += matrix[i][i]

    return total


if __name__ == "__main__":
    matrix = numpy.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
    print(matrix)
    matrix = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    print(diagonal_sum(matrix))
