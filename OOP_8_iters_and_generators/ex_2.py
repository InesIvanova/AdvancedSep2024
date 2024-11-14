class reverse_iter:
    def __init__(self, obj):
        self.data = obj
        self.current_index = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index -= 1
        if self.current_index >= 0:
            return self.data[self.current_index]
        raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
for item in reversed_list:
    print(item)

