# !: 4 kyu

def recover_secret(triplets):
    secret = []
    for i in triplets:
        x = i[0]
        y = i[1]
        z = i[2]

        if x not in secret: # if x is in secret move to next if condition
            secret.insert(0,x)
        if y not in secret:
            secret.insert(secret.index(x), y) # insert y into the position where x is
        if y in secret and secret.index(y) < secret.index(x): # if y is in secret and i[1] comes before x pop it and put it ahead of it
            secret.pop(secret.index(y))
            secret.insert(secret.index(x)+1,y)
        if z not in secret:
            secret.insert(secret.index(y),z)
        if z in secret and secret.index(z) < secret.index(y):
            secret.pop(secret.index(z))
            secret.insert(secret.index(y)+1,z)
    print(''.join(secret))

triplets = [
          ['t','u','p'],
          ['w','h','i'],
          ['t','s','u'],
          ['a','t','s'],
          ['h','a','p'],
          ['t','i','s'],
          ['w','h','s']
        ]

recover_secret(triplets)