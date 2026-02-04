def decimal_to_binary(decimal_num, fractional_places=10):
   
    integer_part = int(decimal_num)
    fractional_part = decimal_num - integer_part
    
    integer_binary = ""
    temp = integer_part
    if temp == 0:
        integer_binary = "0"
    else:
        while temp > 0:
            integer_binary = str(temp % 2) + integer_binary
            temp //= 2
    
    fractional_binary = ""
    for _ in range(fractional_places):
        fractional_part *= 2
        if fractional_part >= 1:
            fractional_binary += "1"
            fractional_part -= 1
        else:
            fractional_binary += "0"
    
    print(f"{integer_binary}.{fractional_binary}")

decimal_to_binary(101.233)