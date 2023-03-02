import numpy as np
from utils import read_image, write_image


def avg_filter(image_arr, start, filter_size=3):
    new_img = np.zeros_like(image_arr)
    for i in range(start, image_arr.shape[0] - start):
        for j in range(start, image_arr.shape[1] - start):
            new_img[i][j] = int(image_arr[i - start:i + filter_size - start, j - start:j + filter_size - start].mean())
    return new_img


def max_filter(image_arr, start, filter_size=3):
    new_img = np.zeros_like(image_arr)
    for i in range(start, image_arr.shape[0] - start):
        for j in range(start, image_arr.shape[1] - start):
            new_img[i][j] = int(image_arr[i - start:i + filter_size - start, j - start:j + filter_size - start].max())
    return new_img


def min_filter(image_arr, start, filter_size=3):
    new_img = np.zeros_like(image_arr)
    for i in range(start, image_arr.shape[0] - start):
        for j in range(start, image_arr.shape[1] - start):
            new_img[i][j] = int(image_arr[i - start:i + filter_size - start, j - start:j + filter_size - start].min())
    return new_img


def median_filter(image_arr, start, filter_size=3):
    new_img = np.zeros_like(image_arr)
    for i in range(start, image_arr.shape[0] - start):
        for j in range(start, image_arr.shape[1] - start):
            new_img[i][j] = int(np.median(
                image_arr[i - start:i + filter_size - start, j - start:j + filter_size - start]))
    return new_img


if __name__ == '__main__':
    image_path = "/home/subhranil/image_new/09_logical_operators/alan.pgm"

    image_data = read_image(image_path)
    metadata = image_data["meta_data"]
    img_data = image_data["data"]
    width, height = map(int, metadata[-2].split(" "))

    img_arr = np.array(img_data).reshape((height, width))

    filter_size = 3
    start = (filter_size - 1) // 2
    avg_filtered_image = avg_filter(img_arr, start, filter_size).flatten()
    max_filtered_image = max_filter(img_arr, start, filter_size).flatten()
    min_filtered_image = min_filter(img_arr, start, filter_size).flatten()
    median_filtered_image = median_filter(img_arr, start, filter_size).flatten()

    write_image("avg_filter_output.pgm", metadata, avg_filtered_image)
    write_image("max_filter_output.pgm", metadata, max_filtered_image)
    write_image("min_filter_output.pgm", metadata, min_filtered_image)
    write_image("median_filter_output.pgm", metadata, median_filtered_image)
