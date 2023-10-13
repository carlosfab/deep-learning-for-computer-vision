# import the necessary libraries
import cv2


class SimplePreprocessor:
    """
    Resize an input image to a fixed size.

    Args:
        width (int): The desired width of the output image.
        height (int): The desired height of the output image.
        inter (int): The interpolation method used for resizing. Default is cv2.INTER_AREA.

    Methods:
        preprocess(image): Resize the input image to the specified width and height.

    Returns:
        NumPy array: The resized image as a NumPy array.
    """

    def __init__(self, width, height, inter=cv2.INTER_AREA):
        self.width = width
        self.height = height
        self.inter = inter

    def preprocess(self, image):
        """
        Resize the input image to the specified width and height.

        Args:
            image (NumPy array): The input image to be resized.

        Returns:
            NumPy array: The resized image as a NumPy array.
        """
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)
