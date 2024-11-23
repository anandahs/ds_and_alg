def rotate_matrix1(matrix):
    matrix = matrix[::-1]

    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"original_matrix:{matrix}")
    print(f"rotated_matrix:{rotate_matrix(matrix)}")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"rotated_matrix:{rotate_matrix1(matrix)}")
