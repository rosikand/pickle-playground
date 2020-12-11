import pickle

dogs_obj = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

out_f = open('uncompressed.pkl', 'wb')

pickle.dump(dogs_obj, out_f)

out_f.close()
