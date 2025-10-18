import os
from PIL import Image, ImageStat

input_folder = 'input'

def print_average_hue(filename):
    img = Image.open(filename).convert('RGB').convert('HSV')
    h, s, v = img.split()
    average_hue = ImageStat.Stat(h).mean[0]

    print(filename, average_hue)

for filename in os.listdir(input_folder):
    path = os.path.join(input_folder, filename)
    print_average_hue(path)
