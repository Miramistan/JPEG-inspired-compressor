import numpy as np
from PIL import Image
from modules import *

def to_jpeg(file_path: str, to_file_path: str, quality: int, quantize_table = 'standard', huffman_table = 'standard'):

    with open(file_path, 'rb') as file:
        file_type = file.read(3)
        color_space = file.read(3).decode('utf-8')
        if color_space == 'LLL' or color_space == '111':
            number_of_colors = 1
            color_space_for_img = color_space[0]
        if color_space == 'RGB' or color_space == 'YCC':
            number_of_colors = 3
            color_space_for_img = color_space

        print(color_space)
        
        width = int.from_bytes(file.read(2))
        height = int.from_bytes(file.read(2))
        data = file.read()


        img = Image.frombytes(color_space_for_img, [width, height], data)


        if color_space == 'RGB':
            img = image_RGB_to_YCbCr_program(img)
            color_space = 'YCC'

        pixels = np.array(img)


        DCs, ACs = jpeg_transform(pixels, quality, color_space)

        with open(to_file_path, 'wb') as output_file:
            
            output_file.write(bytearray('jpg' + color_space, 'utf-8'))
            output_file.write(width.to_bytes(2))
            output_file.write(height.to_bytes(2))

            if quantize_table == 'standard':
                output_file.write(bytearray('ST', 'utf-8'))
                output_file.write(quality.to_bytes(1))
            else:
                output_file.write(bytearray("NW", 'utf-8'))
                # Запись таблицы

            if huffman_table == 'standard':
                output_file.write(bytearray("ST", 'utf-8'))
            else:
                output_file.write(bytearray("NW", 'utf-8'))
                # Запись таблицы

            bits = ''

            for DC in DCs:
                for color in range(number_of_colors):
                    bits += ''.join(DC[color])

            # print(ACs.shape)
            # print(ACs[:10])
        
            for AC in ACs:
                for color in range(number_of_colors):
                    bits += ''.join(AC[color])

                bits += '10100000'

            #print(len(bits))
            #print(len(bitstring_to_bytes(bits)))

            output_file.write(bitstring_to_bytes(bits))