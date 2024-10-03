import json

a = {"a": 1}

with open("asd.txt", "w") as file:
    file.write(json.dumps(a))