"""
File: depickle.py 
-------------------
This is a sample Python script for loading back in a pickled object. 
"""

import pickle

# read in file
in_file = open('sample_file.pkl', 'rb')

# load in object 
loaded_obj = pickle.load(in_file)

# close the file
in_file.close()

# test to see if working 
print(loaded_obj)
print(type(loaded_obj))