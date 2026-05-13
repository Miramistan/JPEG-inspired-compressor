import numpy as np
from .diff_DC_encoding import diff_DC_encoding
from .length_encoding import length_encoding
from .make_luminance_chrominance import make_AC_chrominance, make_AC_luminance, \
                                       make_DC_chrominance, make_DC_luminance


def DC_full_pipeline(DCs: np.array):

    number_of_colors = DCs.shape[-1]

    #print('DC_full_pipeline', DCs.shape)

    diff_DCs = diff_DC_encoding(DCs)

    #print(diff_DCs)
    #print(np.sum(diff_DCs == 0))

    new_shape = list(DCs.shape)
    new_shape.append(2)

    length_diff_DCs = np.zeros(new_shape)
    table_length_diff_DCs = np.zeros(DCs.shape, dtype=object)


    #print(diff_DCs)

    for color in range(number_of_colors):

        #print(diff_DCs[:, color])
        length_diff_DCs[:, color] = np.array(length_encoding(diff_DCs[:, color], 'DC'))

        #print(table_length_diff_DCs.shape)

        # global length_diff_DCs_test

        # length_diff_DCs_test = length_diff_DCs.copy()

        for single_index in range(table_length_diff_DCs.shape[0]):
            single_sample = length_diff_DCs[single_index][color]

            if single_sample[1] < 0:
                first = '0'
            else:
                first = '1'

            #print(single_sample[0], end=' ')

            if single_sample[0] == 0:
                table_length_diff_DCs[single_index][color] = \
                    (single_sample[0], '')
                
            elif single_sample[0] == 1:
                table_length_diff_DCs[single_index][color] = \
                    (single_sample[0], first)
            else:
                value = single_sample[1]
                if single_sample[1] < 0:
                    value = value + (2**single_sample[0] - 1)

                bits_value = np.binary_repr(int(abs(value)), int(single_sample[0]))

                #print(value, bits_value)

                table_length_diff_DCs[single_index][color] = \
                    (single_sample[0], bits_value)
                
            single_sample = table_length_diff_DCs[single_index][color]

            #print(single_sample, end = ' ')

            if color == 0:
                table_length_diff_DCs[single_index][color] = \
                    make_DC_luminance(single_sample)
            else:
                table_length_diff_DCs[single_index][color] = \
                    make_DC_chrominance(single_sample)
    
    return table_length_diff_DCs    
