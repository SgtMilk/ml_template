# Copyright (c) 2022 Alix Routhier-Lalonde. Licence included in root of package.

"""
Contains the Params class, a collection for training parameters
"""
import torch


# DEVICE = torch.device("cpu")
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# ========== DATA PARAMETERS ========== #
SOURCE_PATH = "./src/data/source/"
CLEAN_PATH = "./src/data/clean/"
# of format [(filename1, url1), (filename2, url2), ...]
REQUEST_LIST = []
BATCH_SIZE = 4096

# ========== MODEL PARAMETERS ========== #
# MODEL =
VALIDATION_SPLIT = 0.1
TEST_SPLIT = 0.1

# ========== TRAINING PARAMETERS ========== #
# EPOCHS =
# LEARNING_RATE =
# LOSS =
# OPTIMIZER =
