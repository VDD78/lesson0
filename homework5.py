immutable_var=3,2,1,'start',True
print(immutable_var)            # кортежи,числа и строки - неизменяемые
immutable_var=[3,2,1],'start',True
immutable_var[0][0]=[1]
print(immutable_var)            # числа отделбного блока в кортеже меняются
immutable_list=[3,2,1,'start', True]
print(immutable_list)
immutable_list[0]=[2]
print(immutable_list)