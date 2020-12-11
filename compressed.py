import pickle
import bz2


dogs_obj = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }


saved_file = bz2.BZ2File('compressed_file.pkl', 'w')

pickle.dump(dogs_obj, saved_file)

saved_file.close()