
import torch
import random
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from my_util import *
import pickle


categories=readLinesC("ParsedData/categories.txt")
sentences=readLines("ParsedData/titles.txt")
embeddings=np.load("saved_embeddings.npy")

network_state = torch.load("trained_model",map_location='cpu')

network_state

with open ('test_indices', 'rb') as fp:
    test_indices = pickle.load(fp)


index = random.choice(test_indices)
print("----------------------------")
print("SENTENCE: ",sentences[index], "PREDICTED CATEGORY: ",network.forward(embeddings[index]), "RIGHT CATEGORY: ", categories[index] )
print("----------------------------")
