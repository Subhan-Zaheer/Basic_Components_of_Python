import pickle

languages = ["Urdu", "English", "Punjabi", "Arabic"]

file_name = "lang.pkl"
fileobj = open(file_name, "wb")
pickle.dump(languages, fileobj)
fileobj.close()

fileobj1 = open(file_name, "rb")
my_languages = pickle.load(fileobj1)
print(my_languages)