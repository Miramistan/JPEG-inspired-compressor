import numpy as np


def RLE_AC(ACs: np.array):

    length = ACs.shape[0]

    result = np.array([0, 1])
    AC_index = 0

    cur_zeros = 0

    while AC_index < length:
        if ACs[AC_index] == 0:
            cur_zeros += 1
            AC_index += 1
            #print(AC_index, 0)

        else:
            #print(AC_index, 1)
            number_full_codes = cur_zeros // 16
            ostatok_code = cur_zeros % 16

            for i in range(number_full_codes):
                result = np.vstack((result, np.array([15, 0])))

            result = np.vstack((result, np.array([ostatok_code, ACs[AC_index]])))

            cur_zeros = 0
            AC_index += 1

    if cur_zeros != 0:
        result = np.vstack((result, np.array([0, 0])))

    return result[1:]