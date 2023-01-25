N = int(input())
X = list(map(int,input().split()))
sorted_X = sorted(list(set(X)))
x_idx = {}
idx = 0
for x in sorted_X:
    x_idx[x] = idx
    idx += 1
for x in X:
    print(x_idx[x], end = ' ')