from face_cropper import crop
import os

cage_folder = './data/cage/'
trump_folder = './data/trump/'
resized_folder = './cropped_data/'
new_cage_folder = './cropped_data/cage/'
new_trump_folder = './cropped_data/trump/'

try:
    os.mkdir(resized_folder)
    os.mkdir(new_cage_folder)
    os.mkdir(new_trump_folder)
except OSError:
    print("Directory already exist")

for i, filename in enumerate(os.listdir(cage_folder)):
    if filename.endswith(".jpg"):
        try:
            crop(cage_folder + filename, new_cage_folder)
        except:
            print("Found no face for image " + filename + " continuing...")
    else:
        continue

for i, filename in enumerate(os.listdir(trump_folder)):
    if filename.endswith(".jpg"):
        try:
            crop(trump_folder + filename, new_trump_folder)
        except:
            print("Found no face for image " + filename + " continuing...")
    else:
        continue
