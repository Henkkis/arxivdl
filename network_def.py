import torch
import torch.nn as nn
import numpy as np


class MLP(nn.Module):
    def __init__(self,input_size,output_size):
        super(MLP, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, 200),
            nn.Tanh(),
            nn.Conv1d(1, 6, 1),
            nn.Linear(200, 100),
            nn.Tanh(),
            nn.Dropout(0.04),
            nn.Linear(100, 50),
            nn.Tanh(),
            nn.Dropout(0.04),
            nn.Conv1d(6, 1, 1),
            nn.Linear(50, output_size),
            nn.LogSoftmax(dim=2)
            )

    def forward(self, x):
        return self.net(x)
