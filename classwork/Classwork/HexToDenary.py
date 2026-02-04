bits = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

result = []
def HexToDenary(hex):
    for i in hex:
        if i in bits: # is it in the Bits? I.e. is it a-f?
            result.append(bits[i]*16)
        else: # else just add the number on its own
            result.append(int(i))
    sum = 0
    for i in result:
        sum = sum + i
    print(sum)
HexToDenary('A5')