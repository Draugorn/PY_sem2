"""Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число."""

file_op = open("file.txt", "r")
a, b, c = file_op.read().split("\n")

a,b,c = int(a)-1, int(b)-1, int(c)-1

Numericals = int(input("Введите количество чисел массива:"))
Num_array = []

for i in range(1, Numericals+1):
    Num_array.append(i)

res = Num_array[a] * Num_array[b] * Num_array[c]

print(f"Позиция один: {a+1}, её значение: {Num_array[a]}, позиция два: {b+1}, её значение: {Num_array[b]}, третья позиция: {c+1}, её значение: {Num_array[c]}, произведение элементов: {res}")
