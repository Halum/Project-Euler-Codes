ans = 0;

threes = []

for i in range (1, 500):
    if 3 * i >= 1000:
        break
    threes.append( i * 3 )
    ans += 3 * i

for i in range (1, 500):
    tmp = i * 5
    if tmp >= 1000:
        break
    if tmp not in threes:
        ans += tmp

print(ans)
