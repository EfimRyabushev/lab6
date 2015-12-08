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
def search(arr):
    for i in range(len(arr)):
        if arr[i] == arr[i + 1]:
            return arr[i]
input = open('input.txt', 'r')
output = open('output.txt', 'w')
N = input.readline()
N = int(N.rstrip())
line = input.readline()
line = line.rstrip()
line = list (map(lambda x: int(x), line.split()))
line = sorted(line)
output.write(search(line))
