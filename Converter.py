import sys
import os
from PIL import Image

"""
run script: python converter.py [directory of jpg file] [directory of png file]
example:  python converter.py ./Pokedex ./New-pokedex
"""
path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    clean_filename = os.path.splitext(filename)[0]
    img = Image.open(f"{path}/{filename}")
    img.save(f"{directory}/{clean_filename}.png", "png")
    print("all done!")
