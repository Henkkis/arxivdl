# curl -Lo examples/infersent2.pkl https://dl.fbaipublicfiles.com/senteval/infersent/infersent2.pkl


import torch
import numpy as np
import torch.nn as nn
import sys
import nltk
from my_util import *
sys.path.insert(0, '../InferSent')
nltk.download('punkt')
from models import InferSent

sentences=readLines("ParsedData/titles.txt")
categories=readLinesC("ParsedData/categories.txt")



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




