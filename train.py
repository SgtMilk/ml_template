# Copyright (c) 2022 Alix Routhier-Lalonde. Licence included in root of package.

"""
Runs the training loop.
"""
from src.data.dataloader import Dataloader
from src.model.net import Net

if __name__ == "__main__":
    # Getting the data
    dataset = Dataloader()

    # Training
    net = Net(dataset)
    net.train()

    # Testing
    net.evaluate()
