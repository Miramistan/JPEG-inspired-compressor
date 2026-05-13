import numpy as np


def FDCT_nxm_matrix(block: np.array):

    width, height = block.shape

    C = np.zeros([width, height])

    for i in range(width):
        for j in range(height):
            
            c_j = np.sqrt(1 / height) if j == 0 else np.sqrt(2 / height)

            C[i][j] = c_j * np.cos((2 * i + 1) * j * np.pi / 2 / width)

    S = np.dot(np.dot(C.T, block), C)

    return S