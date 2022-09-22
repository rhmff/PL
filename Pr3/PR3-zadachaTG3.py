a = int(input())
b = int(input())
c = 0
if a < b:
	c = a + b
	print(c)
elif a > b and a > 3:
	c = b * b - b
	print(c)
else:
	c = b * b - 1
	print(c)
