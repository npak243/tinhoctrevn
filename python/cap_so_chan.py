# https://tinhoctre.vn/problem/evenpair
# n = 5 => output = 9
# (1,2) (2,2) (2,3) (2,4) (2,5) (1,4) (3,4) (4,4) (4,5)
# 1 -> 5: have 5 numbers
# 1 -> 5: have 2 even numbers(2, 4) => 2 x 5 = 10 - 1 (duplicated (2,4) <--> (4,2)) = 9

n = int(input())

num_evens = n // 2
total = num_evens * n
total -= (num_evens - 1) * num_evens // 2
# (2, 4, 6, 8) -1, -2 , -3  => - (1 + 2 + 3) = - (n * (n+1)) // 2

print(total)
