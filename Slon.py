l = list(map(int, input().split()))
N = l[0]
color = l[1:]
count = [0] * 8
for c in color:
    count[c - 1] += 1
for i in range(8):
    print(i + 1, count[i], end=' ')
