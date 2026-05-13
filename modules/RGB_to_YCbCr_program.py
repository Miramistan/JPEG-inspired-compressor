import numpy as np


def RGB_to_YCbCr_program(RGB_colors):
    R, G, B = RGB_colors
    
    Y  = int(np.round(   0.299 * R +  0.587 * G +  0.114 * B))
    Cb = int(np.round(- 0.1687 * R - 0.3313 * G +    0.5 * B + 128))
    Cr = int(np.round(     0.5 * R - 0.4187 * G - 0.0813 * B + 128))

    return (Y, Cb, Cr)