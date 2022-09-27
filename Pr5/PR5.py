stroka = input("Введите строку слов")
for i in stroka.split():
    if i.endswith("я"):
        print(i)