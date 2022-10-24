from random import randint
a = [randint(1, 100) for i in range(10)]
b = [randint(1, 100) for i in range(10)]
print('Составлены 2 массива в диапазоне от 1 до 100 с размером 10')
print('1 список =' ,a)
print('2 список =' ,b)
a, b = b.copy(), a.copy()
print('1 список после замены =' ,*a)
print('2 список после замены =' ,*b)
