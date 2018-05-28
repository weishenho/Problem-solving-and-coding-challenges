import sys

a = 0
b = 0
for line in sys.stdin:
    if a == 0:
        continue
    b =  line.split()

print(int(a) * (int(b) -1) + 1)

