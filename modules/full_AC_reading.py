import numpy as np
from .luminance_chrominance_tables import AC_luminance_table, AC_chrominance_table
from .AC_reading import AC_reading


def full_AC_reading(file_path: str, width: int, height: int, number_of_colors: int, start_position: int, start_bit: int):

    number_of_ACs = int(np.ceil(width / 8)) * int(np.ceil(height / 8))
    yuy = np.zeros([number_of_ACs, 63, number_of_colors], dtype='object')
    yuy_result = np.zeros_like(yuy)

    AC_luminance_table_inverted = {v: k for k, v in AC_luminance_table.items()}
    AC_chrominance_table_inverted = {v: k for k, v in AC_chrominance_table.items()}

    place = (start_position, start_bit)
    end_flag = False

    for j in range(number_of_ACs):
        for i in range(63):
            for color in range(number_of_colors):
                yuy[j, i, color] = (0, 0)

    skip_color = []


    for AC_block_index in range(number_of_ACs):
        for AC_index in range(63):
            for color in range(number_of_colors):
                if color in skip_color:
                    continue

                if color == 0:
                    place, yuy[AC_block_index, AC_index, color] = AC_reading(file_path, AC_luminance_table_inverted, place[0], place[1])
                else:
                    place, yuy[AC_block_index, AC_index, color] = AC_reading(file_path, AC_chrominance_table_inverted, place[0], place[1])


                if yuy[AC_block_index, AC_index, color] == (0, 0):
                    #print('PIZDEC')
                    skip_color.append(color)
                    end_flag = True
                    break
            
            if end_flag:
                break
        if end_flag:
            break

    for AC_block_index in range(number_of_ACs):
        for color in range(number_of_colors):

            AC_pair = yuy[AC_block_index, 0, color]
            AC_index = 0
            AC_index_old = 0

            while AC_index < 63:

                AC_pair = yuy[AC_block_index, AC_index_old, color]
                #print(AC_index, '###')

                for _ in range(AC_pair[0]):
                    yuy_result[AC_block_index, AC_index, color] = 0
                    AC_index += 1

                #print(AC_index, AC_index_old, yuy[AC_block_index, AC_index_old, color])


                yuy_result[AC_block_index, AC_index, color] = AC_pair[1]
                AC_index += 1
                AC_index_old += 1
    
    return (place, yuy_result)