print("Введите список чисел: ")
a = list(filter(lambda x : x % 2, list(map(int, input().split()))))
print(min(a) if a else 0)