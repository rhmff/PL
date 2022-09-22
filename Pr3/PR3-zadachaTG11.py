x = int(input())
y = int(input())
q = 0
if x == 4 and y < 2:
	q = x + x * y
	print(q)
elif x < y:
	q = y * y
	print(q)
else:
	q = y * y + 4
	print(q)

