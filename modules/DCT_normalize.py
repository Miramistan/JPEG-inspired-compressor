import numpy as np


def DCT_normalize(DCT_matrix: np.array, quantize_matrix: np.array, quality: int):
    if quality < 50:
        scale = 5000 / quality
    else:  
        scale = 200 - 2 * quality

    quantize_matrix = np.ceil(np.array(quantize_matrix) * scale / 100)
        
    return DCT_matrix * quantize_matrix