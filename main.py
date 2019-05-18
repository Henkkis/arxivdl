# curl -Lo examples/infersent2.pkl https://dl.fbaipublicfiles.com/senteval/infersent/infersent2.pkl

from __future__ import unicode_literals, print_function, division
from io import open
import glob
import os
import torch
import numpy as np


import unicodedata
import string

all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)

def letterToIndex(letter):
    return all_letters.find(letter)

def readLines(filename):
    lines = open(filename, encoding='utf-8').read().strip().split('\n')
    return [line.strip() for line in lines]

def readWords(filename):
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
import torch.nn as nn

import sys
sys.path.insert(0, '../InferSent')
import nltk
nltk.download('punkt')
from models import InferSent
V = 2
MODEL_PATH = '../InferSent/encoder/infersent%s.pkl' % V
params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                'pool_type': 'max', 'dpout_model': 0.0, 'version': V}
infersent = InferSent(params_model)
infersent.load_state_dict(torch.load(MODEL_PATH))
infersent = infersent.cuda()

W2V_PATH = '../InferSent/dataset/fastText/crawl-300d-2M-subword.vec'
infersent.set_w2v_path(W2V_PATH)
print(sentences[0:10])
infersent.build_vocab(sentences, tokenize=True)
print("Starting encoding")
embeddings = infersent.encode(sentences, tokenize=True)
np.save("saved_embeddings",embeddings)
print("Done")




