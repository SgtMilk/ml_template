"""
This module is an example of a pytorch model. It is the simplest pytorch model there is,
the linear model.
"""
import torch

# pylint: disable=too-few-public-methods
class Linear(torch.nn.Module):
    """
    Linear model class example
    """

    def __init__(self, input_size: int, output_size: int):
        """
        Initializes the model.

        Args:
            input_size (int): The input size
            output_size (int): The output size
        """
        super().__init__()
        self.linear = torch.nn.Linear(input_size, output_size)

    # pylint: disable=redefined-builtin
    def forward(self, input: torch.Tensor):
        """
        Gives a prediction on the x input data.

        Args:
            x (torch.Tensor): The input for the prediction.

        Returns:
            pytorch tensor: The predicted value
        """
        out = self.linear(input)
        return out
