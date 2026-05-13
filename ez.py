from to_jpeg import to_jpeg
from from_jpeg import from_jpeg

images_list = ['lena_color', 'color_img', 'gray_img', 
               'wb_dithered_img', 'wb_rounded_img']

images_list_2 = ['wb_dithered_img', 'wb_rounded_img']

for image_name in images_list:

    for quality in range(5, 100, 10):
        to_jpeg(f'raw_images/{image_name}.raw',
                f'jpeged_images/{image_name}_{quality}.jpeg', quality)

        img = from_jpeg(f'jpeged_images/{image_name}_{quality}.jpeg')

        img.save(f'saved_images/{image_name}_{quality}.jpg')

    #img.show()