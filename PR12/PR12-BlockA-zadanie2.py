a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def ost(a):
    if b == 0:
        print("На ноль делить нельзя!")
        return(" ")
    return a % b
print(ost(a))