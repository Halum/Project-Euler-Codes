num = 0

with open('A.txt') as f:
    for i in f:
        data = int(i)
        num += data

print(num)
