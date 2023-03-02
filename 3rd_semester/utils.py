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
