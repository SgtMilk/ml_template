# Copyright (c) 2022 Alix Routhier-Lalonde. Licence included in root of package.

"""
Contains the Params class, a collection for training parameters
"""
import torch
from torch.nn import MSELoss
from torch.optim import Adam

from src.model.linear_model import Linear


# DEVICE = torch.device("cpu")
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# ========== DATA PARAMETERS ========== #
SOURCE_PATH = "./src/data/source/"
CLEAN_PATH = "./src/data/clean/"
# of format [(filename1, url1), (filename2, url2), ...]
REQUEST_LIST = []
BATCH_SIZE = 4096

# ========== MODEL PARAMETERS ========== #
MODEL = Linear
MODEL_PATH = "./src/model/models/"
VALIDATION_SPLIT = 0.1
TEST_SPLIT = 0.1

# ========== TRAINING PARAMETERS ========== #
EPOCHS = 100
VERBOSITY_INTERVAL = 1
LEARNING_RATE = 0.0001
LOSS = MSELoss(reduction="mean")
OPTIMIZER = Adam
OPTIMIZER_BETAS = (0.5, 0.999)
