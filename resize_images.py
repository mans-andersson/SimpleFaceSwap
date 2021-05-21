# Resize images, making them smaller makes training easier
# Original size 256x256 new size 64x64
# https://opensource.com/life/15/2/resize-images-python
from PIL import Image
import os

basewidth = 64
cage_folder = './cropped_data/cage/'
trump_folder = './cropped_data/trump/'
resized_folder = './resized_data/'
new_cage_folder = './resized_data/cage/'
new_trump_folder = './resized_data/trump/'

try:
    os.mkdir(resized_folder)
    os.mkdir(new_cage_folder)
    os.mkdir(new_trump_folder)
except OSError:
    print("Directory already exist")

for i, filename in enumerate(os.listdir(cage_folder)):
    if filename.endswith(".jpg"):
        img = Image.open(cage_folder + filename)
        # wpercent = (basewidth / float(img.size[0]))
        # hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, basewidth), Image.ANTIALIAS)
        img.save(new_cage_folder + filename)
    else:
        continue

for i, filename in enumerate(os.listdir(trump_folder)):
    if filename.endswith(".jpg"):
        img = Image.open(trump_folder + filename)
        # wpercent = (basewidth / float(img.size[0]))
        # hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, basewidth), Image.ANTIALIAS)
        img.save(new_trump_folder + filename)
    else:
        continue