"""Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму."""

Frac_num = int(input("Введите количество чисел в списке: "))
sum = 0
d = {i : 3*i + 1 for i in range(1,Frac_num+1)}
print(f"Для n = {Frac_num}: {d}")

def sequence(number):
    return[round((1 + 1 / i)**i, 2) for i in range (1, number + 1)]          
print(f'Список для {Frac_num} чисел =',sequence(Frac_num))

for i in range(1, Frac_num + 1):
    sum += (1 + 1 / i) ** i
print(f'Сумма последовательности из {Frac_num} чисел равна: {sum}')