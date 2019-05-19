import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from my_util import *

categories=readLinesC("ParsedData/categories.txt")
embeddings=np.load("saved_embeddings.npy")




num_titles=len(categories)
num_categories=6
encoding_size=4096


device = torch.device("cuda")
X=[ embeddings[i][:] for i in range(0,num_titles)  ]
Y=[int(i) for i in categories]
X = torch.tensor(X,device=device)
Y= torch.tensor(Y,device=device)




class MLP(nn.Module):
    def __init__(self,input_size,output_size):
        super(MLP, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, 100),
            nn.ReLU(),
            nn.Linear(100, 100),
            nn.ReLU(),
            nn.Linear(100, output_size),
            nn.LogSoftmax(dim=0)
            )

    def forward(self, x):
        return self.net(x)

network =MLP(encoding_size,num_categories)
network.to(device)
network = network.cuda()

output = network.forward(X[0])
target = Y[0]
loss   = F.nll_loss(output,target)

print(loss.cpu().data.numpy())



