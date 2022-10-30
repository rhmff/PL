import math
def mediana(a, b, c):
    mediana = (math.sqrt(2 * (b ** b) + 2 * (c ** c) - (a ** a))) / 2
    return mediana
print("Введите размеры треугольника")
x = int(input())
y = int(input())
z = int(input())
if x > y + z or y > x + z or z > x + y:
    print("Такого треугольника не существует!!!")
M = mediana(x, y, z)
print(M)
