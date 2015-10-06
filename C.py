'''
Задача C
++++++++

В прихожей в ряд стоит N тапочек, которые бывают разных размеров, а также левыми и правыми. Гость выбирает два тапочка,
удовлетворяющих следующим условиям:

- выбранные тапочки должны быть одного размера;
- из выбранных тапочков левый тапочек должен стоять левее правого;
- если можно выбрать несколько пар тапочек, удовлетворяющих первым двум условиям, то выбирается два тапочка с наименьшим
  расстоянием между ними.

  В первой строке входны данных записано число тапочков N. Во второй строке записаны размеры тапочков в порядке слева
  направо, при этом левые тапочки условно обозначаются отрицательными числами (то есть -s обозначает левый тапочек, а s
  обозначает правый тапочек размера s).

  Выведите одно число: минимальное расстояние между двумя тапочками одного размера таких, что левый тапочек стоит левее
  правого. Если таких пар тапочек нет, то выведите одно число 0.

  +----------------------+-------+
  | Ввод                 | Вывод |
  +======================+=======+
  | 6                    | 2     |
  +----------------------+-------+
  | -40 41 -42 -41 42 40 |       |
  +----------------------+-------+
'''
inputting = open('input.txt', 'r')
outputing = open('output.txt', 'w')
N = int(inputting.rstrip())
arr = inputting.rstrip()
arr = list(map((lambda x: int(x)), arr))
ans = []
for i in range(len(arr)):
   if arr[i] < 0:
      for b in range (i, len(arr)):
          if arr[i] == (-1)*arr[b]:
             ans.append(b - i)
             break
if (not arr):
    outputting.write(0)
else:
   outputting.write(min (ans))
