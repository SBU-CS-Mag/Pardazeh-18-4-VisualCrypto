import random
from PIL import Image
import numpy as np


def encrypt(img: np.ndarray, full_pixel: int = 0) -> (np.ndarray, np.ndarray):
    """
    Function encrypts binary image (image contains only black and white pixels)

    :param image: Location of the image
    :return: two 2D numpy arrays which represent shares
    """
    height, width = img.shape

    full_pixel_share1 = [[[0, 255], [255, 0]], [[255, 0], [0, 255]], [[255, 0], [255, 0]], [[0, 255], [0, 255]]]
    full_pixel_share2 = [[[255, 0], [0, 255]], [[0, 255], [255, 0]], [[0, 255], [0, 255]], [[255, 0], [255, 0]]]

    empty_pixel_share1 = [[[0, 255], [255, 0]], [[255, 0], [0, 255]], [[255, 0], [255, 0]], [[0, 255], [0, 255]]]
    empty_pixel_share2 = [[[0, 255], [255, 0]], [[255, 0], [0, 255]], [[255, 0], [255, 0]], [[0, 255], [0, 255]]]

    encrypted1 = np.zeros((height * 2, width * 2), dtype=np.uint8)
    encrypted2 = np.zeros((height * 2, width * 2), dtype=np.uint8)

    for row in range(height):
        for column in range(width):
            if img[row][column] == full_pixel:
                i = random.randint(0, len(full_pixel_share1) - 1)
                share1 = full_pixel_share1[i]
                share2 = full_pixel_share2[i]
            else:
                i = random.randint(0, len(empty_pixel_share1) - 1)
                share1 = empty_pixel_share1[i]
                share2 = empty_pixel_share2[i]
            encrypted1[2 * row: 2 * row + 2, 2 * column: 2 * column + 2] = share1
            encrypted2[2 * row: 2 * row + 2, 2 * column: 2 * column + 2] = share2

    return encrypted1, encrypted2


random.seed(1001)
img = np.asarray(Image.open('flag.png').convert('L'))
e1, e2 = encrypt(img)
Image.fromarray(e1).save('1.png')
Image.fromarray(e2).save('2.png')