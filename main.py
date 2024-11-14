nums = [1, 2, 3, 4]

iter_object = iter(nums)
while True:
    try:
        print(next(iter_object))
    except StopIteration:
        break


iter_object = iter(nums)

while True:
    try:
        print(next(iter_object))
    except StopIteration:
        break
#
# p = Person("Test")
#
#
# print(len(p))
# for el in p:
#     print(el)
#
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#         self.current_index=-1
#
#     def __len__(self):
#         return len(self.name)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current_index += 1
#         if self.current_index < len(self.name):
#             return self.name[self.current_index]
#         raise StopIteration()
#
# print("after for")