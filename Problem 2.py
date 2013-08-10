fst = 1
snd = 1
ans = 0
lim = 4000000


for i in range(1, lim):
    fib = fst + snd
    if fib > lim:
        break
    if fib % 2 == 0:
        ans += fib
    fst = snd
    snd = fib

print(ans)
    
