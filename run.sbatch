#!/bin/bash

#SBATCH -t 00:05:00
#SBATCH -p gpu
#SBATCH --mem=8G
#SBATCH --gres=gpu:p100:1

module load python-env/3.6.3-ml
python3 create_embeddings.py

