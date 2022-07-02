# Copyright (c) 2022 Alix Routhier-Lalonde. Licence included in root of package.

"""
This module includes the Dataloader class.
"""

import torch
import numpy as np
from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler
from src.params import CLEAN_PATH, REQUEST_LIST, BATCH_SIZE, VALIDATION_SPLIT, TEST_SPLIT, DEVICE


class Dataloader:
    """
    This class will get data from a clean source, divide and resize it, and serve it into batches.
    """

    def __init__(self):
        """
        Gets data from the clean folder, does a bit of pre-processing, scales it, divides it into
        batches and into training, validation and testing datasets.
        """
        x_data_unscaled = np.array([])
        y_data_unscaled = np.array([])

        for filename, _ in REQUEST_LIST:
            dataframe = read_csv(
                CLEAN_PATH + filename,
                # index_col="SOMETHING HERE",
            )
            if dataframe is None:
                continue

            ### DO OTHER CHECKS HERE TO SEE IF RIGHT FORMAT, ETC. ###

            ### FIND YOUR X AND Y DATA (CHANGE THIS) ###
            data = dataframe.to_numpy()
            x_temp = data[0]
            y_temp = data[1]

            x_data_unscaled = np.concatenate((x_data_unscaled, x_temp))
            y_data_unscaled = np.concatenate((y_data_unscaled, y_temp))

        ### DO OTHER CHECKS HERE ###
        assert x_data_unscaled.shape[0] == y_data_unscaled.shape[0]

        ### USE A SCALER ###
        x_scaler = MinMaxScaler()
        y_scaler = MinMaxScaler()
        x_data = x_scaler.fit_transform(x_data_unscaled)
        y_data = y_scaler.fit_transform(y_data_unscaled)

        self.scalers = (x_scaler, y_scaler)

        ### DIVIDE IN BATCHES ###
        num_batches = x_data.shape[0] // BATCH_SIZE
        x_data = np.resize(
            x_data[: num_batches * BATCH_SIZE], (num_batches, BATCH_SIZE, *x_data.shape[1:])
        )
        y_data = np.resize(
            y_data[: num_batches * BATCH_SIZE], (num_batches, BATCH_SIZE, *y_data.shape[1:])
        )

        ### TRANSFORMING INTO CPU TENSORS ###
        x_data = torch.from_numpy(x_data)
        y_data = torch.from_numpy(y_data)

        ### SPLITTING DATA IN TRAINING, VALIDATION AND TESTING DATASETS ###
        v_split = int(x_data.shape[0] * (1 - VALIDATION_SPLIT - TEST_SPLIT))
        t_split = int(x_data.shape[0] * (1 - TEST_SPLIT))

        self.train_data = (
            x_data[:v_split],
            y_data[:v_split],
        )
        self.validation_data = (
            x_data[v_split:t_split],
            y_data[v_split:t_split],
        )
        self.test_data = (
            x_data[t_split:],
            y_data[t_split:],
        )

        self.num_train_batches = v_split
        self.num_validation_batches = t_split - v_split
        self.num_test_batches = x_data.shape[0] - t_split

    class Iterable:
        """
        Iterable class for the training, validation and testing datasets.
        Returns the batch on the specified dataset.
        """

        def __init__(self, dataset):
            """
            Sets the counter, max as well as the dataset of the iterator.

            Args:
                dataset (torch cpu tensor): The dataset to iterate through.
            """
            self.x_data = dataset[0]
            self.y_data = dataset[1]
            self.max = self.x_data.shape[0]
            self.counter = -1
            assert self.x_data.shape[0] == self.y_data.shape[0]

        def __iter__(self):
            """
            Returns the iterator object

            Returns:
                object: The iterator object
            """
            return self

        def __next__(self):
            """
            Goes to the next value in the iterator.
            Returns the batch on the specified device.

            Raises:
                StopIteration: If we are done iterating.

            Returns:
                torch tensor: The batch tensor.
            """
            self.counter += 1
            if self.counter < self.max:
                return (
                    self.x_data[self.counter].to(device=DEVICE),
                    self.y_data[self.counter].to(device=DEVICE),
                )
            raise StopIteration

    def get_train(self):
        """
        Returns an iterable for the train data.
        Will return the data on the asked device.

        Returns:
            tensor: (x, y) train data
        """
        return self.Iterable(self.train_data)

    def get_validation(self):
        """
        Returns an iterable for the validation data.
        Will return the data on the asked device.

        Returns:
            tensor: (x, y) validation data
        """
        return self.Iterable(self.validation_data)

    def get_test(self):
        """
        Returns an iterable for the test data.
        Will return the data on the asked device.

        Returns:
            tensor: (x, y) test data
        """
        return self.Iterable(self.test_data)
