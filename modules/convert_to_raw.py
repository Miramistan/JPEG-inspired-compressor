from PIL import Image


def convert_to_raw(image: Image, file_name, meta_data, color_space = 'RGB'):
    meta_data = bytearray(meta_data, 'utf-8')
    color_space = bytearray(color_space, 'utf-8')
    width = image.width.to_bytes(2)
    height = image.height.to_bytes(2)
    bytes = image.tobytes()

    file_bytes = meta_data + color_space + width + height + bytes
    
    with open(file_name, 'wb') as file:
        file.write(file_bytes)

    return file_bytes

if __name__ == "__main__":

    # Лена
    with Image.open('lena_color.tiff', mode='r') as lena_img:

        #lena_img.show()
        convert_to_raw(lena_img, 'raw_images/lena_color.raw', 'icf')

    # Цветное изображение
    with Image.open('color_imag.jpg', mode='r') as color_img:

        #print(len(color_img.tobytes()))
        convert_to_raw(color_img, 'raw_images/color_img.raw', 'icf')

    # Изображение в оттенках серого
    gray_img = color_img.convert('L')
    #gray_img.show()
    convert_to_raw(gray_img, 'raw_images/gray_img.raw', 'igs', 'LLL')


    # Округлённое до чб изображние
    wb_rounded_img = color_img.convert('1', dither=Image.Dither.NONE)

    wb_rounded_img.show()
    print(len(wb_rounded_img.tobytes()))

    convert_to_raw(wb_rounded_img, 'raw_images/wb_rounded_img.raw', 'ibw', '111')


    # Dithered изображение
    wb_dithered_img = color_img.convert('1')

    wb_dithered_img.show()

    convert_to_raw(wb_dithered_img, 'raw_images/wb_dithered_img.raw', 'ibw', '111')
    

