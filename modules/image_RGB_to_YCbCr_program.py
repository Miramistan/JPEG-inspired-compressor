from .RGB_to_YCbCr_program import RGB_to_YCbCr_program
from PIL import Image

def image_RGB_to_YCbCr_program(img: Image, is_spaced = True):

    width, height = img.size
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            R, G, B = pixels[x, y]
        
            pixels[x, y] = RGB_to_YCbCr_program([R, G, B])
    
    return img
