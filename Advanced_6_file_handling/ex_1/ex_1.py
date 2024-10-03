try:
    file = open("text.txt")
    print(file.read())
    print("File found")
except FileNotFoundError:
    print("File not found")
