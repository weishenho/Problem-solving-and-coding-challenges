import sys

for line in sys.stdin:
    source = line.split("-")
    for x in source:
        print(x[0], end="")