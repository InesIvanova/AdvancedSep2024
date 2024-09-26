from functools import reduce

def operate(operator, *args):
    def sum_nums():
        return reduce(lambda x, y: x+y, args)

    def subtract_nums():
        return reduce(lambda x, y: x -y, args)

    def multiply_nums():
        return reduce(lambda x, y: x * y, args)

    def divide():
        return reduce(lambda x, y: x/y, args)

    mapper = {"+": sum_nums, "-": subtract_nums, "*": multiply_nums, "/": divide}
    return mapper[operator]()



print(operate("-", 1, 2,3,4))
