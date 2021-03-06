import torch
import random
import pickle
from network_def import *
from parameters import *
import numpy as np
import torch.nn as nn

from my_util import *


# Load our categories and saved embeddings from running create_embeddings.py
categories=readLinesC("ParsedData/categories.txt")
embeddings=np.load("saved_embeddings.npy")
num_titles=len(categories)



# Use a gpu and convert data to tensors
device = torch.device("cuda")
X=[ [embeddings[i][:]] for i in range(0,num_titles)  ]
Y=[[int(i)] for i in categories]
X = torch.tensor(X,device=device)
Y= torch.tensor(Y,device=device)




# Create the network
network =MLP(encoding_size,num_categories)
network.to(device)
network = network.cuda()
optimizer = torch.optim.Adam(network.parameters(), lr=0.0002)
criterion   = nn.NLLLoss()


# Split the data to training, validation and test data sets
total_indices = [i for i in range(0,num_titles)]
random.shuffle(total_indices)
test_indices = total_indices[0:int(num_titles/10)]
validation_indices = total_indices[int(num_titles/10):int(num_titles/10)*3]
training_indices = total_indices[int(num_titles/10)*3:]

# Save the indices for the test data so we can use them when we test our accuracy
with open('test_indices', 'wb') as fp:
    pickle.dump(test_indices, fp)





# Training loop
print("Starting training")
running_loss=0
best_loss = 100
grace = 5
for epoch in range(n_epochs):

    if(grace == 0):
        print("Early stopping")
        break

    train_selection = random.choices(training_indices, k=batch_size)
    train_inputs = torch.stack([X[i] for i in train_selection ])
    train_output = network.forward(train_inputs).view(-1,num_categories,1)
    train_target = torch.stack([Y[i] for i in train_selection ])

    optimizer.zero_grad()
    train_loss = criterion(train_output,train_target)
    train_loss.backward()
    optimizer.step()

    running_loss += train_loss.item()

    if(epoch % 500 == 0):
        val_selection = random.choices(validation_indices, k=validation_size)
        val_inputs = torch.stack([X[i] for i in val_selection ])
        val_output = network.forward(val_inputs).view(-1,num_categories,1)
        val_target = torch.stack([Y[i] for i in val_selection ])
        val_loss = criterion(val_output,val_target)
        if(val_loss > best_loss):
            grace -=1
        else:
            grace=6
            best_loss=val_loss

        print("Training Loss: ",running_loss/500, "Validation Loss: ", val_loss.item(),  "Epoch:", epoch)
        running_loss=0


torch.save(network.state_dict(),"trained_model")
