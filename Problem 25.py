count = 2
fst = snd = 1


for i in range(3, 100000):
    fib = fst + snd
    fst = snd
    snd = fib
    if len( str( fib ) ) >= 1000:
        break
    
print(i)
