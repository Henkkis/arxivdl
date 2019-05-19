import torch
import random
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from my_util import *

categories=readLinesC("ParsedData/categories.txt")
embeddings=np.load("saved_embeddings.npy")




num_titles=len(categories)
num_categories=6
encoding_size=4096
batch_size=128


device = torch.device("cuda")
#device =torch.device("cpu")
X=[ [embeddings[i][:]] for i in range(0,num_titles)  ]
Y=[[int(i)] for i in categories]
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




# Divide the data in a random order 

# 70% 20% 10%
# Generators would we a nicer way to do this (maby in another version)
total_indices = [i for i in range(0,num_titles)]
# shuffel
random.shuffle(total_indices)

test_indices = total_indices[0:int(num_titles/10)]
validation_indices = total_indices[int(num_titles/10):int(num_titles/10)*3]
training_indices = total_indices[int(num_titles/10)*3:]
print(test_indices)




#output = network.forward(X[0:10]).view(-1,num_categories,1)
#target = Y[0:10]
#criterion   = nn.NLLLoss()
#loss = criterion(output,target)



