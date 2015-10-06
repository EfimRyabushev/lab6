'''
Задача A
++++++++

В массиве ровно два элемента равны. Найдите эти элементы.

Программа получает на вход число N, в следующей строке заданы N элементов списка через пробел.

Выведите значение совпадающих элементов.

+-------------+-------+
| Ввод        | Вывод |
+=============+=======+
| 6           | 5     |
+-------------+-------+
| 8 3 5 4 5 1 |       |
+-------------+-------+
'''
inputting = open('input.txt', 'r')
outputing = open('output.txt', 'w')
N = int(inputting.readline().rstrip())
as = 0
for i in range(N):
  a = int(inputting.readline().rstrip())
  if arr.count(a) != 0:
    as = a
  arr.append(a)
outputting.write(as)
