score = 0

with open('A.txt') as f:
    data = f.read()
    names = data.split(',')

for i in range(0, len(names) ):
    (a, b, c) = names[i].split('"')
    names[i] = b

names = sorted(names)

for i in range(0, len(names) ):
    temp = 0
    for j in range(0, len(names[i]) ):
        temp += ord( names[i][j]) - 64
    score += temp * (i+1)

print(score)
