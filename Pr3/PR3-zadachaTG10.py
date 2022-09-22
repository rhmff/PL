k = int(input())
c = int(input())
x = 0
if k < 5 and c > 4:
	x = k + c * c
	print(x)
elif k > c and k > 3:
	x = c * c + 2
	print(x)
else:
	x = c - 1
	print(x)
