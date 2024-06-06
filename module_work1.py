grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johny','Bilbo','Steve','Khendrik','Aaron'}

name0='Aaron'
name1='Bilbo'
name2='Johny'
name3='Khendrik'
name4='Steve'

grades0=sum(grades[0])/(len(grades[0]))
grades1=sum(grades[1])/(len(grades[1]))
grades2=sum(grades[2])/(len(grades[2]))
grades3=sum(grades[3])/(len(grades[3]))
grades4=sum(grades[4])/(len(grades[4]))

print({name0:grades0,name1:grades1,name2:grades2,name3:grades3,name4:grades4})
# grades_sum=[sum(grades[0])/(len(grades[0])),sum(grades[1])/(len(grades[1])),
#             sum(grades[2])/(len(grades[2])),sum(grades[3])/(len(grades[3])),sum(grades[4])/(len(grades[4]))]
# print(grades_sum)
# print(tuple(students))
# print(list(students))

# students=len(students),set(students)
# print(students)