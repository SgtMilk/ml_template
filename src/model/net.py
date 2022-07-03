# Copyright (c) 2022 Alix Routhier-Lalonde. Licence included in root of package.

"""
Contains the Net class, a class for training a model.
"""

import time
import os
from datetime import datetime
from sklearn.metrics import mean_squared_error
import torch
from torch.utils.tensorboard import SummaryWriter
from src.data.dataloader import Dataloader


from src.params import (
    MODEL,
    DEVICE,
    MODEL_PATH,
    EPOCHS,
    LOSS,
    OPTIMIZER,
    LEARNING_RATE,
    OPTIMIZER_BETAS,
    VERBOSITY_INTERVAL,
)
from src.utils.cmd import printc


class Net:
    """
    Trains and evaluates a model.
    """

    def __init__(self, dataset: Dataloader, filename: str = None):
        """
        Initializes the Net and generates the file name of the model.

        Args:
            dataset (Dataloader object): The dataset to train on.
            filename (str, optional): The filename to save/load the model to/from. Defaults to None.
        """

        # Initialize the model (change model declaration if necessary)
        model = MODEL(dataset.train_data.shape[1], 1)
        self.model = model.to(device=DEVICE)

        self.dataset = dataset
        self.optimizer = OPTIMIZER(self.model.parameters(), lr=LEARNING_RATE, betas=OPTIMIZER_BETAS)

        if filename is None:
            # getting the right file name
            now = datetime.now()
            dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
            self.model_filepath = MODEL_PATH + dt_string + ".hdf5"
        else:
            self.model_filepath = MODEL_PATH + filename

    def train(self):
        """
        Runs the training loop for the model.
        """

        writer = SummaryWriter()

        start_time = time.time()

        lowest_validation_error = 10000000000

        for epoch in range(1, EPOCHS + 1):

            log_error_train = 0
            log_error_validation = 0

            ##################
            # model training #
            ##################

            self.model.train()
            with torch.set_grad_enabled(True):
                for x_train, y_train in self.dataset.get_train():

                    output = self.model(x_train)
                    error = LOSS(output, y_train)
                    log_error_train += error.mean().item()

                    self.model.zero_grad()
                    error.backward()
                    self.optimizer.step()

            ####################
            # model validation #
            ####################

            self.model.eval()
            with torch.set_grad_enabled(False):
                for x_validation, y_validation in self.dataset.get_validation():

                    output = self.model(x_validation)

                    error = LOSS(output, y_validation)
                    log_error_validation += error.mean().item()

                    self.model.zero_grad()

            log_error_train /= self.dataset.num_train_batches
            log_error_validation /= self.dataset.num_validation_batches

            # save if the validation error is the lowest
            if log_error_validation < lowest_validation_error:
                lowest_validation_error = log_error_validation
                self.save()

            # logging losses to console and tensorboard
            writer.add_scalar("Training Error", log_error_train, epoch)
            writer.add_scalar("Validation Error", log_error_validation, epoch)
            if epoch == 1 or epoch % VERBOSITY_INTERVAL == 0:
                print(
                    f"Epoch {epoch}/{EPOCHS}, Training Error: {log_error_train}, "
                    + f"Validation Error: {log_error_validation}"
                )
        training_time = time.time() - start_time
        print(f"Training time: {training_time}")
        self.load()
        torch.cuda.empty_cache()

    def evaluate(self):
        """
        Evaluates the model.
        """

        self.model.eval()

        scaled_mse = 0
        with torch.set_grad_enabled(False):
            for x_test, y_test in self.dataset.get_test():

                output = self.model(x_test)

                scaled_mse += mean_squared_error(
                    output.detach().cpu().numpy(),
                    y_test.detach().cpu().numpy(),
                )

        print(f"scaled_mse_y: {scaled_mse/self.dataset.num_test_batches}")

    def save(self):
        """
        Saves the model according to the Net filepath.
        """

        if os.path.exists(self.model_filepath):
            os.remove(self.model_filepath)
        torch.save(self.model.state_dict(), self.model_filepath)

    def load(self):
        """
        Loads a dataset according to the Net filepath.
        If the Net filepath is not present, it searches through all the models to find the
        most recent, and loads this one.
        """

        filepath = self.model_filepath
        models = os.listdir()
        if filepath not in models:
            if len(models) == 0:
                printc("No model exists.", ["red"])
                return
            filepath = MODEL_PATH + os.listdir().sort(reverse=True)[0]

        self.model = self.model.to(device=DEVICE)
        self.model.load_state_dict(torch.load(self.model_filepath))
