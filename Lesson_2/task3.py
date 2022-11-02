size = int(input("Input size: "))
for elem in reversed(range(size)):
    elem += 1
    while elem > 0:
        print(f"{elem} ", end = " " )
        if elem == 1:
            print("")
        elem -= 1