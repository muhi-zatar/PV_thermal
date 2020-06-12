import numpy as np
from PIL import Image

def load_cell_image(fname):
    with Image.open(fname) as image:
        return np.asarray(image, dtype='float32')


def normalize(image):
    return image/255.0
