import numpy as np


def zigzag_traversal(matrix: np.array):

    width, height = matrix.shape[:2]

    result = np.array([])

    start_position_even = min(0, height - width) - min(height, width) + 1
    start_position_odd =  max(0, height - width) + min(height, width) - 1

    for traversal_turn in range(max(width, height) + min(width, height)):

        #print(result, traversal_turn)

        if traversal_turn % 2 == 0:
            result = np.concatenate((result, 
                     np.flipud(matrix).diagonal(start_position_even + traversal_turn)))
        else:
            result = np.concatenate((result, 
                     np.fliplr(matrix).diagonal(start_position_odd - traversal_turn)))
            
    return result

    