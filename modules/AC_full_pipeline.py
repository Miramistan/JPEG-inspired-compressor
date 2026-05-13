import numpy as np
from .RLE_AC import RLE_AC
from .length_encoding import length_encoding
from .make_luminance_chrominance import make_AC_chrominance, make_AC_luminance, \
                                       make_DC_chrominance, make_DC_luminance


def AC_full_pipeline(ACs: np.array):

    #number_of_colors = 1 if len(ACs.shape) < 3 else ACs.shape[-1]

    number_of_colors = ACs.shape[-1]

    #print('AC_full_pipeline', ACs.shape)

    new_shape = list(ACs.shape)
    new_shape.append(3)

    full_length_RLE_ACs = np.zeros(new_shape)
    table_length_diff_ACs = np.zeros(ACs.shape, dtype=object)
    
    #print(diff_DCs)

    for color in range(number_of_colors):

        #print(ACs[:,color])

        RLE_ACs = RLE_AC(ACs[:, color])
        
        new_shape[0] = RLE_ACs.shape[0]
        new_shape[2] = 2
        length_RLE_ACs = np.zeros(new_shape)

        length_RLE_ACs[:, color] = np.array(length_encoding(RLE_ACs[:, 1], 'AC'))

        for i in range(length_RLE_ACs.shape[0]):
            #print(RLE_ACs.shape, length_RLE_ACs.shape)
            full_length_RLE_ACs[i, color, 0] = RLE_ACs[i, 0]
            full_length_RLE_ACs[i, color, 1:3] = length_RLE_ACs[i, color]

        #print(table_length_diff_DCs.shape)

        #print(full_length_RLE_ACs)

        for single_index in range(table_length_diff_ACs.shape[0]):
            single_sample = full_length_RLE_ACs[single_index][color]

            #print(single_sample, end = ' ')

            if single_sample[2] < 0:
                first = '0'
            else:
                first = '1'

            #print(single_sample[0], end=' ')

            if single_sample[1] == 0:
                table_length_diff_ACs[single_index][color] = \
                    (int(single_sample[0]), int(single_sample[1]), '')
                
            elif single_sample[1] == 1:
                table_length_diff_ACs[single_index][color] = \
                    (int(single_sample[0]), int(single_sample[1]), first)
            else:
                value = single_sample[2]
                if single_sample[2] < 0:
                    value = value + (2**single_sample[1] - 1)

                bits_value = np.binary_repr(int(abs(value)), int(single_sample[1]))

                #print(value, bits_value)

                table_length_diff_ACs[single_index][color] = \
                    (int(single_sample[0]), int(single_sample[1]), bits_value)
                
            single_sample = table_length_diff_ACs[single_index][color]

            #print(single_sample, end = ' ')

            if color == 0:
                table_length_diff_ACs[single_index][color] = \
                    make_AC_luminance(single_sample)
            else:
                table_length_diff_ACs[single_index][color] = \
                    make_AC_chrominance(single_sample)
                
    #print(table_length_diff_ACs)

    null_pattern = [('1010', ''), ('00', ''), ('00', '')]
    
    try:
        first_null = table_length_diff_ACs.tolist().index(null_pattern)
        unnulled_table_length_diff_ACs = table_length_diff_ACs[:first_null+1]

        #print(first_null)

        return unnulled_table_length_diff_ACs
    
    except ValueError:
        
        return table_length_diff_ACs
