from utils import read_image, write_image
import numpy as np


def salt_pap_noise(img, low, high):
    noise_matrix = np.random.randint(low, high, size=len(img))
    for i in range(len(img)):
        if noise_matrix[i] == low:
            img[i] = 0
        elif noise_matrix[i] == high - 1:
            img[i] = 255
    return img


if __name__ == '__main__':
    image_path = "/home/subhranil/image_new/09_logical_operators/alan.pgm"

    image_data = read_image(image_path)
    metadata = image_data["meta_data"]
    img_data = image_data["data"]
    w, h = map(int, metadata[-2].split(" "))

    write_image("output.pgm", metadata, salt_pap_noise(img_data, 0, 20))
