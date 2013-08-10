

Sum = 0


for i in range(1, 1001):
    Sum +=  i ** i

string = str(Sum)
length = len( string )

#print(Sum)
print( string[length-10 : length] )
