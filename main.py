import math

n = int(input("Введіть кількість елементів у послідовності: "))
array = []

print("Введіть елементи послідовності:")
for i in range(n):
  element = float(input())
  array.append(element)

min_val = min(array)
max_val = max(array)

axis_length = max_val - min_val

print("Довжина осі:", axis_length)