from math import pow
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


def bitplane_slicing(img_data, bit):
    new_img = [1 if i % pow(2, bit) >= pow(2, bit - 1) else 0 for i in img_data]
    return new_img


if __name__ == '__main__':
    # image_path = "/home/subhranil/image_new/02_negative/alan.pgm"
    image_path = "/home/subhranil/image_new/05_bitplane_slicing/Alan_Turing.pgm"

    img_data = read_image(image_path)

    img_data["meta_data"][-1] = '1'

    for i in tqdm(range(1, 9)):
        bit_data = bitplane_slicing(img_data["data"], i)
        write_image(f"{i}_bit_image.pgm", img_data["meta_data"], bit_data)
