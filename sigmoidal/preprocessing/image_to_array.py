# import necessary libraries
from tensorflow import keras
from keras.utils import img_to_array


class ImageToArrayPreprocessor:
    """
    Convert an input image to a NumPy array.

    Args:
        data_format (str): The image data format. Can be "channels_first" or "channels_last".

    Methods:
        preprocess(image): Convert the input image to a NumPy array.

    Returns:
        NumPy array: The converted image as a NumPy array.
    """

    def __init__(self, data_format=None):
        self.data_format = data_format

    def preprocess(self, image):
        return img_to_array(image, data_format=self.data_format)
