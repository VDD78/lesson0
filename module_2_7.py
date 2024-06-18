# Домашнее задание по уроку "Распаковка параметров и параметры функции"

print('Задача распаковка - 1')
print('')
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

print('')
print('Задача распаковка - 2')
print('')

values_list = (8, 'moon', False)
values_dict = {'a': 2, 'b': 'joker', 'c': True}

print_params(*values_list)
print_params(**values_dict)

print('')
print('Задача распаковка - 3')
print('')

values_list_2 = (87, 'sun')
print_params(*values_list_2)




