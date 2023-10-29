# import necessary libraries
import os
from pathlib import Path
from typing import List, Optional, Tuple

import cv2
import numpy as np
from tqdm import tqdm


class SimpleDatasetLoader:
    """
    A utility class to load and preprocess images from a dataset directory structure.

    Attributes:
        preprocessors (List[Callable]): A list of image preprocessing functions or objects
                                        with a "preprocess" method.

    Methods:
        load: Load images from a specified dataset path and return images and their labels.

    Example:
        loader = SimpleDatasetLoader(preprocessors=[ResizePreprocessor(32, 32)])
        images, labels = loader.load("path/to/dataset")
    """

    def __init__(
        self,
        preprocessors: Optional[List] = None,
    ) -> None:
        """
        Initialize a new SimpleDatasetLoader.

        Parameters:
            preprocessors (Optional[List]): List of image preprocessing functions or
                                            objects with a "preprocess" method. Defaults to None.
        """
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

        Images are loaded from sub-directories within the dataset_path. Each sub-directory's
        name is used as the label for all images within it.

        If preprocessors are specified in the SimpleDatasetLoader, they are applied in the
        order they are listed.

        Parameters:
        - dataset_path (str): Path to the dataset directory structure.
        - verbose (int, optional): Verbosity level for tqdm progress bar. Default is -1,
                                   which means no progress bar.

        Returns:
        - Tuple[np.ndarray, List[str]]: A tuple containing a list of preprocessed images
                                        and their corresponding labels.
        """

        # Lists to store loaded images and their labels
        images = []
        labels = []

        # Convert the generator to a list to get all image paths
        paths = list(Path(dataset_path).glob('*/*'))

        # Iterate over each image path and load the image and label
        for img_path in tqdm(
            paths,
            total=len(paths),
            desc='Loading images',
            disable=verbose == -1,
        ):
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
