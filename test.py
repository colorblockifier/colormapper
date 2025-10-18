import os
from PIL import Image, ImageStat

input_folder = 'input'

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

def sorter(list):
    return list['hue']

output_data.sort(key=sorter)

print(output_data)
