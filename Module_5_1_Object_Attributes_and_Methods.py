class House:
    """ЖК Эльбрус, 30"""
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):
        print(f'{self.name} имеет {self.number_of_floors} этажей')
        print(f'Нам нужно на {new_floor}-й этаж')
        if new_floor < 1 or new_floor > self.number_of_floors:
            print(f'Этажа под номером {new_floor} не существует!')
        else:
            for floor in range (new_floor):
                print(floor + 1)

h = House('ЖК Эльбрус, 30', 15)
h.go_to(14)
h.go_to(25)
h.go_to(-1)