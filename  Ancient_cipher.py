import random
def get_a_random_number():
    """Получение случайного числа от 3 до 20"""
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    random_number = random.choice(numbers)
    return random_number

def get_password(num):
    """Ключ - значение/ Шифр - пароль"""
    password_dict = {3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645,
                10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867,
                14: 1611325212343114105968, 15: 1214114232133124115106978, 16: 1317115262143531341251161079,
                17: 11621531441351261171089, 18: 12151811724272163631545414513612711810,
                19: 118217316415514613712811910, 20: 13141911923282183731746416515614713812911}
    password = password_dict.get(num)
    return password

num = get_a_random_number()
print('Шифр: ', num)
print('Пароль: ', get_password(num))

pair_numbers_1 = range(num)
pair_numbers_2 = range(num)
pairs = []
result = str()

for q in pair_numbers_1:
    for w in pair_numbers_2:
        p_n_1 = q
        p_n_2 = w
        if p_n_1 >= p_n_2:
            continue
        else:
            integer_division = num % (p_n_1 + p_n_2)
            if integer_division == 0:
                pairs.append([p_n_1, p_n_2])
                result = result + str(p_n_1) + str(p_n_2)
print('Пары чисел: ', * pairs)
print('Введите пароль:', result)