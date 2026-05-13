import numpy as np
from .luminance_chrominance_tables import DC_luminance_table, DC_chrominance_table
from .DC_reading import DC_reading


def full_DC_reading(file_path: str, width: int, height: int, number_of_colors: int, start_position: int, start_bit: int):

    number_of_DCs = int(np.ceil(width / 8)) * int(np.ceil(height / 8))
    yuy = np.zeros([number_of_DCs, number_of_colors], dtype='object')

    DC_luminance_table_inverted = {v: k for k, v in DC_luminance_table.items()}
    DC_chrominance_table_inverted = {v_2: k_2 for k_2, v_2 in DC_chrominance_table.items()}

    place = (start_position, start_bit)

    counter = 0

    #print(number_of_DCs)
    #print(number_of_colors)

    for DC_index in range(number_of_DCs):
        for color in range(number_of_colors):
            counter += 1
            #print(counter)
            #print(place, color)
            try:
                if color == 0:
                    place, yuy[DC_index, color] = DC_reading(file_path, DC_luminance_table_inverted, place[0], place[1])
                else:
                    place, yuy[DC_index, color] = DC_reading(file_path, DC_chrominance_table_inverted, place[0], place[1])
            except TypeError:
                return (place, yuy, DC_index, color)
            if DC_index > 0:
                yuy[DC_index, color] += yuy[DC_index - 1, color]
    
    return (place, yuy)