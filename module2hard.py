def count_pas(n):
    password = list()
    for i in range(1,n):
        for j in range(i+1,n):
            if n % (i + j) == 0:
                an = str(i) + str(j)
                password.append(an)
    return password

n = int(input('Что там выпало на первом камне? :'))
while (n < 3 or n > 20):
    n = int(input('Суицидник, вводи правильно:'))

result = str()
baseresult = count_pas(n)
for i in range(len(baseresult)):
    result += baseresult[i]
print('Вводи на втором камне:', result)