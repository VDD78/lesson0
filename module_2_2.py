# first=12
# second=12
# third=11

first=int(input('Введите первое число: '))
second=int(input('Введите второе число: '))
third=int(input('введите третье число: '))

if first==second==third:
    print('Количество совпадений: 3')
elif ((first==second)and(first!=third))or((first==third)and(first!=second))or((second==third)and(second!=first)):
    print('Количество совпадений: 2')
else:
    print('Количество совпадений: 0')
# first!=second!=third
# second!=first!=third
# third!=first!=second

# if ((first==n1!=n2!=n3)or(first!=n1!=n2==n3)or(first!=n1==n2!=n3))\
#     and ((second==n1!=n2!=n3)or(second!=n1!=n2==n3)or(second!=n1==n2!=n3))\
#     and ((third==n1!=n2!=n3)or(third!=n1!=n2==n3)or(third!=n1==n2!=n3)):
#     print('2')
# elif ((first==n1 or first==n2 or first==n3) and (second==n1 or second==n2 or second==n3)
#       and (third==n1 or third==n2 or third==n3)):
#     print('3')
# elif first!=n1!=n2!=n3 and second!=n1!=n2!=n3 and third!=n1!=n2!=n3:
#     print('0')
#
# else:
#     print('1')

