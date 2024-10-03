import os

path = os.path.join("..", "ex_3", "my_first_file.txt")

try:
    os.remove(path)
except:
    print("File already deleted")