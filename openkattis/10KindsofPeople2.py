class Grp:
    def __init__(self):
        self.zero = []

    def addToDict(self, cord):
        zero_len = len(self.zero)

        cords = [ (cord[0]-1, cord[1]), (cord[0], cord[1]-1), (cord[0]+1, cord[1]),(cord[0], cord[1]+1) ]
        setadded = []
        for idx, v in enumerate(self.zero):
            if {cords[0]}.intersection(v) or {cords[1]}.intersection(v) or {cords[2]}.intersection(v) or {cords[3]}.intersection(v):
                v.add(cord)
                setadded.append(idx)

        if not setadded:
            self.zero.append({cord})
            return

        for i in setadded[1:]:
            self.zero[ setadded[0] ].update(self.zero[ i ])
            del self.zero[ i ]
    
    def searchDict(self, cord1, cord2):
        for v in self.zero:
            if {cord1, cord2} < v:
                return True
        return False


zeroObj = Grp()
oneObj = Grp()

f = open('sample-01.in', 'r')
rows, cols = map(int, f.readline().split())

for i in range(1, rows+1):
    for idx, c in enumerate(f.readline()):
        if c == "1":
            oneObj.addToDict((i, idx+1))
        elif c == "0":
            zeroObj.addToDict((i, idx+1))

print(oneObj.zero)

incords = int(f.readline())
for line in f.readlines():
    incord = list(map(int, line.split()))
    boolZero = zeroObj.searchDict( (incord[0], incord[1]), (incord[2], incord[3]))
    boolOne =  oneObj.searchDict( (incord[0], incord[1]), (incord[2], incord[3])) 

    if(boolZero and not boolOne):
        print("binary")
    elif(not boolZero and boolOne):
        print("decimal")
    elif(not boolZero and not boolOne):
        print("neither")

