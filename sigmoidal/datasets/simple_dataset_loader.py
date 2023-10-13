# import necessary libraries
import numpy as np
import cv2
from typing import List, Optional, Tuple
from pathlib import Path
import os
from tqdm import tqdm


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
        dataset_path: str,
        verbose: int = -1,
    ) -> Tuple[np.ndarray, List[str]]:
        """
         Load images from a dataset path and return a tuple of images and labels.

        Parameters:
        - dataset_path (str): Path to the dataset.

        Returns:
        - Tuple[List[np.array], List[str]]: A tuple containing a list of images and their corresponding labels.
        """

        # Lists to store loaded images and their labels
        images = []
        labels = []

        # Convert the generator to a list to get all image paths
        paths = list(Path(dataset_path).glob("*/*"))

        # Iterate over each image path and load the image and label
        for img_path in tqdm(paths, total=len(paths), desc="Loading images"):
            # Read the image
            image = cv2.imread(str(img_path))

            if self.preprocessors is not None:
                # Apply the preprocessors
                for p in self.preprocessors:
                    image = p.preprocess(image)

            # Add the preprocessed image and label to the lists
            images.append(image)
            labels.append(img_path.parent.name)

        return np.array(images), np.array(labels)
