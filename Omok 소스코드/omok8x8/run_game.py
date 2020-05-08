from Omok import *
import pygame, sys
import random
import pickle
from pygame.locals import *
from rule import *
#black attat first  #whtie defense first
#from policy_value_net_pytorch import PolicyValueNet
from policy_value_net_numpy import PolicyValueNetNumpy

from game import Board, Game
from mcts_alphaZero import MCTSPlayer


fps = 60
fps_clock = pygame.time.Clock()



class Human(object):
    """
    human player
    흑수 관련 구조체, 포인트 x,y 와 턴을 넘겨줘야함
    """

    def __init__(self, x, y):
        self.player = None
        self.x = x
        self.y = y

    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board):
        move = board.location_to_move(self.x, self.y)
        "xy입력받아서, 1차원 move로 변환하여 리턴해준다. "
        return move

def run_game(surface, omok, menu):
    omok.init_game()  # board = 0 ~ 7
    omok.id=0
    board = Board(width=8, height=8, n_in_row=5)
    game = Game(board)
    model_file = 'best_policy_8_8_5.model'

    while True:
        # balck stone
        if (omok.id == 0):
            a = random.randint(3, 4)
            b = random.randint(3, 4)
            print('first stone', a, b)
            omok.board[a][b] = 1
            omok.check_board_black(a ,b )
            human = Human(a, b)
            game.start_play(human)


        elif (omok.turn == 1 and omok.id > 1):
            # 4 defense, 4attack, 3 defense, 3 attack
            # 4 defense code
            #  right under 4 defense
            for x in range(0, 4):
                for y in range(0, 4):  ## 0~11 +4 max = 15
                    if (omok.board[x][y] == 2 and omok.board[x + 1][y + 1] == 2 and omok.board[x + 2][y + 2] == 2
                            and omok.board[x + 3][y + 3] == 2 and omok.turn == 1):
                        if (omok.board[x + 4][y + 4] == 0):
                            omok.board[x + 4][y + 4] = 1
                            omok.check_board_black(x + 4, y + 4)
                            human = Human(x + 4, y + 4)
                            game.start_play(human)


                        elif (x > 0 and y > 0 and omok.board[x - 1][y - 1] == 0):
                            omok.board[x - 1][y - 1] = 1
                            omok.check_board_black(x - 1, y - 1)
                            human = Human(x - 1, y - 1)
                            game.start_play(human)


                    elif (omok.board[x][y] == 2 and omok.board[x + 1][y + 1] == 0 and omok.board[x + 2][y + 2] == 2
                          and omok.board[x + 3][y + 3] == 2 and omok.turn == 1):
                        omok.board[x + 1][y + 1] = 1
                        omok.check_board_black(x + 1, y + 1)
                        human = Human(x + 1, y + 1)
                        game.start_play(human)


                    elif (omok.board[x][y] == 2 and omok.board[x + 1][y + 1] == 2 and omok.board[x + 2][y + 2] == 0
                          and omok.board[x + 3][y + 3] == 2 and omok.turn == 1):
                        omok.board[x + 2][y + 2] = 1
                        omok.check_board_black(x + 2, y + 2)
                        human = Human(x + 2, y + 2)
                        game.start_play(human)
            # left under 4 defense
            for x in range(4, 7):  # 3 ~ 14
                for y in range(0, 4):
                    if (omok.board[x][y] == 2 and omok.board[x - 1][y + 1] == 2 and omok.board[x - 2][
                        y + 2] == 2
                            and omok.board[x - 3][y + 3] == 2 and omok.turn == 1):
                        if (y > 0 and omok.board[x + 1][y - 1] == 0):
                            omok.board[x + 1][y - 1] = 1
                            omok.check_board_black(x + 1, y - 1)
                            human = Human(x + 1, y - 1)
                            game.start_play(human)


                        elif (omok.board[x - 4][y + 4] == 0):
                            omok.board[x - 4][y + 4] = 1
                            omok.check_board_black(x - 4, y + 4)
                            human = Human(x - 4, y + 4)
                            game.start_play(human)


                    elif (omok.board[x][y] == 2 and omok.board[x - 1][y + 1] == 0 and omok.board[x - 2][
                        y + 2] == 2
                          and omok.board[x - 3][y + 3] == 2 and omok.turn == 1):
                        omok.board[x - 1][y + 1] = 1
                        omok.check_board_black(x - 1, y + 1)
                        human = Human(x - 1, y + 1)
                        game.start_play(human)


                    elif (omok.board[x][y] == 2 and omok.board[x - 1][y + 1] == 2 and omok.board[x - 2][
                        y + 2] == 0
                          and omok.board[x - 3][y + 3] == 2 and omok.turn == 1):
                        omok.board[x - 2][y + 2] = 1
                        omok.check_board_black(x - 2, y + 2)
                        human = Human(x - 2, y + 2)
                        game.start_play(human)
            #   -> 4 defense
            for x in range(0, 4):
                for y in range(0, 8):
                    if (omok.board[x][y] == 2 and omok.board[x + 1][y] == 2 and omok.board[x + 2][
                        y] == 2 and
                            omok.board[x + 3][y] == 2 and omok.turn == 1):
                        if (omok.board[x + 4][y] == 0):
                            omok.board[x + 4][y] = 1
                            omok.check_board_black(x + 4, y)
                            human = Human(x + 4, y)
                            game.start_play(human)


                        elif (x > 0 and omok.board[x - 1][y] == 0):
                            omok.board[x - 1][y] = 1
                            omok.check_board_black(x - 1, y)
                            human = Human(x - 1, y)
                            game.start_play(human)



                    elif (omok.board[x][y] == 2 and omok.board[x + 1][y] == 0 and omok.board[x + 2][
                        y] == 2 and
                          omok.board[x + 3][y] == 2 and omok.turn == 1):
                        omok.board[x + 1][y] = 1
                        omok.check_board_black(x + 1, y)
                        human = Human(x + 1, y)
                        game.start_play(human)


                    elif (omok.board[x][y] == 2 and omok.board[x + 1][y] == 2 and omok.board[x + 2][
                        y] == 0 and
                          omok.board[x + 3][y] == 2 and omok.turn == 1):
                        omok.board[x + 2][y] = 1
                        omok.check_board_black(x + 2, y)
                        human = Human(x + 2, y)
                        game.start_play(human)
            # to under 4 defense
            for x in range(0, 8):
                for y in range(0, 4):
                    if (omok.board[x][y] == 2 and omok.board[x][y + 1] == 2 and omok.board[x][y + 2] == 2 and
                            omok.board[x][y + 3] == 2 and omok.turn == 1):
                        if (omok.board[x][y + 4] == 0):
                            omok.board[x][y + 4] = 1
                            omok.check_board_black(x, y + 4)
                            human = Human(x, y + 4)
                            game.start_play(human)


                        elif (y > 0 and omok.board[x][y - 1] == 0):
                            omok.board[x][y - 1] = 1
                            omok.check_board_black(x, y - 1)
                            human = Human(x, y - 1)
                            game.start_play(human)


                    elif (omok.board[x][y] == 2 and omok.board[x][y + 1] == 0 and omok.board[x][y + 2] == 2 and
                          omok.board[x][y + 3] == 2 and omok.turn == 1):
                        omok.board[x][y + 1] = 1
                        omok.check_board_black(x, y + 1)
                        human = Human(x, y + 1)
                        game.start_play(human)


                    elif (omok.board[x][y] == 2 and omok.board[x][y + 1] == 2 and omok.board[x][y + 2] == 0 and
                          omok.board[x][y + 3] == 2 and omok.turn == 1):
                        omok.board[x][y + 2] = 1
                        omok.check_board_black(x, y + 2)
                        human = Human(x, y + 2)
                        game.start_play(human)

                # condition1 = fair  position
                # place  the black stone near the place where the black stone gathers

            # 4 attack code
            # right under 4 attack
            for x in range(0, 4):  # 12
                for y in range(0, 4):  # 12
                    if (omok.board[x][y] == 1 and omok.board[x + 1][y + 1] == 1 and omok.board[x + 2][
                        y + 2] == 1
                            and omok.board[x + 3][y + 3] == 1 and omok.turn == 1):
                        if (omok.board[x + 4][y + 4] == 0):
                            omok.board[x + 4][y + 4] = 1
                            omok.check_board_black(x + 4, y + 4)
                            human = Human(x + 4, y + 4)
                            game.start_play(human)

                        elif (x > 0 and y > 0 and omok.board[x - 1][y - 1] == 0):
                            omok.board[x - 1][y - 1] = 1
                            omok.check_board_black(x - 1, y - 1)
                            human = Human(x - 1, y - 1)
                            game.start_play(human)


                    elif (omok.board[x][y] == 1 and omok.board[x + 1][y + 1] == 0 and omok.board[x + 2][
                        y + 2] == 1
                          and omok.board[x + 3][y + 3] == 1 and omok.turn == 1):
                        omok.board[x + 1][y + 1] = 1
                        omok.check_board_black(x + 1, y + 1)
                        human = Human(x + 1, y + 1)
                        game.start_play(human)

                    elif (omok.board[x][y] == 1 and omok.board[x + 1][y + 1] == 1 and omok.board[x + 2][
                        y + 2] == 0
                          and omok.board[x + 3][y + 3] == 1 and omok.turn == 1):
                        omok.board[x + 2][y + 2] = 1
                        omok.check_board_black(x + 2, y + 2)
                        human = Human(x + 2, y + 2)
                        game.start_play(human)
            # left under 4 attack
            for x in range(4, 7):  # 3 ~ 14 # 3,15
                for y in range(0, 4):
                    if (omok.board[x][y] == 1 and omok.board[x - 1][y + 1] == 1 and omok.board[x - 2][
                        y + 2] == 1
                            and omok.board[x - 3][y + 3] == 1 and omok.turn == 1):
                        if (x < 7 and y > 0 and omok.board[x + 1][y - 1] == 0):
                            omok.board[x + 1][y - 1] = 1
                            omok.check_board_black(x + 1, y - 1)
                            human = Human(x + 1, y - 1)
                            game.start_play(human)


                        elif (omok.board[x - 4][y + 4] == 0):
                            omok.board[x - 4][y + 4] = 1
                            omok.check_board_black(x - 4, y + 4)
                            human = Human(x - 4, y + 4)
                            game.start_play(human)


                    elif (omok.board[x][y] == 1 and omok.board[x - 1][y + 1] == 0 and omok.board[x - 2][
                        y + 2] == 1
                          and omok.board[x - 3][y + 3] == 1 and omok.turn == 1):
                        omok.board[x - 1][y + 1] = 1
                        omok.check_board_black(x - 1, y + 1)
                        human = Human(x - 1, y + 1)
                        game.start_play(human)



                    elif (omok.board[x][y] == 1 and omok.board[x - 1][y + 1] == 1 and omok.board[x - 2][
                        y + 2] == 0
                          and omok.board[x - 3][y + 3] == 1 and omok.turn == 1):
                        omok.board[x - 2][y + 2] = 1
                        omok.check_board_black(x - 2, y + 2)
                        human = Human(x - 2, y + 2)
                        game.start_play(human)
            #  -> 4 attack
            for x in range(0, 4):  # 12
                for y in range(0, 8):  # 12
                    if (omok.board[x][y] == 1 and omok.board[x + 1][y] == 1 and omok.board[x + 2][
                        y] == 1 and
                            omok.board[x + 3][y] == 1 and omok.turn == 1):
                        if (omok.board[x + 4][y] == 0):
                            omok.board[x + 4][y] = 1
                            omok.check_board_black(x + 4, y)
                            human = Human(x + 4, y)
                            game.start_play(human)


                        elif (x > 0 and omok.board[x - 1][y] == 0):
                            omok.board[x - 1][y] = 1
                            omok.check_board_black(x - 1, y)
                            human = Human(x - 1, y)
                            game.start_play(human)


                    elif (omok.board[x][y] == 1 and omok.board[x + 1][y] == 0 and omok.board[x + 2][
                        y] == 1 and
                          omok.board[x + 3][y] == 1 and omok.turn == 1):
                        omok.board[x + 1][y] = 1
                        omok.check_board_black(x + 1, y)
                        human = Human(x + 1, y)
                        game.start_play(human)


                    elif (omok.board[x][y] == 1 and omok.board[x + 1][y] == 1 and omok.board[x + 2][
                        y] == 0 and
                          omok.board[x + 3][y] == 1 and omok.turn == 1):
                        omok.board[x + 2][y] = 1
                        omok.check_board_black(x + 2, y)
                        human = Human(x + 2, y)
                        game.start_play(human)
            # to under 4 attack
            for x in range(0, 8):  # 15
                for y in range(0, 4):  # 12
                    if (omok.board[x][y] == 1 and omok.board[x][y + 1] == 1 and omok.board[x][y + 2] == 1 and
                            omok.board[x][y + 3] == 1 and omok.turn == 1):
                        if (omok.board[x][y + 4] == 0):
                            omok.board[x][y + 4] = 1
                            omok.check_board_black(x, y + 4)
                            human = Human(x , y+4)
                            game.start_play(human)


                        elif (y > 0 and omok.board[x][y - 1] == 0):
                            omok.board[x][y - 1] = 1
                            omok.check_board_black(x, y - 1)
                            human = Human(x , y - 1)
                            game.start_play(human)


                    elif (omok.board[x][y] == 1 and omok.board[x][y + 1] == 0 and omok.board[x][y + 2] == 1 and
                          omok.board[x][y + 3] == 1 and omok.turn == 1):
                        omok.board[x][y + 1] = 1
                        omok.check_board_black(x, y + 1)
                        human = Human(x, y + 1)
                        game.start_play(human)


                    elif (omok.board[x][y] == 1 and omok.board[x][y + 1] == 1 and omok.board[x][y + 2] == 0 and
                          omok.board[x][y + 3] == 1 and omok.turn == 1):
                        omok.board[x][y + 2] = 1
                        omok.check_board_black(x, y + 2)
                        human = Human(x, y + 2)
                        game.start_play(human)

            # 3 defense
            # right under 3 defense
            for x in range(0, 5):  # 0~12 +3 max =15
                for y in range(0, 5):
                    if (omok.board[x][y] == 2 and omok.board[x + 1][y + 1] == 2 and omok.board[x + 2][
                        y + 2] == 2 and omok.turn == 1):
                        if (omok.board[x + 3][y + 3] == 0):
                            omok.board[x + 3][y + 3] = 1
                            omok.check_board_black(x + 3, y + 3)
                            human = Human(x + 3, y + 3)
                            game.start_play(human)


                        elif (y > 0 and x > 0 and omok.board[x - 1][y - 1] == 0):
                            omok.board[x - 1][y - 1] = 1
                            omok.check_board_black(x - 1, y - 1)
                            human = Human(x - 1, y - 1)
                            game.start_play(human)
            # left under 3 defense
            for x in range(3, 7):
                for y in range(0, 5):
                    if (omok.board[x][y] == 2 and omok.board[x - 1][y + 1] == 2 and omok.board[x - 2][
                        y + 2] == 2
                            and omok.turn == 1):
                        if (y > 0 and omok.board[x + 1][y - 1] == 0):
                            omok.board[x + 1][y - 1] = 1
                            omok.check_board_black(x + 1, y - 1)
                            human = Human(x + 1, y - 1)
                            game.start_play(human)


                        elif (omok.board[x - 3][y + 3] == 0):
                            omok.board[x - 3][y + 3] = 1
                            omok.check_board_black(x - 3, y + 3)
                            human = Human(x - 3, y + 3)
                            game.start_play(human)
                #  -> defense
            # > 3 defense
            for x in range(0, 5):
                for y in range(0, 8):
                    if (omok.board[x][y] == 2 and omok.board[x + 1][y] == 2 and omok.board[x + 2][y] == 2 and
                            omok.turn == 1):
                        if (omok.board[x + 3][y] == 0):
                            omok.board[x + 3][y] = 1
                            omok.check_board_black(x + 3, y)
                            human = Human(x + 3, y)
                            game.start_play(human)


                        elif (x > 0 and omok.board[x - 1][y] == 0):
                            omok.board[x - 1][y] = 1
                            omok.check_board_black(x - 1, y)
                            human = Human(x - 1, y)
                            game.start_play(human)
                # to under defense
            # under 3 defense
            for x in range(0, 8):
                for y in range(0, 5):  # 0~12 for i in range(0,14)
                    if (omok.board[x][y] == 2 and omok.board[x][y + 1] == 2 and omok.board[x][y + 2] == 2 and
                            omok.turn == 1):
                        if (omok.board[x][y + 3] == 0):
                            omok.board[x][y + 3] = 1
                            omok.check_board_black(x, y + 3)
                            human = Human(x, y + 3)
                            game.start_play(human)


                        elif (y > 0 and omok.board[x][y - 1] == 0):
                            omok.board[x][y - 1] = 1
                            omok.check_board_black(x, y - 1)
                            human = Human(x, y - 1)
                            game.start_play(human)
            # 3 attack
            # right under 3 attack
            for x in range(0, 5):
                for y in range(0, 5):  # 13
                    if (omok.board[x][y] == 1 and omok.board[x + 1][y + 1] == 1 and omok.board[x + 2][
                        y + 2] == 1 and omok.turn == 1):
                        if (omok.board[x + 3][y + 3] == 0):
                            omok.board[x + 3][y + 3] = 1
                            omok.check_board_black(x + 3, y + 3)
                            human = Human(x+3, y+3)
                            game.start_play(human)

                        elif (y > 0 and x > 0 and omok.board[x - 1][y - 1] == 0):
                            omok.board[x - 1][y - 1] = 1
                            omok.check_board_black(x - 1, y - 1)
                            human = Human(x - 1, y - 1)
                            game.start_play(human)
            # left under attack
            for x in range(3, 7):  # 2 ~ 14 # 2,15
                for y in range(0, 5):  # 13
                    if (omok.board[x][y] == 1 and omok.board[x - 1][y + 1] == 1 and omok.board[x - 2][y + 2] == 1 and omok.turn == 1):
                        if (x < 7 and y > 0 and omok.board[x + 1][y - 1] == 0):
                            omok.board[x + 1][y - 1] = 1
                            omok.check_board_black(x + 1, y - 1)
                            human = Human(x + 1, y - 1)
                            game.start_play(human)
                        elif (omok.board[x - 3][y + 3] == 0):
                            omok.board[x - 3][y + 3] = 1
                            omok.check_board_black(x - 3, y + 3)
                            human = Human(x - 3, y + 3)
                            game.start_play(human)
            # -> attack
            # > 3 attack
            for x in range(0, 5):  # 4
                for y in range(0, 8):  # 7
                    if (omok.board[x][y] == 1 and omok.board[x + 1][y] == 1 and omok.board[x + 2][y] == 1 and
                            omok.turn == 1):
                        if (omok.board[x + 3][y] == 0):
                            omok.board[x + 3][y] = 1
                            omok.check_board_black(x + 3, y)
                            human = Human(x + 3, y)
                            game.start_play(human)


                        elif (x > 0 and omok.board[x - 1][y] == 0):
                            omok.board[x - 1][y] = 1
                            omok.check_board_black(x - 1, y)
                            human = Human(x - 1, y)
                            game.start_play(human)
            # to under attack
            for x in range(0, 8):  # 15
                for y in range(0, 5):  # 13
                    if (omok.board[x][y] == 1 and omok.board[x][y + 1] == 1 and omok.board[x][y + 2] == 1 and
                            omok.turn == 1):
                        if (omok.board[x][y + 3] == 0):
                            omok.board[x][y + 3] = 1
                            omok.check_board_black(x, y + 3)
                            human = Human(x , y+3)
                            game.start_play(human)


                        elif (y > 0 and omok.board[x][y - 1] == 0):
                            omok.board[x][y - 1] = 1
                            omok.check_board_black(x, y - 1)
                            human = Human(x , y-1)
                            game.start_play(human)
            # left under attack
            for x in range(3, 7):  # 2 ~ 14 # 2,15
                for y in range(0, 5):  # 13
                    if (omok.board[x][y] == 1 and omok.board[x - 1][y + 1] == 1 and omok.board[x - 2][y + 2] == 1
                            and omok.turn == 1):
                        if (x < 7 and y > 0 and omok.board[x + 1][y - 1] == 0):
                            omok.board[x + 1][y - 1] = 1
                            omok.check_board_black(x + 1, y - 1)
                            human = Human(x + 1, y-1)
                            game.start_play(human)


                        elif (omok.board[x - 3][y + 3] == 0):
                            omok.board[x - 3][y + 3] = 1
                            omok.check_board_black(x - 3, y + 3)
                            human = Human(x -3 , y+3)
                            game.start_play(human)

            # defense code

            # empty triangle
            """for x in range(2, 4):
                for y in range(3, 5):
                    if (omok.board[x][y] == 1 and omok.board[x + 1][y] == 1 and omok.board[x][
                        y - 1] == 0 and omok.turn == 1):
                        if (y > 0 and omok.board[x][y - 1] == 0):
                            omok.board[x][y - 1] = 1
                            omok.check_board_black(x, y - 1)
                            human = Human(x, y - 1)
                            game.start_play(human)"""



            if (omok.turn != 2 and omok.id !=0):
                movelist = list()
                countlist = list()
                for a in range(1, 7):  # 1 ~ 6
                    for b in range(1, 7):  # 1 ~ 6
                        count = 0
                        if (omok.board[a][b] != 0):  # a b =!0
                            pass
                        else:
                            if (omok.board[a - 1][b - 1] == 1):
                                count = count + 1
                            if (omok.board[a][b - 1] == 1):
                                count = count + 1
                            if (omok.board[a + 1][b - 1] == 1):
                                count = count + 1
                            if (omok.board[a - 1][b] == 1):
                                count = count + 1
                            if (omok.board[a + 1][b] == 1):
                                count = count + 1
                            if (omok.board[a - 1][b + 1] == 1):
                                count = count + 1
                            if (omok.board[a][b + 1] == 1):
                                count = count + 1
                            if (omok.board[a + 1][b + 1] == 1):
                                count = count + 1
                            xymove = str(a) + ',' + str(b)  # (a,b) list add (1,1) , (1,2)
                            movelist.append(xymove)  # xy's move list add(1,1 ~ 13,13)
                            countlist.append(count)  # 모든 좌표마다의 가중치 값을 카운트 리스트에 넣음 [0 , 0 , 0 , ...]
                move = countlist.index(max(countlist))  # 가장 큰 가중치가 있는 좌표 반환
                splitposition = movelist[move].split(',')  # 받은 값을 x , y로 변환 = splitposition[0],spolitposition[1]
                if (move == 0):  # 배열에 아무것도 없다면 혹은 가중치가 다 같다면 ?
                    indexx = 0   # x,y를 0 초기화
                    indexy = 0
                    for c in range(2, 5):
                        for d in range(2, 5):
                            if (omok.board[c][d] == 2):  # block stone point
                                indexx = c
                                indexy = d
                    movepm = [1, 2,-1,-2,0]
                    var1=movepm[random.randint(0,4)]
                    if (var1 == 0):
                        var2 = movepm[random.randint(0, 3)]
                    else:
                        var2 = movepm[random.randint(0, 4)] # var1이 0 아니라면 -1 1 0중에 하나 고
                    indexx = indexx + var1
                    indexy = indexy + var2
                    splitposition[0] = str(indexx)
                    splitposition[1] = str(indexy)
                positionx = int(splitposition[0])
                positiony = int(splitposition[1])
                try :
                    if(positionx > 0 and positiony > 0 and omok.board[positionx][positiony] == 0 ):
                        omok.board[positionx][positiony] = 1
                        omok.check_board_black(positionx, positiony)
                        human = Human(positionx, positiony)
                        game.start_play(human)


                except:
                    pass

        elif (omok.turn == 2):
                   try:
                       policy_param = pickle.load(open(model_file, 'rb'))
                   except:
                       policy_param = pickle.load(open(model_file, 'rb'),
                                                  encoding='bytes')
                   best_policy = PolicyValueNetNumpy(8, 8, policy_param)
                   print('current model is', model_file)
                   mcts = MCTSPlayer(best_policy.policy_value_fn, c_puct=7, n_playout=2000)
                   move = game.start_play1(mcts)
                   x = move // board_size
                   y = move % board_size
                   omok.board[x][y] = 2
                   omok.check_board_white(x, y)

        if omok.is_gameover: ##return true
            return

        pygame.display.update()
        fps_clock.tick(fps)