import pygame, sys

from pygame.locals import *
from rule import *
import numpy as np


bg_color = (128, 128, 128)
black = (0, 0, 0)
blue = (0, 50, 255)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
blackwin = 0
whitewin = 0

window_width = 800
window_height = 500
board_width = 500
grid_size = 30
epside = 0
fps = 60
fps_clock = pygame.time.Clock()
turn = 1

class Omok(object):

    def __init__(self, surface):
        self.board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.menu = Menu(surface)
        self.rule = Rule(self.board)
        self.surface = surface
        self.pixel_coords = []
        self.set_coords()
        self.set_image_font()
        self.is_show = True
        self.blackwin = 0
        self.whitewin = 0
        self.max_episode = 10
        self.id = 0
        self.episode = 0
        self.turn = 1

    def init_game(self):
        self.init_board()  # board initialize
        self.id = 0  # id = 0
        self.turn = 1
        self.draw_board()  # draw board..
        self.menu.show_msg(empty)  # no message
        self.coords = []  # array create
        self.is_gameover = False  # not game over
        self.is_forbidden = False

    def set_image_font(self):
        black_img = pygame.image.load('image/black.png')
        white_img = pygame.image.load('image/white.png')
        board_img = pygame.image.load('image/board8x8num.png')
        self.last_w_img = pygame.image.load('image/white_a.png')
        self.last_b_img = pygame.image.load('image/black_a.png')
        self.board_img = pygame.transform.scale(board_img, (485,485))
        self.forbidden_img = pygame.image.load('image/forbidden.png')
        self.font = pygame.font.Font("freesansbold.ttf", 14)
        self.black_img = pygame.transform.scale(black_img, (47, 47))
        self.white_img = pygame.transform.scale(white_img, (47, 47))

    def init_board(self):  # just board initialize
        for y in range(board_size):
            for x in range(board_size):
                self.board[y][x] = 0 # # # #  #

    def draw_board(self):  # draw board
        self.surface.blit(self.board_img, (0, 0))

    def draw_image(self, img_index, x, y):  #
        img = [self.black_img, self.white_img, self.black_img, self.white_img, self.forbidden_img]
        self.surface.blit(img[img_index], (x, y))

    def show_number(self, x, y, stone, number):
        colors = [white, black, red, red]
        color = colors[stone]
        self.menu.make_text(self.font, str(number), color, None, y + 23, x + 23, 1)

    def hide_numbers(self):
        for i in range(len(self.coords)):
            x, y = self.coords[i]
            self.draw_image(i % 2, x, y)
        if self.coords:
            x, y = self.coords[-1]
            self.draw_image(i % 2 + 2, x, y)

    def show_numbers(self):
        for i in range(len(self.coords)):
            x, y = self.coords[i]
            self.show_number(x, y, i % 2, i + 1)
        if self.coords:
            x, y = self.coords[-1]
            self.draw_image(i % 2, x, y)
            self.show_number(x, y, i % 2 + 2, i + 1)

    def draw_stone_b(self, coord,stone, increase):
        x, y = self.get_point(coord)
        self.hide_numbers()
        if self.is_show:
            self.show_numbers()
        self.id += increase
        self.turn = 2

    def draw_stone_w(self, coord, stone,increase):
        x, y = self.get_point(coord)
        self.hide_numbers()
        if self.is_show:
            self.show_numbers()
        self.id += increase
        self.turn = 1


    def set_coords(self):
        for y in range(board_size):
            for x in range(board_size):
                self.pixel_coords.append((x * grid_size + 30, y * grid_size + 30))

    def get_pixel(self, x, y):
        x1 = (x * 50) + 55
        y1 = (y * 50) + 55
        return x1, y1

    def get_coord(self, pos):
        for coord in self.pixel_coords:
            x, y = coord
            rect = pygame.Rect(x, y, grid_size, grid_size)
            if rect.collidepoint(pos):
                return coord
        return None

    def get_point(self, coord):
        x, y = coord
        x = (x - 55) // grid_size
        y = (y - 55) // grid_size
        return x, y

    def check_board_white(self, y, x):
        coord = self.get_pixel(x, y)
        self.coords.append(coord)
        self.draw_stone_w(coord, self.turn, 1)  # id increase
        array = np.array(self.board)
        print('RL AI(White) point = {', y ,',', x ,'}, id = ',self.id)
        print(array)
        if self.check_gameover(x, y, 3-self.turn):  # if the game is over , plus win and episode,
            self.whitewin += 1
            self.episode = self.episode + 1
            print('\n',self.episode,'번째 episode 승자는 RL AI (white) 입니다.')
            print('\nRulebased AI(Black) win = ', self.blackwin)
            print('\nRL AI(White) win= ', self.whitewin)
            print('\nepisode = ', self.episode)
            print('\nmax_episode = ', self.max_episode)
            if self.episode == self.max_episode:    # if episode = max , print win rate and terminate
                print('\nRulebased AI(Black) win rate = ', (self.blackwin / self.max_episode) * 100)
                print('\nRL AI(White) win rate = ', (self.whitewin / self.max_episode) * 100)
                if (self.blackwin == self.whitewin):
                    print('\ntie win rate = 50')
                self.id = 0
                self.turn = 1
                Menu.terminate(self)
            if self.episode < self.max_episode:
                self.init_game()
        else:
            self.turn = 1
        print("\n")
        return True

    def check_board_black(self, y, x):
        coord = self.get_pixel(x, y)
        self.coords.append(coord)
        self.draw_stone_b(coord, self.turn, 1)  # id increase
        array = np.array(self.board)
        print('Rulebase AI(black) point = {', y ,',', x ,'}, id = ',self.id,'\n')
        print(array)
        if self.check_gameover(x, y, 3-self.turn):
            self.id=0
            self.blackwin += 1
            self.episode = self.episode + 1
            print('\nepisode ',self.episode,'의 승자는 Rulebased AI (Black) 입니다.')
            print('\nRulebased AI(Black) win = ', self.blackwin)
            print('\nRL AI(White) win= ', self.whitewin)
            print('\nepisode = ', self.episode)
            print('\nmax_episode = ', self.max_episode)
            if self.episode == self.max_episode:
                print('\nRulebased AI(Black) win rate = ', (self.blackwin / self.max_episode) * 100)
                print('\nRL AI(White) win rate = ', (self.whitewin / self.max_episode) * 100)
                if (self.blackwin == self.whitewin):
                    print('\ntie win rate = 50')
                self.turn=1
                Menu.terminate(self)
            if self.episode < self.max_episode:
                self.init_game()
        else:
            self.turn = 2

        print("\n")
        return True

    def check_gameover(self, x, y, stone):
        if self.id > board_size * board_size:
            self.show_winner_msg(stone)
            return True
        elif self.rule.is_gameover(x, y, stone) == 1 or self.rule.is_gameover(x, y, stone) == 2 :
            self.show_winner_msg(stone)
            return True
        return False

    def show_winner_msg(self, stone):
        for i in range(3):
            self.menu.show_msg(stone)
            pygame.display.update()
            pygame.time.delay(200)
            self.menu.show_msg(empty)
            pygame.display.update()
            pygame.time.delay(200)
        self.menu.show_msg(stone)


