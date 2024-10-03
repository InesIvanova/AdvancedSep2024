import os
from constants import ABSTRACT_PATH

path = os.path.join(ABSTRACT_PATH, "nested.txt")
file = open(path)
print(file.read())