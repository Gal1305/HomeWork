from Sorting_algorithms import *

data_1 = list(map(int, input("Введите значения через пробел: ").split()))
data_2 = list(map(int, input("Введите значения через пробел: ").split()))
data_3 = list(map(int, input("Введите значения через пробел: ").split()))

bubble_sort(data_1)
selections_sort(data_2)


print("Пузырьковая сортировка: ", data_1)
print("Сортировка выбором: ", data_2)