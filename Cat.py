w = list(map(int, input().split()))
N = w[0]
weights = w[1]
min_w = min(w)
max_w = max(w)
sum_w = (sum(w) - w[0])
print(max_w)
print(min_w)
print(sum_w)
