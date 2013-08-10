def sum( n ):
    return ( n * (n + 1) / 2 )

def sqrsum( n ):
    return ( n * (n + 1) * (2 * n + 1) / 6  )


data = int( input())

print( sum(data) * sum(data) - sqrsum(data) )
