import pickle

in_f = open('compressed_file.pkl', 'rb')

loaded_o = pickle.load(in_f) 

# close 
in_f.close()

# test to see if working 
print(loaded_o)
print(type(loaded_o))