class Menu(object):
    def __init__(self, surface) :
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.surface = surface
        self.draw_menu()

    def draw_menu(self):
        top, left = window_height - 30, window_width - 200
        self.new_rect = self.make_text(self.font, 'New Game', blue, None, top - 30, left)
        self.quit_rect = self.make_text(self.font, 'Quit Game', blue, None, top, left)

    def show_msg(self, msg_id):
        msg = {
            empty: '                                    ',
            black_stone: 'Black win!!!',
            white_stone: 'White win!!!',
            tie: 'Tie',
        }
        center_x = window_width - (window_width - board_width) // 2
        self.make_text(self.font, msg[msg_id], black, bg_color, 30, center_x, 1)

    def make_text(self, font, text, color, bgcolor, top, left, position=0):
        surf = font.render(text, False, color, bgcolor)
        rect = surf.get_rect()
        if position:
            rect.center = (left, top)
        else:
            rect.topleft = (left, top)
        self.surface.blit(surf, rect)
        return rect

    def check_rect(self, pos):
        if self.new_rect.collidepoint(pos):
            return True

        elif self.quit_rect.collidepoint(pos):
            return False

    def terminate(self):
        pygame.quit()
        sys.exit()

    def is_continue(self, omok):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                else :
                    if self.check_rect(event.pos):
                        return

            pygame.display.update()
            fps_clock.tick(fps)
