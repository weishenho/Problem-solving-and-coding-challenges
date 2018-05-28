import sys

for line in sys.stdin:
    line = line.strip()
    s = list(map(int, line.split(" ")))
    if s[1]>= 45:
        print(str(s[0]) + " " + str(s[1] - 45))
    else:
        b = 60 - 45 + s[1]
        a = 23 if s[0] == 0 else (s[0] - 1)
        print(str(a) + " " + str(b))