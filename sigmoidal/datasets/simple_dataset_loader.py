# import necessary libraries
import numpy as np
import cv2
from typing import List, Optional
import os


class SimpleDatasetLoader:
    def __init__(
        self,
        preprocessors: Optional[List] = None,
    ) -> None:
        # store the image preprocessor
        self.preprocessors = preprocessors

        # if the preprocessors list is None, initialize it as an empty list
        if self.preprocessors is None:
            self.preprocessors = []

    def load(
        self,
        image_paths: List[str],
        verbose: int = -1,
    ):
        images = []
        labels = []

        for i, path in enumerate(image_paths):
            image = cv2.imread(path)
            label = 

            if self.preprocessors is not None:

        for p in self.preprocessors:
            p.