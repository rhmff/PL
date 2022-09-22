a = int(input())
b = int(input())
x = 0
if a < b:
	x = 2 * a + 2 * b
	print(x)
elif a > b:
	x = a - b + 1
	print(x)
elif a == b:
	x = b * b
	print(x)

