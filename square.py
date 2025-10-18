import math
import os
from PIL import Image, ImageStat

input_folder = 'input'
output_folder = 'output'
texture_size = 16

number_of_blocks = len(os.listdir(input_folder))
background_width_blocks = math.ceil(math.sqrt(number_of_blocks))
background_width_pixels = background_width_blocks * texture_size
composite_image = Image.new("RGBA", (background_width_pixels, background_width_pixels), (0, 0, 0, 0))

blocks = []

for filename in os.listdir(input_folder):
    path = os.path.join(input_folder, filename)
    img = Image.open(path).convert('RGBA')
    h, s, v = img.convert('HSV').split()
    average_hue = ImageStat.Stat(h).mean[0]
    block_name = filename.split('.')[0]
    blocks.append({
        'name': block_name,
        'hue': average_hue,
        'image': img
    })

blocks.sort(key=(lambda x: x['hue']))

for index, block in enumerate(blocks):
    img = block['image']
    col_blocks = index % background_width_blocks
    row_blocks = math.floor(index / background_width_blocks)
    col_pixels = col_blocks * texture_size
    row_pixels = row_blocks * texture_size
    composite_image.paste(img, (col_pixels, row_pixels), img)

composite_image.save(f'{output_folder}/square.png')
