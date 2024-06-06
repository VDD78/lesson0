my_dict={'Vova':1978,'Anna':1980}
print(my_dict)
print((my_dict.get('Vova')),(my_dict.get('Anton')))
my_dict.update({'Lera':2016,'Dasha':2004})
print(my_dict)
print(my_dict.pop('Anna'))
print(my_dict)

my_set=[1,1,2,3,4,4,3,2, 'a','b',True,(3,7,8)]
print(my_set)
my_set=set(my_set)
print(my_set)
my_list=my_set.remove(1),my_set.add(6),my_set.add(9)
print(my_set)
