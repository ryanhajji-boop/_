bits = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

def denaryToHex(den):
    convert = den // 16
    rem = den % 16
    print(bits[convert],rem)
denaryToHex(163)

