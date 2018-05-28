import sys

s = [1, 0, 0]

def f(letter):
    if letter == "A":
        s[0], s[1] = s[1], s[0]
    elif letter == "B":
        s[1], s[2] = s[2], s[1]
    elif letter == "C":
        s[0], s[2] = s[2], s[0]

for line in sys.stdin:
    for x in line:
        f(x.upper())

print(s.index(1) + 1)