romandict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

number = "CCC"

converted = [romandict[i] for i in number]

s = 0

for i in range(len(converted)-1):
    s += converted[i] 
    if converted[i]<converted[i+1]:
        s-=2*converted[i]
s+=converted[-1]

print(s)