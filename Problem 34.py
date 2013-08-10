fact = [1, 1]

for i in range(2, 11):
    temp = fact[i-1] * i
    fact.append( temp )

def check( n ):
    num = str( n )
    Sum = 0

    for i in num:
        Sum += fact[int(i)]

    if Sum == n: return True
    else: return False

score = 0


for i in range(3, 55555):
    if check( i ) == True:
        print( i )
        score += i

print(score)
        
    

