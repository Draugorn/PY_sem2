"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""

def Multiplier_Calculus():
    try:
        array = []
        Multi_Sum = 1
        print("Введите число от 1 до N:")
        Num_Mult = int(input ())
        for i in range(1, Num_Mult+1):
            Multi_Sum *= i
            array.append(Multi_Sum)
        if Num_Mult < 0:
            print("Вы ввели отрицательное число. Введите положительное целое! ")
            Multiplier_Calculus()
    except ValueError:
        print("Целое число не введено, повторите ввод.")
        Multiplier_Calculus()
    return array

print (f"Произведение последовательности составляет: {Multiplier_Calculus()}")

