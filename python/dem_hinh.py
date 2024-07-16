n = int(input())
m = int(input())

result = 0
while n > 0 and m > 0:
    result += n * m
    n -= 2
    m -= 2

print(result)
