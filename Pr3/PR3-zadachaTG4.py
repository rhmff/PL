v = int(input())
k = int(input())
z = 0
if v < k:
	z = v - k + 1
	print(z)
elif k > v:
	z = k * k - v * v
	print(z)
else:
	z = k * k - k
	print(z)
