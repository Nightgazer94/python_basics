def chessboard(n=8):
    board = []
    for i in range(n):
        if i % 2 == 0:
            row = "# " * 4
        else:
            row = " #" * 4
        board.append(row)
    return "\n".join(board)

print (chessboard())