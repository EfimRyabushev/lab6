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
n = int(inputing.readline())
array = inputing.readline()
arr = list (map ((lambda x: int (x)), array.split()))
arr.sort()
for i in range(len(arr) - 1):
   if arr[i] == arr[i + 1]:
      outputing.write(arr[i])
      break
