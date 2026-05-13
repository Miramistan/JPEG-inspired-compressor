import numpy as np


def resize_image_bilinear(pixels: np.array, new_size: list, color_space: str):

    height, width = pixels.shape[:2]

    #print(width, height)

    new_width, new_height = new_size

    s_x, s_y = width / new_width, height / new_height

    pixels = pixels.astype(np.float64)

    if color_space == 'RGB' or color_space == 'YCC':
        new_pixels = np.zeros([new_height, new_width, 3], dtype=np.float64)
        pad_shape = ((1, 1), (1, 1), (0, 0))
    if color_space == 'LLL' or color_space == '111':
        new_pixels = np.zeros([new_height, new_width], dtype=np.float64)
        pad_shape = ((1, 1), (1, 1))

    #print(new_pixels[0][0])

    pixels = np.pad(pixels, pad_shape, mode='edge')

    #print(pixels.shape)

    x_arr = []
    y_arr = []

    #print(pixels[0][0])

    for x_new in range(new_width):
        for y_new in range(new_height):

            x_old = (x_new + 0.5) * s_x - 0.5 + 1
            y_old = (y_new + 0.5) * s_y - 0.5 + 1

            x_arr.append(x_old)
            y_arr.append(y_old)

            x0 = int(np.floor(x_old))
            y0 = int(np.floor(y_old))
            
            x0 = max(0, min(x0, height))
            y0 = max(0, min(y0, width))
            x1 = min(x0 + 1, height)
            y1 = min(y0 + 1, width)

            wa = x_old - x0
            wb = y_old - y0

            p00 = pixels[y0, x0]
            p10 = pixels[y0, x1]
            p01 = pixels[y1, x0]
            p11 = pixels[y1, x1]

            value = (p00 * (1 - wa) * (1 - wb) +
                    p10 * wa * (1 - wb) +
                    p01 * (1 - wa) * wb +
                    p11 * wa * wb)

            #value = bilinear_interpolation([x0, x1], [y0, y1], [[p00, p10], [p01, p11]], wa, wb)

            new_pixels[y_new, x_new] = value

    #print(max(x_arr), min(x_arr))
    #print(max(y_arr), min(y_arr))
    
    return new_pixels