from itertools import islice
import numpy as np
from numpy import ndarray
from typing import Dict


class ImageReader:
    """
    PGM Image reader class.
    Reads a image and extract its metadata.
    And extract the image data and convert into numpy array: ndarray
    """

    def __init__(self, filename: str) -> None:
        self.filename = filename  # filename of the PGM file
        self.image_data = self.read_image()  # generator object
        self.metadata = self.extract_metadata()  # metadata extraction
        self.color_mode = self.metadata['color_mode']  # color mode
        self.comment = self.metadata['comment']  # comment line
        self.dimension = self.metadata['dimension']  # dimension
        self.width = int(self.dimension.split(" ")[0])  # width
        self.height = int(self.dimension.split(" ")[1])  # height
        self.max_value = self.metadata['max_value']  # max value of the pixel
        self.data = self.extract_data()  # numpy array of the image

    def read_image(self):
        """
        Reads an PGM image
        :return: generator object of the line
        """
        with open(self.filename, encoding="utf-8") as f_obj:
            for line in f_obj.readlines():
                yield line  # yields each line

    def extract_metadata(self) -> Dict[str, str]:
        """
        Extract metadata from the PGM Image
        :return: dictionary of metadata
        """
        # read first 4 lines and delete them
        metadata_: map = map(lambda x: x.strip(), list(islice(self.image_data, 4)))
        keys: list = ["color_mode", "comment", "dimension", "max_value"]

        metadata: Dict[str, str] = {key: value for key, value in zip(keys, metadata_)}
        return metadata

    def extract_data(self) -> ndarray:
        """
        Extract pixel values
        :return: ndarray of same as image size
        """
        data: ndarray = np.array(
            list(map(
                lambda x: int(x.strip()),  # delete new line and convert into integer
                self.image_data  # generator object first 4 line deleted
            ))).reshape((self.height, self.width))
        return data

    def save_img(self, target_folder: str = None):
        """
        Save an image from the ndarray
        :return:
        """
        pass
