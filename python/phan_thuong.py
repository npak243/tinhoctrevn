# https://tinhoctre.vn/problem/bonus

ifirst_line = input().split(' ')
n, k = int(ifirst_line[0]), int(ifirst_line[1])

board = {}

# read the next k lines
for line in range(0, k):
    gift_pos = input().split(' ')
    irow = int(gift_pos[0])
    icol = int(gift_pos[1])
    gift = int(gift_pos[2])
    # update the board position with max bonus
    board[irow * n + icol] = -1
    # (row,col) => (row+1,col-2), (row+2,col-1), (row+1,col+2), (row+2,col+1)
    # (row,col) => (row-1,col-2), (row-2,col-1), (row-1,col+2), (row-2,col+1)
    # ---------------
    # (row,col) => (row+-1,col+-2), (row+-2,col+-1)
    change_row = [1, -1, 2, -2, 1, -1, 2, -2]
    change_col = [-2, -2, -1, -1, 2, 2, 1, 1]
    for index in range(0, 8):
        cur_row = irow + change_row[index]
        cur_col = icol + change_col[index]
        if cur_row == 0 or cur_row > n or cur_col == 0 or cur_col > n:
            continue
        pos = cur_row * n + cur_col
        if board.get(pos) == -1:
            continue
        board[pos] = board.get(pos, 0) + gift

print(max(board.values()))
