import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


def read_image(img_path):
    with open(img_path) as f_obj:
        data = [x.strip() for x in f_obj.readlines()]

    meta_data = data[:4]
    data = list(map(int, data[4:]))

    return {"meta_data": meta_data, "data": data}


def write_image(image_name, meta_data, data):
    with open(image_name, "w") as f_obj:
        [f_obj.write(x + "\n") for x in meta_data]

        [f_obj.write(str(x) + "\n") for x in data]


def transform_negative(data):
    max_value = max(data)
    return [max_value - i for i in tqdm(data)]


if __name__ == '__main__':
    image_path = "/home/subhranil/image_new/02_negative/alan.pgm"
    img_data = read_image(image_path)
    meta_data = img_data["meta_data"]
    image_width, image_height = list(map(int, meta_data[2].split(" ")))

    neg_image_data = transform_negative(img_data["data"])
    write_image("alan_neg.pgm", meta_data, neg_image_data)

    arr = np.array(img_data["data"]).reshape((image_height, image_width))
    neg_arr = np.array(neg_image_data).reshape((image_height, image_width))

    plt.subplot(1, 2, 1)
    plt.imshow(arr, cmap='gray')
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(neg_arr, cmap='gray')
    plt.axis("off")

    plt.show()
