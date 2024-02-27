import math

def axis(array):
    min_val = min(array)
    max_val = max(array)

    axis_length = max_val - min_val

    return axis_length

try:
    n = int(input("Введіть кількість елементів у послідовності: "))
    if n > 0:
        array = []

        print("Введіть елементи послідовності:")
        for i in range(n):
            element = float(input())
            array.append(element)

        length = axis(array)

        print("Найменша довжина числової осі:", length)
    else:
        print("Введіть правильне значення")
except ValueError:
    print("Введіть правильне значення")