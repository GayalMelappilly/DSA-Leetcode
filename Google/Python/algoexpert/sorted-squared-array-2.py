def sortedSqyaredArray(array):
    result = [0 for _ in array]

    smallIdx = 0
    largeIdx = len(array) - 1

    for idx in reversed(range(len(array))):

        smallVal = array[smallIdx]
        largeVal = array[largeIdx]

        if abs(smallVal) > abs(largeVal):
            result[idx] = smallVal ** 2
            smallIdx += 1

        else:
            result[idx] = largeVal ** 2
            largeIdx -= 1

    return result