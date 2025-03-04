#List - Список
list1 = [1, 2, 3, 4, 5, None, 'text', False, 2.45]
print(list1)
print(list1[6])
print(list1[-1])
list1[6] = 12
print(list1)
list1 = []
print(list1)
list1.append(53)
list1.append('text')
print(list1)
print(len(list1))
print(list1.index('text'))
popped = list1.pop(0)
print(list1)
print(popped) #переменная с удаленным элементом списка
print('text' in list1) #поиск в списке

#Tuple - Кортеж - в кортеже нельзя изменять данные

tuple1 = (1, 2, 3, 4, 5, None, 'text', False, 2.45, 3)
print(tuple1[2])
print(tuple1[-1])
print(tuple1.count(3))
print(tuple1.index(5))

#Set - Множества - Содержит в себе только не поторяющиеся элементы

myset = {1, 2, 3, 4, 5, None, 'text', False, 2.45, 3, 5}
print(myset)
myset.add(42)
print(myset)

# dict - словарь

mydict = {'one': 'value', 'two': 'value2', 'three': 'value3'}
print(mydict['one'])
print(len(mydict))
mydict['one'] = 'myvalue'
print(mydict)
mydict['four'] = 55
print(mydict)
mydict['six'] = [1, 5, 68, 25, 14]
print(mydict)
print(mydict.keys())
print(mydict.values())
print(mydict.items())