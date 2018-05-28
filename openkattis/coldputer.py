import sys

a = 0
b = list()
for line in sys.stdin:
    if a == 0:
        a += 1
        continue
    b = list(map(int, line.split()))

less_than_zero = list(filter(lambda x: x < 0, b))
print(len(less_than_zero))