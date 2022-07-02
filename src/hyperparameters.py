"""
Contains the Params class, a collection for training parameters
"""
import torch


class Params:
    """
    Collection class for training parameters
    """

    # device = torch.device("cpu")
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # MODEL PARAMETERS
    # model =
    # hidden_dim = 256
    # num_dim = 4
    # dropout = 0.4
    # validation_split = 0.1

    # TRAINING PARAMETERS
    # epochs = 150
    # learning_rate = 0.0001
    # loss = MSELoss(reduction="mean")
    # optimizer = Adam
