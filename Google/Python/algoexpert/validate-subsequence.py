def isValidsubsequence(array,sequence):
    main = 0
    sub = 0

    if len(sequence) > len(array):
        return False

    while main < len(array) and sub < len(sequence):
        if array[main] == sequence[sub]:
            main += 1
            sub += 1

        else:
            main += 1

    return sub == len(sequence)