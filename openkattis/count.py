import sys, re

result = set()

inputs = [line.strip() for line in sys.stdin]

for x in inputs[2:]:
    if not re.findall("^[0-9]+$", x):
        result.add(x)
    else:
        print(str(len(result)))
        result.clear()

print(str(len(result)))