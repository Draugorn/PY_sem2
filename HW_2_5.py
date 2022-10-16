def Array_former():
    try:
        Array = []
        print("Пожалуйста, введте размер списка в виде целого положительного числа:")
        Ar_length = int(input())
        if Ar_length < 0:
            print("Пожалуйста, введте целое положительное число.")
            Array_former()
        for i in range (Ar_length+1):
            Array.append(i) 
    except ValueError:
        print("Пожалуйста, введте целое положительное число!")
        Array_former()
    return Array

Ar = Array_former()
print(f"Созданный массив = {Ar}")

def Array_mixer(array):
    Neue_Array = []

    for i in array:
        if i % 2 == 0:
            Neue_Array.append(array[i])
    for j in array:
        if j % 2 != 0:
            Neue_Array.append(array[j])
            Back_Ar = Neue_Array[::-1]
    return Back_Ar

Back_Ar = print(f"Перемешанный список: {Array_mixer(Ar)}")