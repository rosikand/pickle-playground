"""
File: program.py 
-------------------
This is a sample Python script for playing around with Python Pickle. 
"""

import pickle

# sample object to be pickled 
sample_obj_two = {"one": 1, "two": 2, "three": 3, "four": 4}

# pickle the file 

# the file that the pickled object will be saved to 
out_file = open("sample_file_two.pkl", "wb")

# save the object into the file 
# parameter format: pickle.dump(object, file) 
pickle.dump(sample_obj_two, out_file)

# close the file 
out_file.close() 

