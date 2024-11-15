def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1, 'строка', True)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print('-------------------')
values_list = [50, 'Error', False]
values_dict = {'a': 100500, 'b': True, 'c': 'iteration'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [101, 'строка']
print_params(*values_list_2, 'error')