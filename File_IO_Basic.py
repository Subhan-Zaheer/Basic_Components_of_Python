"""
"r" - Open file for reading purpose - default
"w" - Open file for Writing Purpose
"x" - Create file if does not exist
"a" - Append mode
"t" - Text mode
"b" - Binary Mode
"+" - read and write
"""
# Reading Function with file.

f = open("Subhan.txt.txt")
# content = f.read()
# print(content)
# print(f.readline())
# print(f.readline())
print(f.readlines())
# for line in f:
#     print(line)

f.close()

# Writing a file
file = open("Subhan2.txt", "a")
file.write("So it is Subhan 2 file \n")

file2 = open("Subhan3.txt", "a")
file2.write("So it is Subhan 3 file.\n")

file3 = open("Subhan3.txt", "r+")
print(file3.tell())
file3.write("It is another line.")
print(file3.read())


"""
Seek function will reset the pointer to our given position.
Tell function will tell us the recent position of our file pointer.
"""

f = open("Subhan.txt.txt")

print(f.seek(2))
print(f.tell())
print(f.read())

file.close()
file2.close()
file3.close()




