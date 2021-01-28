from rule import *
from pygame.locals import *
import random
import pygame, sys

bg_color = (128, 128, 128)
black = (0, 0, 0)
blue = (0, 50, 255)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)

window_width = 800
window_height = 500
board_width = 500
grid_size = 30

fps = 60
fps_clock = pygame.time.Clock()

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

    def init_game(self):
        self.turn = black_stone
        self.draw_board()
        self.menu.show_msg(empty)
        self.init_board()
        self.coords = []
        self.id = 1
        self.is_gameover = False
        self.is_forbidden = False

    def set_image_font(self):
        black_img = pygame.image.load('image/black.png')
        white_img = pygame.image.load('image/white.png')
        self.last_w_img = pygame.image.load('image/white_a.png')
        self.last_b_img = pygame.image.load('image/black_a.png')
        self.board_img = pygame.image.load('image/board.png')
        self.forbidden_img = pygame.image.load('image/forbidden.png')
        self.font = pygame.font.Font("freesansbold.ttf", 14)
        self.black_img = pygame.transform.scale(black_img, (grid_size, grid_size))
        self.white_img = pygame.transform.scale(white_img, (grid_size, grid_size))

    def init_board(self):
        for y in range(board_size):
            for x in range(board_size):
                self.board[y][x] = 0

    def draw_board(self):
        self.surface.blit(self.board_img, (0, 0))

    def draw_image(self, img_index, x, y):
        img = [self.black_img, self.white_img, self.last_b_img, self.last_w_img, self.forbidden_img]
        self.surface.blit(img[img_index], (x, y))

    def show_number(self, x, y, stone, number):
        colors = [white, black, red, red]
        color = colors[stone]
        self.menu.make_text(self.font, str(number), color, None, y + 15, x + 15, 1)

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

    def check_forbidden(self):
        if self.turn == black_stone:
            coords = self.rule.get_forbidden_points(self.turn)
            while coords:
                x, y = coords.pop()
                x, y = x * grid_size + 25, y * grid_size + 25
                self.draw_image(4, x, y)
            self.is_forbidden = True

    def draw_stone(self, coord, stone, increase):
        if self.is_forbidden:
            self.draw_board()
        x, y = self.get_point(coord)
        self.board[y][x] = stone
        self.hide_numbers()
        if self.is_show:
            self.show_numbers()
        self.id += increase
        self.turn = white_stone
        self.check_forbidden()

    def draw_stone_w(self, coord,  stone, increase):
        if self.is_forbidden:
            self.draw_board()
        x, y = self.get_point(coord)
        self.draw_image(1, x, y)
        self.hide_numbers()
        if self.is_show:
            self.show_numbers()
        self.id += increase
        self.turn = black_stone
        self.check_forbidden()

    def set_coords(self):
        for y in range(board_size):
            for x in range(board_size):
                self.pixel_coords.append((x * grid_size + 25, y * grid_size + 25))

    def get_pixel(self, x, y):
        x1 = (x * 30) + 25
        y1 = (y * 30) + 25
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
        x = (x - 25) // grid_size
        y = (y - 25) // grid_size
        return x, y

    def check_board_black(self, pos):
        coord = self.get_coord(pos)
        if not coord:
            return False
        x, y = self.get_point(coord)
        if self.board[y][x] != empty:
            print("occupied")
            return True

        if self.turn == black_stone:
            if self.rule.forbidden_point(x, y, self.turn):
                print("forbidden point")
                return True

        self.coords.append(coord)
        self.draw_stone(coord, self.turn, 1)
        if self.check_gameover(coord, 3 - self.turn):
            self.is_gameover = True

        for x in range(0, 15):
            print(self.board[x][0], self.board[x][1], self.board[x][2], self.board[x][3], self.board[x][4],
                  self.board[x][5], self.board[x][6], self.board[x][7], self.board[x][8],
                  self.board[x][9], self.board[x][10], self.board[x][11], self.board[x][12], self.board[x][13],
                  self.board[x][14])
        print("\n")
        return True

    def check_board_white(self, y, x):
        coord = self.get_pixel(x, y)
        self.coords.append(coord)
        self.draw_stone_w(coord, self.turn, 1)
        if self.check_gameover(coord, 3 - self.turn):
            self.is_gameover = True

        for x in range(0, 15):
            print(self.board[x][0], self.board[x][1], self.board[x][2], self.board[x][3], self.board[x][4],
                  self.board[x][5], self.board[x][6], self.board[x][7], self.board[x][8],
                  self.board[x][9], self.board[x][10], self.board[x][11], self.board[x][12], self.board[x][13],
                  self.board[x][14])
        print("\n")
        return True

    def check_gameover(self, coord, stone):
        x, y = self.get_point(coord)
        if self.id > board_size * board_size:
            self.show_winner_msg(stone)
            return True
        elif self.rule.is_gameover(x, y, stone):
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
    def __init__(self, surface):
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

    def check_rect(self, pos, omok):
        if self.new_rect.collidepoint(pos):
            return True

        elif self.quit_rect.collidepoint(pos):
            self.terminate(self)
        return False

    def terminate(self):
        pygame.quit()
        sys.exit()

    def is_continue(self, omok):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == MOUSEBUTTONUP:
                    if (self.check_rect(event.pos, omok)):
                        return
            pygame.display.update()
            fps_clock.tick(fps)
