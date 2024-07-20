# https://tinhoctre.vn/problem/tht2022a_phansonhonhat

a = int(input())
b = int(input())
c = int(input())

numerator = min(a, b, c)
denominator = max(a, b, c)

if denominator % numerator == 0:
    result = (denominator // numerator) + 1
elif (
    (denominator % (denominator - numerator) == 0) and
    (numerator % (denominator - numerator) == 0)
):
    result = int(
        (denominator // (denominator - numerator)) +
        (numerator // (denominator - numerator))
    )
else:
    result = denominator + numerator

print(result)
