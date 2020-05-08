def show(self, move, player, board):
    x = move // 15
    y = move % 15
    board[x][y] = player
    array = np.array(board)
    print(array)
    print("\n")


self.show(move, self.board.current_player, showboard)
