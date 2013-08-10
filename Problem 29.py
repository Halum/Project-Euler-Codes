term = []

for i in range(2, 101):
    for j in range(2, 101):
        term.append( i ** j )

distinct = set( term )

print( len(distinct) )
