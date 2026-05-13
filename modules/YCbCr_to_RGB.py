import numpy as np


def YCbCr_to_RGB(YCbCr_colors):
    Y, Cb, Cr = YCbCr_colors
    
    R = int(np.round(1 * Y +       0 *  Cb        +   1.402 * (Cr - 128)))
    G = int(np.round(1 * Y - 0.34414 * (Cb - 128) - 0.71414 * (Cr - 128)))
    B = int(np.round(1 * Y +   1.772 * (Cb - 128) +       0 *  Cr))

    if R < 0:
        R = abs(R)
        if abs(R) > 25:
            print(R)
    if G < 0:
        G = abs(G)
        if abs(G) > 25:
            print(G)
    if B < 0:
        B = abs(B)
        if abs(B) > 25:
            print(B)

    if R > 255:
        R = 255
        if abs(R) > 256:
            print(R)
    if B > 255:
        B = 255
        if abs(B) > 256:
            print(B)
    if G > 255:
        G = 255
        if abs(G) > 256:
            print(G)

    return R.to_bytes(1) + G.to_bytes(1) + B.to_bytes(1)