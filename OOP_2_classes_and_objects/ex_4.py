import pdb


class Glass:
    """
    This is our service for producing glass
    """
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        """
        If there is enough space we will the glass
        """
        if (self.content + ml) > Glass.capacity:
            return f"Cannot add {ml} ml"
        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        space_left = self.capacity - self.content
        return f"{space_left} ml left"


breakpoint()
glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())

