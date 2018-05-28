import sys


for idx, line in enumerate(sys.stdin):
    if idx == 0: continue
    num = int(line.strip())
    if num % 2 == 0:
        print(line, "is even")
    else:
        print(line, "is odd")
