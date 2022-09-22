a = int(input())
x = int(input())
y = 0
if (a > 5) and (x == 3):
	y = x + a
	print(y)
elif (a == 4) or (x < 2):
	y = x * a
	print(y)
else:
	y = x ** a
	print(y)
