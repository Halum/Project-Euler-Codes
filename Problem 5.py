def GCD( a, b ):
    if not b:
        return a

    return GCD(b, a%b)

def LCM(a, b):
    return int((a * b) / GCD(a, b))

ans = 1

for i in range (1, 21):
    ans = LCM(ans, i)

print(ans)
