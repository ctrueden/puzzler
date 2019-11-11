def binstr(n):
    return str(bin(n))[2:]

def pal(s):
    return s == s[::-1]

def double_pal(x):
    return pal(str(x)) and pal(binstr(x))

total = sum(i for i in range(1000000) if double_pal(i))
print(total)
