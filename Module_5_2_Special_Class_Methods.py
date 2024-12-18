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

h = House('ЖК Эльбрус, 30', 51)
h_1 = House('ЖК Петрострой, 57', 24)
print(h_1)
print(h)
print(len(h_1))
print(len(h))