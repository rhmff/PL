f = int(input())
k = int(input())
R = 0
if f < k:
	R = f + k * k - 1
	print(R)
elif k < 2 and f == 3:
	R = k * k
	print(R)
else:
	R = f - 1
	print(R)
