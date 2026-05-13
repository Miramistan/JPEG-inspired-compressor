from modules.resize_image_bilinear import resize_image_bilinear
from modules.convert_to_raw import convert_to_raw
from PIL import Image
import numpy as np

#resize_list = ['lena_color', 'color_img', 'gray_img', 
resize_list = [               'wb_dithered_img', 'wb_rounded_img']


for image_name in resize_list:
    with open(f'raw_images/{image_name}.raw', 'rb') as file:
        file_type = file.read(3).decode('utf-8')
        color_space = file.read(3).decode('utf-8')
        width = int.from_bytes(file.read(2))
        height = int.from_bytes(file.read(2))
        data = file.read()

        print(file_type, color_space)

        if color_space == 'LLL' or color_space == '111':
            color_space_for_img = color_space[0]

        if color_space == 'RGB':
            color_space_for_img = color_space

        if color_space == 'YCC':
            color_space_for_img = 'YCbCr'

        test_img = Image.frombytes(color_space_for_img, [width, height], data)
        pixels = np.array(test_img)

        #print(pixels.dtype)

        # resized_pixels = resize_image_bilinear(pixels, [256, 256], color_space)
        # resized_pixels = resize_image_bilinear(resized_pixels, [512, 512], color_space)
        # resized_img = Image.fromarray(resized_pixels.astype(np.uint8), mode=color_space_for_img)

        #convert_to_raw(resized_img, f'raw_images/{image_name}_resized_new.raw', file_type, color_space=color_space)

        #resized_test_img = test_img.resize([512, 512])

        #convert_to_raw(resized_test_img, f'raw_images/{image_name}_resized_new.raw', file_type, color_space=color_space)


        test_img.show()