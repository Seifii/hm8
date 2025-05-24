x = list(map(int, input().split()))
n = x[0]
m = x[1]
a = x[2:]
a.sort(reverse=True)
s = 0
k = 0
for l in a:
    s += l
    k += 1
    if s >= n:
        print(k)
        break
else:
    print(0)
