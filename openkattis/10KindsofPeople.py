
zero = {}
one = {}
print(zero, one)

f = open('sample-01.in', 'r')
rows, cols = map(int, f.readline().split())

def findZeroGrp(cord):
    zero_len = len(zero)

    if not zero:
        zero[0] = set()
        zero[0].add(cord)

    cords = [ (cord[0]-1, cord[1]), (cord[0], cord[1]-1), (cord[0]+1, cord[1]),(cord[0], cord[1]+1)  ]
    setadded = []
    for k, v in zero.items():
        if {cords[0]}.intersection(v) or {cords[1]}.intersection(v) or {cords[2]}.intersection(v) or {cords[3]}.intersection(v):
            zero[k].add(cord)
            setadded.append(k)

    if not setadded:
        for num in range(0, zero_len+1):
            if num not in zero:
                zero[num] = {cord}
                break

    setadded_len = len(setadded)
    if setadded_len > 1:
        setadded.sort()
        for i in range(1, setadded_len):
            zero[ setadded[0] ].update(zero[ setadded[i] ])
            zero.pop(setadded[i])
        



def findOneGrp(cord):
    pass


for i in range(0, rows):
    col = 0
    for c in f.readline():
        if c == "1":
            findZeroGrp((i, col))
        else:
            findOneGrp((i, col))
        col += 1

print(zero)
print(one)