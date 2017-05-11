
path = "Key.bin"
with open(path, 'rb') as f:
    try:
        byte = " "
        while byte != "":
            # Do stuff with byte.
            byte1 = f.read(1)

            byte2 = f.read(1)
            byte3 = f.read(4)
            print byte1, byte2,byte3
    finally:
        f.close()

