from utils import read_image, write_image


def and_operation(img_1, img_2):
    new_image = []
    for i, j in zip(img_1, img_2):
        if i < j:
            if i < 128:
                new_image.append(i)
            else:
                new_image.append(j)
        else:
            if j < 128:
                new_image.append(j)
            else:
                new_image.append(i)
    return new_image


def or_operation(img_1, img_2):
    new_image = []
    for i, j in zip(img_1, img_2):
        if i < j:
            if j < 128:
                new_image.append(i)
            else:
                new_image.append(j)
        else:
            if i < 128:
                new_image.append(j)
            else:
                new_image.append(i)
    return new_image


def xor_operation(img_1, img_2):
    new_image = []
    for i, j in zip(img_1, img_2):
        if i < j:
            if j < 128:
                new_image.append(i)
            elif i >= 128:
                new_image.append(i)
            else:
                new_image.append(j)
        else:
            if i < 128:
                new_image.append(j)
            elif j >= 128:
                new_image.append(j)
            else:
                new_image.append(i)
    return new_image


if __name__ == '__main__':
    image_1 = "/home/subhranil/image_new/09_logical_operators/alan.pgm"
    image_2 = "/home/subhranil/image_new/09_logical_operators/subhranil.pgm"

    image_1_data = read_image(image_1)
    image_2_data = read_image(image_2)

    metadata_1 = image_1_data["meta_data"]
    metadata_2 = image_2_data["meta_data"]

    new_metadata = ['P2', '# Created by Subhranil', '256 335', '255']

    # new_img_data = and_operation(image_1_data["data"], image_2_data["data"])
    # new_img_data = or_operation(image_1_data["data"], image_2_data["data"])
    new_img_data = xor_operation(image_1_data["data"], image_2_data["data"])

    # write_image("and_op.pgm", new_metadata, new_img_data)
    # write_image("or_op.pgm", new_metadata, new_img_data)
    write_image("xor_op.pgm", new_metadata, new_img_data)
