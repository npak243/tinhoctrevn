n = input()

len_n = len(n)
lucky_numbers_len_n = ['6' * pos + '8' * (len_n - pos) for pos in range(len_n, -1, -1)]
if n in lucky_numbers_len_n:
    # calculate position of n in total lucky numbers
    # for lucky number has len = 1, there are 2 lucky numbers: 6, 8
    # for lucky number has len = 2, there are 3 lucky numbers: 66, 68, 88
    # for lucky number has len = 3, there are 4 lucky numbers: 666, 668, 688, 888
    pos_n = lucky_numbers_len_n.index(n) + 1
    if (len_n - 1) > 0:
        # sum = (1+1) + (2+1) + (3+1) + (len_n-1 + 1) + pos_n
        # sum = (1+2+3+...+len_n-1) + len_n-1 + pos_n
        pos_in_set = (len_n - 1) * len_n // 2 + (len_n - 1) + pos_n
        print(pos_in_set)
    else:
        print(pos_n)
else:
    print("NO")
