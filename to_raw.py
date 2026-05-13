from modules.convert_to_raw import convert_to_raw
from modules.resize_image_bilinear import resize_image_bilinear
from PIL import Image
import numpy as np

# Лена
with Image.open('lena_color.tiff', mode='r') as lena_img:

    lena_img.show()
    convert_to_raw(lena_img, 'raw_images/lena_color.raw', 'icf')

# Цветное изображение
with Image.open('color_imag.jpg', mode='r') as color_img:

    color_img = color_img.resize([512,512])
    
    color_img.show()
    convert_to_raw(color_img, 'raw_images/color_img.raw', 'icf')

# Изображение в оттенках серого
gray_img = color_img.convert('L')
gray_img.show()
convert_to_raw(gray_img, 'raw_images/gray_img.raw', 'igs', 'LLL')


# Округлённое до чб изображние
wb_rounded_img = color_img.convert('1', dither=Image.Dither.NONE)
wb_rounded_img.show()
convert_to_raw(wb_rounded_img, 'raw_images/wb_rounded_img.raw', 'ibw', '111')


# Dithered изображение
wb_dithered_img = color_img.convert('1')
wb_dithered_img.show()
convert_to_raw(wb_dithered_img, 'raw_images/wb_dithered_img.raw', 'ibw', '111')
