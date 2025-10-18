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
    # normalize saturation from 0.0 - 255.0 to 0.0 - 1.0
    average_sat = ImageStat.Stat(sat).mean[0] * (1 / 255)
    block_name = filename.split('.')[0]
    blocks.append({
        'name': block_name,
        'hue': average_hue,
        'sat': average_sat,
        'img': img
    })

for block in blocks:
    img = block['img']
    # get polar coordinates
    r = block['sat']
    theta = block['hue']
    # convert polar coordinates to cartesian
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    # normalize -1.0 - 1.0 to 0.0 - 1.0
    x = (x - -1) / (1 - -1)
    y = (y - -1) / (1 - -1)
    # multiply cartesian coordinates based on image size
    x = x * background_width_pixels
    y = y * background_width_pixels
    # correct for placing based on center of texture instead of top left
    x = x - texture_size / 2
    y = y - texture_size / 2
    # convert float to int
    x = math.floor(x)
    y = math.floor(y)
    # paste image onto background image in position corresponding to colors
    composite_image.paste(img, (x, y), img)

composite_image.save(f'{output_folder}/round.png')
