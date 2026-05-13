import numpy as np
from .resize_image_bilinear import resize_image_bilinear
from .make_blocks_8x8 import make_blocks_8x8
from .block_full_pipeline import block_full_pipeline
from .DC_full_pipeline import DC_full_pipeline
from .AC_full_pipeline import AC_full_pipeline


def jpeg_transform(pixels: np.array, quality: int, color_space):

    number_of_colors = 1 if color_space in ('LLL', '111') else 3

    new_pixels_shape = list(np.ceil(np.array(pixels.shape[:2]) / 2).astype(np.int64))

    #print(new_pixels_shape)
    pixels = resize_image_bilinear(pixels, new_pixels_shape, color_space)

    blocks = make_blocks_8x8(pixels) - 128

    #print(blocks.shape)

    width, height = blocks.shape[:2]


    DCs = np.zeros([1, number_of_colors])
    ACs = np.zeros([63, number_of_colors])

    for x in range(height):
        for y in range(width):
            
            computed_block = block_full_pipeline(blocks[y][x], quality, color_space)
            
            if number_of_colors == 1:
                computed_block = computed_block[:, np.newaxis]

            DCs = np.vstack([DCs, computed_block[0:1, :]])
            ACs = np.vstack([ACs, computed_block[1:, :]])
    
    DCs = DCs[1:, :]
    ACs = ACs[64:, :]

    # print('DC', DCs.min(), DCs.max(), DCs.mean())
    # print('AC', ACs.min(), ACs.max(), ACs.mean())

    # global DCs_test
    # DCs_test = DCs

    #print(DCs.shape, ACs.shape)

    DCs_ready = DC_full_pipeline(DCs)
    ACs_ready = AC_full_pipeline(ACs)


    return DCs_ready, ACs_ready

    