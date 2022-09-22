a = int(input())
b = int(input())
c = 0
if a < 2 and b > 3:
	c = a + b * b
	print(c)
elif a > b and a > 3:
	c = b * b + 2
	print(c)
else:
	c = b
	print(c)
