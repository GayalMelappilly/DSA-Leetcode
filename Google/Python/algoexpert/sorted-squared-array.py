def sortedSquaredarray(array):
    result = []

    for num in array:
        result.append(num**2)

    result.sort()

    return result