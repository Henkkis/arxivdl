#!/bin/bash

#SBATCH -t 00:05:00
#SBATCH -p gpu
#SBATCH --mem=8G
#SBATCH --gres=gpu:k80:1

module load python-env/3.6.3-ml
srun --unbuffered python3 Atrain.py

