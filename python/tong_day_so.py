n = int(input())
m = int(input())

# 1, N, 2, N-1, 3, N-2, ...
# 1, 6, 2, 5, 3, 4 <-- N = 6
if m % 2 == 0:
    result = (m // 2) * (n + 1)
else:
    result = (m // 2) * (n + 1) + (m // 2) + 1

print(result)
