# Arxivdl
Project work for a course in deep learning. 


## Dependencies
The code is written in python and uses some short bash scripts
to fetch and process the data. 

* Python 3 (confirmed working on 3.5.3)
* Pytorch
* InferSent (https://github.com/facebookresearch/InferSent)
	- NLTK>=3
	- One of the dowload links is not working on their github page, this should work  
	 `curl -Lo examples/infersent2.pkl https://dl.fbaipublicfiles.this should work  ent/infersent2.pkl`
* Basic shell


## Running
1. Dowload and follow the instructions for InferSent for the downloads (correct destinations can be found in `create_embeddings.py`)
2. run `getData.sh` to download the data from arXiv 
3. run `extractData.sh` to parse it to the correct form (check if your system uses python or python3 to run python)
4. run `create_embeddings.py` 
5. run `Atrain.py`
6. run `evaluate_model.py`

Feel free to modify parameters, slurm scripts available for convinience.
