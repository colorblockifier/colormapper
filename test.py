import math
import os
from PIL import Image, ImageStat

input_folder = 'input'
output_folder = 'output'
texture_size = 16

number_of_textures = len(os.listdir(input_folder))
background_size = math.ceil(math.sqrt(number_of_textures)) * texture_size
composite_image = Image.new("RGBA", (background_size, background_size), (0, 0, 0, 0))

textures = []

for filename in os.listdir(input_folder):
    path = os.path.join(input_folder, filename)
    img = Image.open(path).convert('RGBA')
    h, s, v = img.convert('HSV').split()
    average_hue = ImageStat.Stat(h).mean[0]
    texture_name = filename.split('.')[0]
    textures.append({
        'name': texture_name,
        'hue': average_hue,
        'image': img
    })

textures.sort(key=(lambda x: x['hue']))

for texture in textures:
    composite_image.paste(texture['image'], (0, 0), texture['image'])

composite_image.save(f'{output_folder}/composite.png')

# print(textures)
