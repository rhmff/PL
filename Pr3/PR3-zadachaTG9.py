f = int(input())
v = int(input())
S = 0
if f < 4 and v > 6:
	S = f + v
	print(S)
elif v < 6:
	S = f * f
	print(S)
else:
	S = 2 * v
	print(S)
