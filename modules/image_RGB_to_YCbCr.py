from RGB_to_YCbCr import RGB_to_YCbCr


def image_RGB_to_YCbCr(file_path: str, is_spaced = True):

    with open(file_path, 'rb') as file:
        file_type = file.read(3)
        if file_type != b'icf':
            print("Не цветной файл!")
            return 0

        if is_spaced:
            color_space = file.read(3)

        width = file.read(2)
        height = file.read(2)

        pixel = file.read(3)

        with open(file_path[:-4] + '_YCbCr.raw', mode='wb') as output_file:
            
            output_file.write(file_type + bytearray('YCC', 'utf-8') + width + height)

            while pixel:
                output_file.write(RGB_to_YCbCr(pixel))

                pixel = file.read(3)

            
    
    return 1
