from __future__ import unicode_literals, print_function, division

import unicodedata
import string
import sys

all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)

def unicodeToAscii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in all_letters
    )

data_dir=sys.argv[1]

with open ("{}/titles.temp".format(data_dir), "r") as fh_in, open ("{}/titles.txt".format(data_dir),"w") as outF:
    # Read each line in loop
    for line in fh_in:
        outF.write( unicodeToAscii(line).lower() +"\n")
