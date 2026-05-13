import numpy as np
from .FDCT_nxm_matrix import FDCT_nxm_matrix
from .DCT_quantize import DCT_quantize
from .quantization_matrices import luminance_quant_matrix, chrominance_quant_matrix
from .zigzag_traversal import zigzag_traversal


def block_full_pipeline(block: np.array, quality: int, color_space):

    colors = 0 if color_space in ('LLL', '111') else 3

    # print('block_full_pipeline', colors)

    FDCT_matrix = np.zeros_like(block)

    if colors:
        for color in range(colors):
            FDCT_matrix[:, :, color] = FDCT_nxm_matrix(block[:, :, color])

        #print(FDCT_matrix)

        quantized_matrix = np.zeros_like(block)

        for color in range(colors):
            if color == 0:
                quantized_matrix[:, :, color] = DCT_quantize(FDCT_matrix[:, :, color],
                                                             luminance_quant_matrix, quality)
            else:
                quantized_matrix[:, :, color] = DCT_quantize(FDCT_matrix[:, :, color],
                                                             chrominance_quant_matrix, quality)
        
        #print(quantized_matrix)

        zigzag_data = np.zeros([64, 3])

        for color in range(colors):
            zigzag_data[:, color] = zigzag_traversal(quantized_matrix[:, :, color])

    else:
        FDCT_matrix = FDCT_nxm_matrix(block)

        quantized_matrix = DCT_quantize(FDCT_matrix, luminance_quant_matrix, quality)

        zigzag_data = zigzag_traversal(quantized_matrix)

    return zigzag_data