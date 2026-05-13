import numpy as np


def diff_DC_encoding(DCs: np.array):

    new_DCs = np.zeros_like(DCs)
    new_DCs[0] = DCs[0]

    for DC_index in range(1, DCs.shape[0]):
        new_DCs[DC_index] = DCs[DC_index] - DCs[DC_index - 1]

    return new_DCs