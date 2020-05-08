from Omok import *
import pygame, sys
import random
from pygame.locals import *
import pickle
from rule import *
import numpy as np
from MCTS import *
from copy import deepcopy
from math import *
from policy_value_net_pytorch import PolicyValueNet
import torch
from game import Board, Game
from mcts_alphaZero import MCTSPlayer
from multiprocessing.pool import ThreadPool
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
    omok.turn = black_stone
    omok.init_game()
    board = Board(width=board_size, height=board_size, n_in_row=5)
    game = Game(board)
    model_file = 'current_policy_15x15-self500.model'
    while True:


        for event in pygame.event.get():
            pygame.display.flip()
            if omok.turn == black_stone and event.type == MOUSEBUTTONUP:
                    x, y = omok.check_board_black(event.pos)
                    human = Human(x, y)
            elif omok.turn == white_stone:

                    best_policy = PolicyValueNet(15, 15, model_file = model_file)
                    mcts = MCTSPlayer(best_policy.policy_value_fn, c_puct=7, n_playout=800)
                    move = game.start_play(human, mcts, start_player=1)
                    x = move / board_size
                    y = move % board_size
                    print(int(x),y)
                    omok.check_board_white(int(x),y)
        else :
            pass

            if omok.is_gameover:
                return

            pygame.display.update()
            fps_clock.tick(fps)
