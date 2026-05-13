import numpy as np


def make_blocks_8x8(pixels: np.array):

    width, height = pixels.shape[:2]
    new_width, new_height = int(np.ceil(width / 8)), int(np.ceil(height / 8))
    new_shape = [new_width, new_height]

    if pixels.shape[-1] == 3:
        new_block_shape = [8, 8, 3]
    else:
        new_block_shape = [8, 8]
    
    new_shape.extend(new_block_shape)
    
    blocks = np.zeros(new_shape)

    for new_y in range(new_height):
        for new_x in range(new_width):
            
            block = pixels[new_x * 8 : (new_x + 1) * 8, new_y * 8 : (new_y + 1) * 8]

            if block.shape != new_block_shape:
                diff_shape = np.array(new_block_shape) - np.array(block.shape)
                diff_shape = [[0, x] for x in diff_shape]

                block = np.pad(block, diff_shape, mode='mean')
            
            blocks[new_x][new_y] = block
    
    return blocks