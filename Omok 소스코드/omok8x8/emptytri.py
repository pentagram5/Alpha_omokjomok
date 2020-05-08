# empty triangle
for x in range(2,4 ):
    for y in range(3,5):
        if (omok.board[x][y] == 1 and omok.board[x + 1][y] == 1 and omok.board[x][y - 1] == 0 and omok.turn == 1):
            if (y > 0 and omok.board[x][y - 1] == 0):
                omok.board[x][y - 1] = 1
                omok.check_board_black(x, y - 1)
                human = Human(x, y - 1)
                game.start_play(human)