# довольно долгий способ поиска и отбора, но рабочий
# P.S. Владимир Владимирович, если есть более быстрый способ решения, отправьте в беседу в тг :)
limit = int(input("Введите ограничение: ")) # задаем ограничение области поиска
a = {}
def divisors_sum(number):
    return sum(x for x in range(1, (number // 2) + 1) if number % x == 0)
for i in range(1, limit + 1):
    aggr = divisors_sum(i)
    if i == divisors_sum(aggr) and i != aggr:
        if i and aggr not in a:
            a[i] = aggr
print(a)
