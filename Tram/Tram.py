t = int(input())

cap = 0
maxC = 0

for _ in range(t):
    n, k = list(map(int,input().split()))

    cap -= n
    cap += k
    maxC = max(maxC, cap)
print(maxC)
