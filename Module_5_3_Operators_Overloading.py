class House:
    """ЖК Эльбрус, 30"""
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        Name = f'Название: {self.name}, количество этажей: {self.number_of_floors}'
        return Name

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self



h = House('ЖК Эльбрус, 30', 51)
h_1 = House('ЖК Петрострой, 57', 24)

print(h)
print(h_1)
print()
print(h == h_1) #__eq__
print()
h_1 = h_1 + 10 #__add__
print(h_1)
print(h == h_1)
print()
h_1 += 10 #__iadd__
print(h_1)
print()
h = 10 + h #__radd__
print(h)
print()
print(h > h_1) #__lt__
print(h >= h_1) #__le__
print(h < h_1) #__gt__
print(h <= h_1) #__ge__
print(h != h_1) # __ne__