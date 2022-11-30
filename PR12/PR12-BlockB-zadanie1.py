def m():
    x = int(input())
    if x == 0:
        return x
    else:
        return max(x, m())
print(m())