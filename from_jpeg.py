import numpy as np
from PIL import Image
from modules import *


def from_jpeg(jpeg_path: str):
    with open(jpeg_path, 'rb') as file:
        
        file_type = file.read(3)
        color_space = file.read(3)
        if color_space == b'YCC' or color_space == b'RGB':
            number_of_colors = 3
        if color_space == b'LLL' or color_space == b'111':
            number_of_colors = 1

        print(file_type, color_space)

        width = int.from_bytes(file.read(2))
        height = int.from_bytes(file.read(2))

        resized_width = np.ceil(width / 2).astype(np.int64)
        resized_height = np.ceil(height / 2).astype(np.int64)
        
        q_table_type = file.read(2) # 'ST'
        if q_table_type == b'ST':
            quality = int.from_bytes(file.read(1))
        h_table_type = file.read(2) # 'ST'
        
        blocks_count = int(np.ceil(resized_width / 8)) * int(np.ceil(resized_height / 8))
        #print(blocks_count)
        
        try:
            place, DCs = full_DC_reading(jpeg_path, resized_width, resized_height, number_of_colors, 15, 128)
            place, ACs = full_AC_reading(jpeg_path, resized_width, resized_height, number_of_colors, place[0], place[1])
        except Exception as e:
            return full_DC_reading(jpeg_path, resized_width, resized_height, number_of_colors, 15, 128)

    

    output_img = np.zeros((resized_height, resized_width, 3), dtype=np.float64)
    
    block_idx = 0
    for i in range(0, resized_height, 8):
        for j in range(0, resized_width, 8):
            block_64 = np.zeros([64, 3])
            block_64[0] = DCs[block_idx]
            block_64[1:] = ACs[block_idx]

            block_2d = np.zeros([8, 8, 3])
            reconstructed_block = np.zeros([8, 8, 3])
                
            for color in range(number_of_colors):
                block_2d[:, :, color] = inverse_zigzag(block_64[:, color])
                
                if color == 0:
                    block_2d[:, :, color] = DCT_normalize(block_2d[:, :, color], luminance_quant_matrix, quality)
                else:
                    block_2d[:, :, color] = DCT_normalize(block_2d[:, :, color], chrominance_quant_matrix, quality)

                #print(block_2d.min(), block_2d.max(), block_2d.mean())
                
                reconstructed_block[:, :, color] = IDCT_nxm_matrix(block_2d[:, :, color])

            in_block_shape = output_img[j:j+8, i:i+8].shape

            #if j > width - 16:
            #    print(in_block_shape, reshaped_block.shape)
                
            output_img[j:j+8, i:i+8] = reconstructed_block[:in_block_shape[0], :in_block_shape[1], :] + 128
            #output_img[j:j+8, i:i+8] = reconstructed_block + 128
            block_idx += 1
    
    # print(output_img.max(), output_img.min(), output_img.mean())

    output_img = resize_image_bilinear(output_img, [width, height], 'YCC')

    #img_uint8 = np.clip(output_img, 0, 255).astype(np.uint8)
    img_uint8 = output_img.astype(np.uint8)
    img_out = Image.fromarray(img_uint8, 'YCbCr')
    return img_out