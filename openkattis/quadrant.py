    import sys

    c = 0
    ie = [0,0]
    for line in sys.stdin:
        ie[c] = int(line.strip())
        c += 1
        if c > 1:
            break


    if ie[0] > 0 and ie[1] > 0:
        print("1")
    elif ie[0] < 0 and ie[1] > 0:
        print("2")
    elif ie[0] < 0 and ie[1] < 0:
        print("3")
    else:
        print("4")

