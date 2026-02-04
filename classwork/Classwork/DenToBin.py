import math # needed for log to find how many bits are needed to represent that number
bits = [] # store the bits

def convertDenaryToBinary(number):
    bitsNeeded = (math.log2(number))
    
    bits.append(number % 2) # append the starting bit

    for i in range(1,bitsNeeded): # we know the times we need to divide 
        number = number // 2 # divide the number for the next iteration
        bits.append(number % 2) # find the bit by finding the remainder with MOD

    bits.reverse() # reverse the bits because this method goes from R to L and we need L to R
    print(bits) 

convertDenaryToBinary(584) 