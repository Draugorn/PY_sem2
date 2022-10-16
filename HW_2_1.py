""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. """

def calculus_sumofdigits():
    try:
        Sumofdigits = 0
        print("Введите число:")
        Num_Sum = input ().replace(".", "").replace("-", "").replace(",","")
        for i in Num_Sum:
            Sumofdigits += int(i)
    except ValueError:
        print("Число не введено, повторите ввод.")
        calculus_sumofdigits()
    return Sumofdigits

print (f"Сумма цифр введенного числа составляет: {calculus_sumofdigits()}")
