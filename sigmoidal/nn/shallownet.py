from keras import backend as K
from keras.layers import Activation, Conv2D, Dense, Flatten
from keras.models import Sequential
from tensorflow import keras


class ShallowNet:
    """ShallowNet is a class that builds a shallow neural network for image classification."""

    @staticmethod
    def build(width, height, depth, classes):
        """
        Builds a shallow neural network for image classification.

        Parameters:
        -----------
        width : int
            The width of the input image.
        height : int
            The height of the input image.
        depth : int
            The depth of the input image.
        classes : int
            The number of classes to classify the input image into.

        Returns:
        --------
        model : keras.Sequential
            The shallow neural network model.
        """
        model = Sequential()
        input_shape = (height, width, depth)

        model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(Flatten())
        model.add(Dense(classes))
        model.add(Activation('softmax'))

        # return the network
        return model
