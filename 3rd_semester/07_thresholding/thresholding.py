from utils import read_image, write_image
from tqdm import tqdm
import numpy as np


def threshold(img_data, threshold_value):
    new_img = [255 if i > threshold_value else 0 for i in tqdm(img_data)]
    return new_img


def tsm(img_arr, eps=1e-6, m1=0, m2=0):
    t = np.mean(img_arr)

    new_t = 0
    while abs(new_t - t) < eps:
        g1 = img_arr[img_arr > t]
        g2 = img_arr[img_arr <= t]

        m1 = np.mean(g1) if len(g1) else m1
        m2 = np.mean(g2) if len(g2) else m2

        new_t = (m1 + m2) / 2
        t = new_t
    return t


def otsu_threshold(img_arr):
    hist = np.histogram(img_arr, bins=256, range=(0, 255))[0]
    hist = hist / hist.sum()
    csum = np.cumsum(hist)
    csum_sq = np.cumsum(np.power(hist, 2))
    csum_xy = np.cumsum(hist * np.arange(256))
    mean = csum_xy[-1] / csum[-1]
    max_var_bt = 0
    t = 0

    for i in range(1, 256):

        p0, p1 = csum[i], 1 - csum[i]
        m0 = csum_xy[i] / p0 if p0 != 0 else np.finfo(float).eps
        m1 = (csum_xy[-1] - csum_xy[i]) / p1 if p1 != 0 else np.finfo(float).eps

        var_bt = p0 * (m0 - mean) ** 2 + p1 * (m1 - mean) ** 2

        if var_bt > max_var_bt:
            max_var_bt = var_bt
            t = i

    return t


if __name__ == '__main__':
    image_path = "/home/subhranil/image_new/07_thresholding/z.pgm"

    image_data = read_image(image_path)
    metadata = image_data["meta_data"]
    img_width, img_height = map(int, metadata[-2].split(" "))
    img_data = np.array(image_data["data"]).reshape((img_height, img_width))

    # threshold_img = threshold(image_data["data"], 200)
    print(tsm(img_data))

    print(otsu_threshold(img_data))

    write_image("tsm_modified_image.pgm", metadata, threshold(image_data["data"], tsm(img_data)))
    write_image("otsu_modified_image.pgm", metadata, threshold(image_data["data"], otsu_threshold(img_data)))
