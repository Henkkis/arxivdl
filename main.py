from __future__ import unicode_literals, print_function, division
from io import open
import glob
import os
import torch

import unicodedata
import string

all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)

def letterToIndex(letter):
    return all_letters.find(letter)

def readLines(filename):
    lines = open(filename, encoding='utf-8').read().strip().split('\n')
    return [line.strip().split(' ') for line in lines]

def readLinesC(filename):
    lines = open(filename, encoding='utf-8').read().strip().split('\n')
    return lines

def lineToTensor(line):
    tensor = torch.zeros(len(line), 1, n_letters)
    for li, letter in enumerate(line):
        tensor[li][0][letterToIndex(letter)] = 1
    return tensor

def sentenceToTensor(sentence):
    return [lineToTensor(i) for i in sentence]


sentences=readLines("ParsedData/titles.txt")
categories=readLinesC("ParsedData/categories.txt")
merged_list = [(sentences[i][j] ,categories[i]) for i in range(0,len(categories)) for j in range(0,len(sentences[i]))  ]
print(merged_list)


import torch.nn as nn

class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(RNN, self).__init__()

        self.hidden_size = hidden_size

        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), 1)
        hidden = self.i2h(combined)
        output = self.i2o(combined)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)

n_hidden = 128
n_categories = 6
rnn = RNN(n_letters, n_hidden, n_categories)
hidden = torch.zeros(1, n_hidden)




