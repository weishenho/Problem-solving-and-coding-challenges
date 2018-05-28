import sys

target = [1, 1, 2, 2, 2, 8]
for line in sys.stdin:
    source = map(int, line.split())
    result = list(map(lambda x, y: x - y, target, source))
    print(" ".join(map(str,result)))