import sys

test = False
mDict = dict()
for line in sys.stdin:
    if not line.strip() or line in ['\n', '\r\n']:
        test = True
    elif test == False:
        entry = line.split()
        mDict[entry[1]] = entry[0]
    elif test:
        if mDict.has_key(line):
            print( mDict[line] )
        else:
            print( "eh" )