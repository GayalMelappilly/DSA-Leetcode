def transposeMatrix(matrix):
    transposedMatrix = []

    for col in range(len(matrix[0])):
        newRow = []

        for row in range(len(matrix)):
            newRow.append(matrix[row][col])

        transposedMatrix.append(newRow)

    return transposedMatrix
