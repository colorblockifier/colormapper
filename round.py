import math
import os
from PIL import Image, ImageStat

input_folder = 'input'
output_folder = 'output'
texture_size = 16
background_width_blocks = 33

number_of_blocks = len(os.listdir(input_folder))

background_width_pixels = background_width_blocks * texture_size
composite_image = Image.new("RGBA", (background_width_pixels, background_width_pixels), (0, 0, 0, 0))

blocks = []

for filename in os.listdir(input_folder):
    path = os.path.join(input_folder, filename)
    img = Image.open(path).convert('RGBA')
    hue, sat, val = img.convert('HSV').split()
    # convert hue from 0.0 - 255.0 to 0.0 - 360.0
    average_hue = ImageStat.Stat(hue).mean[0] * (360 / 255)
    # convert saturation from 0.0 - 255.0 to 0.0 - 1.0
    average_sat = ImageStat.Stat(sat).mean[0] * (1 / 255)
    block_name = filename.split('.')[0]
    blocks.append({
        'name': block_name,
        'hue': average_hue,
        'sat': average_sat,
        'img': img
    })

for index, block in enumerate(blocks):
    print(block['hue'], block['sat'])

# place blocks in polar coordinates based on hue and saturation, with max radius of 1

# convert polar coordinates to cartesian and place based on pixel size of background image

# composite_image.save(f'{output_folder}/composite.png')
