from Omok import *
import pygame, sys
import random
from pygame.locals import *
from rule import *

fps = 60
fps_clock = pygame.time.Clock()

def run_game(surface, omok, menu):
    omok.init_game()

    while True:
        for event in pygame.event.get():
            if omok.turn == black_stone and event.type == MOUSEBUTTONUP:
                omok.check_board_black(event.pos)
            else :
                ## right under
                for y in range(0, 13):
                    for x in range(0, 13):
                        if (omok.board[y][x] == 1 and omok.board[y + 1][x + 1] == 1 and omok.board[y + 2][x + 2] == 1):
                            try:
                                if (omok.board[y + 3][x + 3] == 0):
                                    omok.board[y + 3][x + 3] = 2
                                    omok.check_board_white(y+3, x+3)
                            except:
                                if (y > 0 and omok.board[y - 1][x - 1] == 0):
                                    omok.board[y - 1][x - 1] = 2
                                    omok.check_board_white(y-1, x-1)
                ## right unfer 4
                for y in range(0,12):
                    for x in range(0, 12):
                        if (omok.board[y][x] == 1 and omok.board[y + 1][x + 1] == 1 and omok.board[y + 2][x + 2] == 1
                                and omok.board[y + 3][x + 3] == 1 ):
                            try:
                                if (omok.board[y + 4][x + 4] == 0):
                                    omok.board[y + 4][x + 4] = 2
                                    omok.check_board_white(y+4, x+4)
                                elif (y > 0 and omok.board[y - 1][x - 1] == 0):
                                    omok.board[y - 1][x - 1] = 2
                                    omok.check_board_white(y-1, x-1)
                            except:
                                if (x > 0 and omok.board[y - 1][x - 1] == 0):
                                    omok.board[y - 1][x - 1] = 2
                                    omok.check_board_white(y-1, x-1)
                        elif (omok.board[y][x] == 1 and omok.board[y + 1][x + 1] == 0 and omok.board[y + 2][x + 2] == 1
                              and omok.board[y + 3][x + 3] == 1 and omok.turn == 2):
                              omok.board[y + 1][x + 1] = 2
                              omok.check_board_white(y + 1, x + 1)
                        elif (omok.board[y][x] == 1 and omok.board[y + 1][x + 1] == 1 and omok.board[y + 2][x + 2] == 0
                              and  omok.board[y + 3][x + 3] == 1 and omok.turn == 2):
                              omok.board[y + 2][x + 2] = 2
                              omok.check_board_white(y + 2, x + 2)

                ## ->
                for y in range(0, 15):
                    for x in range(0, 13):
                        if (omok.board[y][x] == 1 and omok.board[y][x+1] == 1 and omok.board[y][x+2] == 1 and
                                omok.turn == 2):
                            try:
                                if (omok.board[y][x+3] == 0):
                                    omok.board[y][x+3] = 2
                                    omok.check_board_white(y , x+3)


                            except:
                                if (x > 0 and omok.board[y][x-1] == 0):
                                    omok.board[y][x-1] = 2
                                    omok.check_board_white(y, x-1)

                ##  -> 4
                for y in range(0, 15):
                    for x in range(0, 12):
                        if (omok.board[y][x] == 1 and omok.board[y ][x+ 1] == 1 and omok.board[y ][x+ 2] == 1 and
                                omok.board[y][x+ 3] == 1 and omok.turn == 2):
                            try:
                                if (omok.board[y][x+ 4] == 0):
                                    omok.board[y][x + 4] = 2
                                    omok.check_board_white(y, x + 4)
                                elif (x > 0 and omok.board[y][x - 1] == 0):
                                    omok.board[y][x - 1] = 2
                                    omok.check_board_white(y, x - 1)

                            except:
                                if (y > 0 and omok.board[y][x - 1] == 0):
                                    omok.board[y][x - 1] = 2
                                    omok.check_board_white(y - 1, x)
                        elif (omok.board[y][x] == 1 and omok.board[y][x + 1] == 0 and omok.board[y][x + 2] == 1 and
                              omok.board[y][x + 3] == 1 and omok.turn == 2):
                              omok.board[y][x + 1] = 2
                              omok.check_board_white(y, x + 1)
                        elif (omok.board[y][x] == 1 and omok.board[y][x + 1] == 1 and omok.board[y][x + 2] == 0 and
                              omok.board[y][x + 3] == 1 and omok.turn == 2):
                              omok.board[y][x + 2] = 2
                              omok.check_board_white(y,x+2)

                ##to under
                for y in range(0, 15):
                    for x in range(0, 13):
                        if (omok.board[x][y] == 1 and omok.board[x + 1][y] == 1 and omok.board[x+ 2][y]  == 1 and
                                omok.turn == 2):
                            try:
                                if (omok.board[x+ 3][y ] == 0):
                                    omok.board[x+ 3][y]  = 2
                                    omok.check_board_white(x+3,y)


                            except:
                                if (x > 0 and omok.board[x-1][y] == 0):
                                    omok.board[x-1][y] = 2
                                    omok.check_board_white(x-1,y)
                #### to under 4
                for y in range(0, 15):
                    for x in range(0, 12):
                        if (omok.board[x][y] == 1 and omok.board[x+ 1][y ] == 1 and omok.board[x+ 2][y ] == 1 and
                                omok.board[x+ 3][y ] == 1 and omok.turn == 2):
                            try:
                                if (omok.board[x+ 4][y ] == 0):
                                    omok.board[x+ 4][y ] = 2
                                    omok.check_board_white(x+4, y)
                                elif (y > 0 and omok.board[x-1][y] == 0):
                                    omok.board[x-1][y] = 2
                                    omok.check_board_white(x-1, y)

                            except:
                                if (x > 0 and omok.board[x - 1][y] == 0):
                                    omok.board[x-1][y] = 2
                                    omok.check_board_white(x-1, y)
                        elif (omok.board[x][y] == 1 and omok.board[x+ 1][y] == 0 and omok.board[x + 2][y] == 1 and
                              omok.board[x + 3][y] == 1 and omok.turn == 2):
                             omok.board[x+1][y] = 2
                             omok.check_board_white(x+1, y)
                        elif (omok.board[x][y] == 1 and omok.board[x + 1][y] == 1 and omok.board[x+ 2][y ] == 0 and
                              omok.board[x+ 3][y ] == 1 and omok.turn == 2):
                             omok.board[x + 2][y] = 2
                             omok.check_board_white(x+2, y)

                ##left under
                for y in range(2, 15):
                    for x in range(0, 13):
                        if (omok.board[x][y] == 1 and omok.board[x + 1][y - 1] == 1 and omok.board[x + 2][y - 2] == 1
                                and omok.turn == 2):
                            try:
                                if (omok.board[x - 1][y + 1] == 0):
                                    omok.board[x - 1][y + 1] = 2
                                    omok.check_board_white(x - 1, y + 1)

                            except:
                                if (omok.board[x + 3][y - 3] == 0):
                                    omok.board[x + 3][y - 3] = 2
                                    omok.check_board_white(x + 3, y - 3)
                ##left under 4
                for y in range(3, 15):
                    for x in range(0, 12):
                        if (omok.board[x][y] == 1 and omok.board[x +  1][y - 1] == 1 and omok.board[x + 2][y - 2] == 1
                                and  omok.board[x + 3][y - 3] == 1 and omok.turn == 2):
                            try:
                                if (omok.board[x + 1][y - 1] == 0):
                                    omok.board[x + 1][y - 1] = 2
                                    omok.check_board_white(x -1 , y+1)
                                elif (y > 0 and omok.board[x + 4][y - 4] == 0):
                                    omok.board[x + 4][y - 4] = 2
                                    omok.check_board_white(x+4, y-4)
                            except:
                                if (x > 0 and omok.board[x + 4][y - 4] == 0):
                                    omok.board[x + 4][y - 4] = 2
                                    omok.check_board_white(x + 4, y-4)
                        elif (omok.board[x][y] == 1 and omok.board[x + 1][y - 1] == 0 and omok.board[x + 2][y - 2] == 1
                              and  omok.board[x + 3][y - 3] == 1 and omok.turn == 2):
                               omok.board[x + 1][y - 1] = 2
                               omok.check_board_white(x + 1, y - 1)

                        elif (omok.board[x][y] == 1 and omok.board[x + 1][y - 1] == 1 and omok.board[x + 2][y - 2] == 0
                              and    omok.board[x + 3][y - 3] == 1 and omok.turn == 1):
                               omok.board[x + 2][y - 2] = 2
                               omok.check_board_white(x + 2, y-2)




                ##condition1 = fair  position
                ##place  the white stone near the place where the white stone gathers
                if (omok.turn != 1):
                    movelist = list()
                    countlist = list()
                    for a in range(1, 14):
                        for b in range(1, 14):
                            count = 0
                            if (omok.board[a][b] != 0):
                                pass
                            else:
                                if (omok.board[a - 1][b - 1] == 2):
                                    count = count + 1
                                if (omok.board[a][b - 1] == 2):
                                    count = count + 1
                                if (omok.board[a + 1][b - 1] == 2):
                                    count = count + 1
                                if (omok.board[a - 1][b] == 2):
                                    count = count + 1
                                if (omok.board[a + 1][b] == 2):
                                    count = count + 1
                                if (omok.board[a - 1][b + 1] == 2):
                                   count = count + 1
                                if (omok.board[a][b + 1] == 2):
                                    count = count + 1
                                if (omok.board[a + 1][b + 1] == 2):
                                    count = count + 1
                                xymove = str(a) + ',' + str(b)
                                movelist.append(xymove)
                                countlist.append(count)
                    move = countlist.index(max(countlist))
                    splitposition = movelist[move].split(',')
                    if (move == 0):
                        indexx = 0
                        indexy = 0
                        for c in range(0, 15):
                            for d in range(0, 15):
                                if (omok.board[c][d] == 1):
                                    indexx = c
                                    indexy = d
                        movepm = [-1, 1, 0]
                        var1 = movepm[random.randint(0, 2)]
                        if (var1 == 0):
                            var2 = movepm[random.randint(0, 1)]
                        else:
                            var2 = movepm[random.randint(0, 2)]
                        indexx = indexx + var1
                        indexy = indexx + var2
                        splitposition[0] = str(indexx)
                        splitposition[1] = str(indexy)

                    positionx = int(splitposition[0])
                    positiony = int(splitposition[1])
                    if(omok.board[positionx][positiony] != 2):
                        omok.board[positionx][positiony] = 2
                        omok.check_board_white(positionx, positiony)
        else:
                  pass





        if omok.is_gameover:
            return

        pygame.display.update()
        fps_clock.tick(fps)
