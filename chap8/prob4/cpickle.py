import pickle
import shelve

print("Pickling lists.\n")

variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

print("Unpickling lists.")

with open("Pickle.dat", "wb") as pickle_file:
    pickle.dump(variety, pickle_file)
    pickle.dump(shape, pickle_file)
    pickle.dump(brand, pickle_file)

with open("Pickle.dat", "rb") as pickle_file:
    variety = pickle.load(pickle_file)
    shape = pickle.load(pickle_file)
    brand = pickle.load(pickle_file)
    print(variety)
    print(shape)
    print(brand)

print("\nShelving lists\n")

print("Retrieving lists from a shelved file:")
pickles = shelve.open("pickles2.dat")


pickles["variety"] = ["sweet", "hot", "dill"]
pickles["shape"] = ["whole", "spear", "chip"]
pickles["brand"] = ["Cluassen", "Heinz", "Vlassic"]
pickles.sync()

for key in pickles.keys() :
    print(key, "-", pickles[key])

pickles.close()

a = input("\n\nPress the enter key to exit.")

if a == "":
    print("")
