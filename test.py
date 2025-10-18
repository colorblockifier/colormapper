import math
import os
from PIL import Image, ImageStat

input_folder = 'input'
output_folder = 'output'
texture_size = 16

number_of_textures = len(os.listdir(input_folder))
background_size = math.ceil(math.sqrt(number_of_textures)) * texture_size
print(background_size)
background_image = Image.new("RGBA", (background_size, background_size), (0, 0, 0, 0))

output_data = []

def get_average_hue(filename):
    img = Image.open(filename).convert('RGB').convert('HSV')
    h, s, v = img.split()
    return ImageStat.Stat(h).mean[0]

for filename in os.listdir(input_folder):
    path = os.path.join(input_folder, filename)
    hue = get_average_hue(path)
    output_data.append({
        'filename': filename,
        'hue': hue
    })

background_image.save(f'{output_folder}/composite.png')

output_data.sort(key=(lambda x: x['hue']))

print(output_data)
