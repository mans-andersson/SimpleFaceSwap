import numpy as np
import os
from PIL import Image

# Generating numpy array format from folder with .jpgs
# https://stackoverflow.com/questions/50772128/pytorch-handling-picutres-and-jpeg-files-beginners-questions
def load_image(infilename):
    """This function loads an image into memory when you give it
       the path of the image
    """
    img = Image.open(infilename)
    img.load()
    data = np.asarray(img, dtype="float64")
    return data

def create_npy_from_image(images_folder, output_name, num_images, image_dim):
    """Loops through the images in a folder and saves all of them
       as a numpy array in output_name
    """
    image_matrix = np.empty((num_images, image_dim, image_dim, 3), dtype=np.float64)
    for i, filename in enumerate(os.listdir(images_folder)):
        if filename.endswith(".jpg"):
            data = load_image(images_folder + filename)
            image_matrix[i] = data
        else:
            continue
    np.save(output_name, image_matrix)

DIM = 64 # The images have the size 256x256
CAGE_SIZE = 306 # Number of Cage images
TRUMP_SIZE = 315 # Number of Trump images
create_npy_from_image("./resized_data/cage/", "cage.npy", CAGE_SIZE, DIM)
create_npy_from_image("./resized_data/trump/", "trump.npy", TRUMP_SIZE, DIM)