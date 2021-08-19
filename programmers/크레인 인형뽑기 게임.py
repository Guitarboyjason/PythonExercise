board = [[0,0,0,0,0]\
    ,[0,0,1,0,3]\
    ,[0,2,5,0,1]\
    ,[4,2,4,4,2]\
    ,[3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]
pick = []
result = 0
board_row = []
for i in range(len(board)):
    for j in range(len(board)):
        if j == 0:
            board_row.append([board[j][i]])
        else:
            board_row[i].append(board[j][i])

for i in moves:
    for j in range(len(board_row[i-1])):
        if len(pick) == 0:
            pick.append(board_row[i-1][j])
        if board_row[i-1][j] != 0:
            if pick[-1] == board_row[i-1][j]:
                result += 1
                pick = pick[:-1]
            else:
                pick.append(board_row[i-1][j])
            board_row[i-1][j] = 0
print(result)
