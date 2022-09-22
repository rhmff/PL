a = int(input())
b = int(input())
R = 0
if a < b:
	R = a - b + 1
	print(R)
elif a > b and a > 3:
	R = b * b - b
	print(R)
else:
	R = b *b -1
	print(R)
