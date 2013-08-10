def Pandigit( a, b, c ):
    string = str(a) + str(b) + str(c)
    num = [0,0,0,0,0,0,0,0,0,0,]

    for i in string:
        temp = int(i)
        num[temp] = num[temp] + 1

    if num[0] > 0:
        return False

    for i in range(1, 10):
        if num[i] == 0 or num[i] > 1:
            return False

    return True


product = []

for i in range(1, 1001):
    for j in range(1, 2001):
        if Pandigit(i, j, i*j) == True:
            print(i*j)
            product.append(i*j)

distinct = set( product )

Sum = 0

for i in distinct:
    Sum += i

print(Sum)
    
