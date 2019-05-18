from __future__ import unicode_literals, print_function, division
from io import open
import glob
import os


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
