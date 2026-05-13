import numpy as np


def length_encoding(numbers_array: np.array, AC_or_DC: str):
    
    result = [[0, 0] for _ in range(numbers_array.shape[0])]

    for i, number in enumerate(numbers_array):
        if number == 0:
            #print(number, 0)
            result[i] = [0, 0]
        else:
            category = (np.floor(np.log2(abs(number))) + 1).astype(np.int64)
            if AC_or_DC == 'AC':
                result[i] = [category, number]
            if AC_or_DC == 'DC':
                result[i] = [category, number]
            #print(number, category, int(number).to_bytes(int(np.ceil(category / 8))))

    return result