n = input()


def change_1_digit(input: str):
    list_digits = ['0', '2', '4', '6', '8']
    if input[0] == '0':
        return '00'
    elif input[1] in ['0', '4', '8']:
        return f"0{input[1]}"
    elif input[1] == '2':
        return 12
    elif input[1] == '6':
        return 16
    else:
        for last_digit in list_digits:
            cur_number = int(f"{input[0]}{last_digit}")
            if cur_number % 4 == 0:
                return cur_number


if len(n) == 2:
    print(12)
else:
    result = '1'
    remain_in_middle = 2
    remain_in_last = 2
    if int(n[-2:]) % 4 != 0:
        remain_in_middle = 1
        remain_in_last = 1

    if n[0] != '1':
        remain_in_middle = remain_in_middle - 1

    change = 0
    for index in range(1, len(n)-2):
        if change == remain_in_middle:
            result += n[index: len(n)-2]
            break

        if n[index] != '0':
            change += 1
        result += '0'

    remain_in_last -= change
    if remain_in_last == 2:
        result += '00'
    elif remain_in_last == 1:
        result += str(change_1_digit(n[-2:]))
    else:
        result += n[-2:]

    print(result)
