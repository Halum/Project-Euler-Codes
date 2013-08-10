score = 0

def DigitSum( num ):
    res = 0
    for i in range(0, len(num) ):
        temp = int( num[i] )
        res += temp ** 5
    return res

for i in range(1000, 999999):
    if DigitSum( str(i) ) == i:
        print(i)
        score += i

print(score)
