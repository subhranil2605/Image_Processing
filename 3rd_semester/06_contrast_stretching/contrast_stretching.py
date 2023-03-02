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


def contrast_stretch(img_data):
    min_ = min(img_data)
    max_ = max(img_data)
    new_img_data = list(map(lambda x: round(((x - min_) / (max_ - min_)) * 255), img_data))
    return new_img_data


if __name__ == '__main__':
    image_path = "/home/subhranil/image_new/06_contrast_stretching/hello.pgm"

    img_data = read_image(image_path)
    meta_data = img_data["meta_data"]

    contrast_stretched_img = contrast_stretch(img_data["data"])
    write_image("modified_image.pgm", meta_data, contrast_stretched_img)
