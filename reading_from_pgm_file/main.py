from image_reader import ImageReader
import matplotlib.pyplot as plt

if __name__ == '__main__':
    path = "tiger.pgm"
    img_reader = ImageReader(path)

    plt.title(f"Color Mode: {img_reader.color_mode}\nwidth: {img_reader.width} height:{img_reader.height}")
    plt.imshow(img_reader.data, cmap='gray', vmin=0, vmax=img_reader.max_value)
    plt.axis("off")
    plt.show()

    # saving image
    # img_reader.save_img()
