import string

n = 10
alphabet = string.ascii_lowercase

for i in reversed(range(n)):
    psu = alphabet[i:n]
    print(('-'.join(psu[:0:-1]+psu)).center(4*n-3,"-"))

for i in range(1,n):
    psu = alphabet[i:n]
    print(('-'.join(psu[:0:-1]+psu)).center(4*n-3,"-"))
