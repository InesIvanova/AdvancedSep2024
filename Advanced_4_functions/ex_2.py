def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


data = {"name": "George", "town": "Sofia", "age": 20}
print(get_info(**data))
print(get_info(name=data["name"], town=data["town"], age=data["age"]))


def sum_nums(*args):
    total = 0
    for el in args:
        total += el
    return total



print(sum_nums(1, 2))
print(sum_nums())