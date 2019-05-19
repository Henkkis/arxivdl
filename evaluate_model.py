
import random
from my_util import *
import pickle
from network_def import *
from parameters import *
import numpy as np
import torch

categories=readLinesC("ParsedData/categories.txt")
sentences=readLines("ParsedData/titles.txt")
num_titles=len(categories)
embeddings=np.load("saved_embeddings.npy")
X=[ [embeddings[i][:]] for i in range(0,num_titles)  ]
X = torch.tensor(X)
network_state = torch.load("trained_model",map_location='cpu')
network =MLP(encoding_size,num_categories)
network.load_state_dict(network_state)



with open ('test_indices', 'rb') as fp:
    test_indices = pickle.load(fp)



for i in range(0,10):
    index = random.choice(test_indices)
    selection = torch.unsqueeze(X[index,:,:],0)
    value,idx = torch.max(torch.exp(network.forward(selection)),2)

    pred_category =  int(idx.data.tolist()[0][0])

    print("----------------------------")
    print("SENTENCE: ",sentences[index], "PREDICTED CATEGORY: ",pred_category, "RIGHT CATEGORY: ", categories[index], "INDEX IN DATA: ",index )
    print("----------------------------")
