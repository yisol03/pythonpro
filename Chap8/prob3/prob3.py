import pickle
import pickle as cPickle

variety = [ 'sweet', 'hot', 'dill' ]
pickle_file = open("pickles1.dat", "w")
cPickle.dump(variety, pickle_file)
pcikle_file.close()


print("Pickling lists.\n")
print("Unpivklinh lists.")
pickle_file = open("pickles1.dat", "r")
variety = cPickle.load(pickle_file)
print(variety)
