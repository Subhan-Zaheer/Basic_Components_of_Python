"""
os.getcwd will give you current working directory.
os.chdir will change the current working directory.
os.listdir will give you list of all directories present in given path.
os.mkdir will make one directory.
os.makedirs will make multiple directories (Directory into a directory).
os.rename will rename file with another name.
os.enviro.get() will give us environment variable.
os.isdir() will check if the input given is dirctory or not.
os.isfile() will check if the input given is file or not.
"""
import os
print(dir(os))

# print(os.getcwd())
# os.chdir("E://")
# print(os.getcwd())
for item in os.listdir("E://"):
    if item == "System Volume Information":
        print(dir(item))

# os.mkdir("This")
# os.makedirs("This/That")
# os.rename("ProgrammerSubhan.txt", "Subhan2.txt")
# f = open("Subhan2.txt")
# print("\nIt is from Subhan2 file\n")
# print(f.read())
# f.close()
# os.rename("Subhan2.txt", "ProgrammerSubhan.txt")
# f1 = open("ProgrammerSubhan.txt")
# print("\nIt is from ProgrammerSubhan file\n")
# print(f1.read())
# f1.close()
print(os.environ.get("Path"))
print(os.path.isdir("E://Arabic Grammer Book"))
