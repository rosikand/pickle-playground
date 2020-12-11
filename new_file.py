import pickle

in_file = open('sample_file_two.pkl', 'rb')

loaded_object = pickle.load(in_file)

# close inputted file
in_file.close()

# test 
print(loaded_object)
print("Type: ", type(loaded_object))