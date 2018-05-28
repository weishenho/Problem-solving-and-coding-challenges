import sys

linenum = 1
n = 0
for line in sys.stdin:
    if linenum == 1:
        n = int(line.strip())
        linenum += 1
    else:
        if n > linenum:
            break
        linenum += 1
        x = line.split()
        print( f( int(x[0].strip()), int(x[1].strip()), int(x[2].strip()) ) )

def f(r, e, c):
    p = e - c
    if r > p : return "do not advertise"
    if p > r : return "advertise"
    if p == r : return "does not matter"