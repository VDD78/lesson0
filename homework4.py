#name=input('Введите Ваше имя: ')
#current_year=2024
#date_of_birth=int(input('В каком году Вы родились? '))
#age=current_year-date_of_birth
#print('В этом году Вам ',age,'лет')
#print('привет, я строка в нижнем регистре'.upper().lower().replace('привет', 'пока'))
# .upper() - верхний регистр, .lower() - нижний регистр
# .replace() - замена значения на другое, в скобках, через запятую

name=input('Привет, как тебя зовут? ')
print(len(name))
my_string='ПРИВЕТ, какая ХОРОШАЯ погода'
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ',''))
print(my_string[0],my_string[-1])
