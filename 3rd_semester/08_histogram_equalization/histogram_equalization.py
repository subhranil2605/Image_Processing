from utils import read_image, write_image
import matplotlib.pyplot as plt
import numpy as np
from itertools import accumulate


def get_histograms(img_data):
    l = len(img_data)

    hists = {i: img_data.count(i) for i in set(img_data)}
    norm_hists = {key: value / l for key, value in hists.items()}
    return {"histogram": hists, "norm_histogram": norm_hists}


def get_counts_numpy(img_data, w, h):
    img_arr = np.array(img_data).reshape((h, w))
    unique, counts = np.unique(img_arr, return_counts=True)
    hists = dict(zip(unique, counts))
    norm_hists = {key: value / img_arr.size for key, value in hists.items()}
    return hists, norm_hists


def plot_histograms(hist: dict):
    plt.bar(hist.keys(), hist.values())
    plt.show()


def histogram_eq(hist):
    values = list(accumulate(hist.values()))
    values = [round(i) for i in values]

    h_eq = {}
    for key, val in zip(hist.keys(), values):
        h_eq[key] = val
    return h_eq


if __name__ == '__main__':
    image_path = "/home/subhranil/image_new/02_negative/alan.pgm"

    image_data = read_image(image_path)
    metadata = image_data["meta_data"]

    # img_w, img_h = map(int, metadata[-2].split(" "))
    # print(get_counts_numpy(image_data["data"], img_w, img_h))

    norm_hist = get_histograms(image_data["data"])["norm_histogram"]
    hist_eq = histogram_eq(norm_hist)

    plot_histograms(norm_hist)
    plot_histograms(hist_eq)

    plt.show()

