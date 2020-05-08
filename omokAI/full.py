##Rulebased 함수 안에 if 양식에 맞추어 원하는 규칙을 if문으로 구현해보세요.
import simplegui
import random

WIDTH = 486
HEIGHT = 486
scale = 27
board = [[0 for x in range(0, 19)] for y in range(0, 19)]
turn = 1


def mouse_handler(position):
    global count_label, turn
    x = int(round(position[0] / scale))
    y = int(round(position[1] / scale))
    if (turn == 3):
        pass
    elif (board[x][y] == 0):
        board[x][y] = 1
        turn = 2
        if (turn == 2):
            count_label.set_text('Your turn')

    else:
        pass


def rulebased(canvas):
    global count_label, turn

    ###여기는 건드리지 않으셔도 됩니다.
    if (turn == 1):
        pass
    elif (turn == 2):
        ####↘방향
        for x in range(0, 17):
            for y in range(0, 17):
                if (board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 1 and turn == 2):
                    try:
                        if (board[x + 3][y + 3] == 0):
                            board[x + 3][y + 3] = 2
                            turn = 1

                    except:
                        if (y > 0 and board[x - 1][y - 1] == 0):
                            board[x - 1][y - 1] = 2
                            turn = 1
        #### 4개의 경우



        #### ↓방향
        for x in range(0, 19):
            for y in range(0, 17):
                if (board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 1 and turn == 2):
                    try:
                        if (board[x][y + 3] == 0):
                            board[x][y + 3] = 2
                            turn = 1


                    except:
                        if (y > 0 and board[x][y - 1] == 0):
                            board[x][y - 1] = 2
                            turn = 1
        #### 4개의 경우
        for x in range(0, 19):
            for y in range(0, 16):
                if (board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 1 and board[x][
                    y + 3] == 1 and turn == 2):
                    try:
                        if (board[x][y + 4] == 0):
                            board[x][y + 4] = 2
                            turn = 1
                        elif (x > 0 and board[x][y - 1] == 0):
                            board[x][y - 1] = 2
                            turn = 1

                    except:
                        if (y > 0 and board[x][y - 1] == 0):
                            board[x][y - 1] = 2
                            turn = 1
                elif (board[x][y] == 1 and board[x][y + 1] == 0 and board[x][y + 2] == 1 and board[x][
                    y + 3] == 1 and turn == 2):
                    board[x][y + 1] = 2
                    turn = 1
                elif (board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 0 and board[x][
                    y + 3] == 1 and turn == 2):
                    board[x][y + 2] = 2
                    turn = 1

        #### ↙방향
        for x in range(2, 19):
            for y in range(0, 17):
                if (board[x][y] == 1 and board[x - 1][y + 1] == 1 and board[x - 2][y + 2] == 1 and turn == 2):
                    try:
                        if (board[x + 1][y - 1] == 0):
                            board[x + 1][y - 1] = 2
                            turn = 1


                    except:
                        if (board[x - 3][y + 3] == 0):
                            board[x - 3][y + 3] = 2
                            turn = 1
        #### 4개의 경우
        for x in range(3, 19):
            for y in range(0, 16):
                if (board[x][y] == 1 and board[x - 1][y + 1] == 1 and board[x - 2][y + 2] == 1 and board[x - 3][
                    y + 3] == 1 and turn == 2):
                    try:
                        if (board[x + 1][y - 1] == 0):
                            board[x + 1][y - 1] = 2
                            turn = 1
                        elif (x > 0 and board[x - 4][y + 4] == 0):
                            board[x - 4][y + 4] = 2
                            turn = 1

                    except:
                        if (y > 0 and board[x - 4][y + 4] == 0):
                            board[x - 4][y + 4] = 2
                            turn = 1

                elif (board[x][y] == 1 and board[x - 1][y + 1] == 0 and board[x - 2][y + 2] == 1 and board[x - 3][
                    y + 3] == 1 and turn == 2):
                    board[x - 1][y + 1] = 2
                    turn = 1
                elif (board[x][y] == 1 and board[x - 1][y + 1] == 1 and board[x - 2][y + 2] == 0 and board[x - 3][
                    y + 3] == 1 and turn == 2):
                    board[x - 2][y + 2] = 2
                    turn = 1

        ###  AI말 체크
        ####↘방향
        for x in range(0, 17):
            for y in range(0, 17):
                if (board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 2 and turn == 2):
                    try:
                        if (board[x + 3][y + 3] == 0):
                            board[x + 3][y + 3] = 2
                            turn = 1

                    except:
                        if (y > 0 and board[x - 1][y - 1] == 0):
                            board[x - 1][y - 1] = 2
                            turn = 1
        ####4개의 경우
        for x in range(0, 16):
            for y in range(0, 16):
                if (board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 2 and board[x + 3][
                    y + 3] == 2 and turn == 2):
                    try:
                        if (board[x + 4][y + 4] == 0):
                            board[x + 4][y + 4] = 2
                            turn = 1
                        elif (x > 0 and board[x - 1][y - 1] == 0):
                            board[x - 1][y - 1] = 2
                            turn = 1

                    except:
                        if (y > 0 and board[x - 1][y - 1] == 0):
                            board[x - 1][y - 1] = 2
                            turn = 1
                elif (board[x][y] == 2 and board[x + 1][y + 1] == 0 and board[x + 2][y + 2] == 2 and board[x + 3][
                    y + 3] == 2 and turn == 2):
                    board[x + 1][y + 1] = 2
                    turn = 1

                elif (board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 0 and board[x + 3][
                    y + 3] == 2 and turn == 2):
                    board[x + 2][y + 2] = 2
                    turn = 1

        #### →방향
        for x in range(0, 17):
            for y in range(0, 17):
                if (board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 2 and turn == 2):
                    try:
                        if (board[x + 3][y] == 0):
                            board[x + 3][y] = 2
                            turn = 1


                    except:
                        if (x > 0 and board[x - 1][y] == 0):
                            board[x - 1][y] = 2
                            turn = 1
        ####4개의 경우
        for x in range(0, 16):
            for y in range(0, 16):
                if (board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 2 and board[x + 3][
                    y] == 2 and turn == 2):
                    try:
                        if (board[x + 4][y] == 0):
                            board[x + 4][y] = 2
                            turn = 1
                        elif (x > 0 and board[x - 1][y] == 0):
                            board[x - 1][y] = 2
                            turn = 1

                    except:
                        if (y > 0 and board[x - 1][y] == 0):
                            board[x - 1][y] = 2
                            turn = 1
                elif (board[x][y] == 2 and board[x + 1][y] == 0 and board[x + 2][y] == 2 and board[x + 3][
                    y] == 2 and turn == 2):
                    board[x + 1][y] = 2
                    turn = 1
                elif (board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 0 and board[x + 3][
                    y] == 2 and turn == 2):
                    board[x + 2][y] = 2
                    turn = 1

        #### ↓방향
        for x in range(0, 19):
            for y in range(0, 17):
                if (board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 2 and turn == 2):
                    try:
                        if (board[x][y + 3] == 0):
                            board[x][y + 3] = 2
                            turn = 1


                    except:
                        if (y > 0 and board[x][y - 1] == 0):
                            board[x][y - 1] = 2
                            turn = 1
        ####4개의 경우
        for x in range(0, 19):
            for y in range(0, 16):
                if (board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 2 and board[x][
                    y + 3] == 2 and turn == 2):
                    try:
                        if (board[x][y + 4] == 0):
                            board[x][y + 4] = 2
                            turn = 1
                        elif (x > 0 and board[x][y - 1] == 0):
                            board[x][y - 1] = 2
                            turn = 1

                    except:
                        if (y > 0 and board[x][y - 1] == 0):
                            board[x][y - 1] = 2
                            turn = 1
                elif (board[x][y] == 2 and board[x][y + 1] == 0 and board[x][y + 2] == 2 and board[x][
                    y + 3] == 2 and turn == 2):
                    board[x][y + 1] = 2
                    turn = 1
                elif (board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 0 and board[x][
                    y + 3] == 2 and turn == 2):
                    board[x][y + 2] = 2
                    turn = 1

        #### ↙방향
        for x in range(2, 19):
            for y in range(0, 17):
                if (board[x][y] == 2 and board[x - 1][y + 1] == 2 and board[x - 2][y + 2] == 2 and turn == 2):
                    try:
                        if (board[x + 1][y - 1] == 0):
                            board[x + 1][y - 1] = 2
                            turn = 1


                    except:
                        if (board[x - 3][y + 3] == 0):
                            board[x - 3][y + 3] = 2
                            turn = 1
        ####4개의 경우
        for x in range(3, 19):
            for y in range(0, 16):
                if (board[x][y] == 2 and board[x - 1][y + 1] == 2 and board[x - 2][y + 2] == 2 and board[x - 3][
                    y + 3] == 2 and turn == 2):
                    try:
                        if (board[x + 1][y - 1] == 0):
                            board[x + 1][y - 1] = 2
                            turn = 1
                        elif (x > 0 and board[x - 4][y + 4] == 0):
                            board[x - 4][y + 4] = 2
                            turn = 1

                    except:
                        if (y > 0 and board[x - 4][y + 4] == 0):
                            board[x - 4][y + 4] = 2
                            turn = 1
                elif (board[x][y] == 2 and board[x - 1][y + 1] == 0 and board[x - 2][y + 2] == 2 and board[x - 3][
                    y + 3] == 2 and turn == 2):
                    board[x - 1][y + 1] = 2
                    turn = 1
                elif (board[x][y] == 2 and board[x - 1][y + 1] == 2 and board[x - 2][y + 2] == 0 and board[x - 3][
                    y + 3] == 2 and turn == 2):
                    board[x - 2][y + 2] = 2
                    turn = 1

        #### 방어 이외 AI 말 두는 규칙
        #### 1. 처음둘 때는 적당한 위치에
        #### 2. 주변에 가장 자신의 많은 돌의 위치를 찾아 거기에 둔다.
        if (turn != 1):
            movelist = list()
            countlist = list()
            for a in range(1, 18):
                for b in range(1, 18):
                    count = 0
                    if (board[a][b] != 0):
                        pass
                    else:
                        if (board[a - 1][b - 1] == 2):
                            count = count + 1
                        if (board[a][b - 1] == 2):
                            count = count + 1
                        if (board[a + 1][b - 1] == 2):
                            count = count + 1
                        if (board[a - 1][b] == 2):
                            count = count + 1
                        if (board[a + 1][b] == 2):
                            count = count + 1
                        if (board[a - 1][b + 1] == 2):
                            count = count + 1
                        if (board[a][b + 1] == 2):
                            count = count + 1
                        if (board[a + 1][b + 1] == 2):
                            count = count + 1
                        xymove = str(a) + ',' + str(b)
                        movelist.append(xymove)
                        countlist.append(count)
            move = countlist.index(max(countlist))
            splitposition = movelist[move].split(',')
            if (move == 0):
                indexx = 0
                indexy = 0
                for c in range(0, 19):
                    for d in range(0, 19):
                        if (board[c][d] == 1):
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
                count_label.set_text(splitposition[0])
            positionx = int(splitposition[0])
            positiony = int(splitposition[1])
            board[positionx][positiony] = 2
            turn = 1
            count_label.set_text('Your turn')
    else:
        pass


####승리체크함수
def finishcheck(canvas):
    global count_label, turn
    for x in range(0, 15):
        for y in range(0, 15):
            if (board[x][y] == 1 and board[x + 1][y + 1] == 1 and board[x + 2][y + 2] == 1 and board[x + 3][
                y + 3] == 1 and board[x + 4][y + 4] == 1):
                turn = 3
            elif (board[x][y] == 2 and board[x + 1][y + 1] == 2 and board[x + 2][y + 2] == 2 and board[x + 3][
                y + 3] == 2 and board[x + 4][y + 4] == 2):
                turn = 4
    for x in range(0, 15):
        for y in range(0, 15):
            if (board[x][y] == 1 and board[x + 1][y] == 1 and board[x + 2][y] == 1 and board[x + 3][y] == 1 and
                    board[x + 4][y] == 1):
                turn = 3
            elif (board[x][y] == 2 and board[x + 1][y] == 2 and board[x + 2][y] == 2 and board[x + 3][y] == 2 and
                  board[x + 4][y] == 2):
                turn = 4
    for x in range(0, 19):
        for y in range(0, 15):
            if (board[x][y] == 1 and board[x][y + 1] == 1 and board[x][y + 2] == 1 and board[x][y + 3] == 1 and
                    board[x][y + 4] == 1):
                turn = 3
            elif (board[x][y] == 2 and board[x][y + 1] == 2 and board[x][y + 2] == 2 and board[x][y + 3] == 2 and
                  board[x][y + 4] == 2):
                turn = 4
    for x in range(4, 19):
        for y in range(0, 15):
            if (board[x][y] == 1 and board[x - 1][y + 1] == 1 and board[x - 2][y + 2] == 1 and board[x - 3][
                y + 3] == 1 and board[x - 4][y + 4] == 1):
                turn = 3
            elif (board[x][y] == 2 and board[x - 1][y + 1] == 2 and board[x - 2][y + 2] == 2 and board[x - 3][
                y + 3] == 2 and board[x - 4][y + 4] == 2):
                turn = 4
    return turn


#### simplegui 함수입니다. 건드릴 필요 없습니다.
def draw(canvas):
    global turn
    for y in range(int(HEIGHT / scale)):
        canvas.draw_line((0, y * scale), (WIDTH, y * scale), 1, "Gray")
    for x in range(int(WIDTH / scale)):
        canvas.draw_line((x * scale, 0), (x * scale, HEIGHT), 1, "Gray")
    for x in range(0, 19):
        for y in range(0, 19):
            if (board[x][y] == 1):
                canvas.draw_circle(((x) * 27, (y) * 27), 10, 1, 'red', 'red')
            elif (board[x][y] == 2):
                canvas.draw_circle(((x) * 27, (y) * 27), 10, 1, 'white', 'white')
    check = finishcheck(canvas)
    if (check == 3):
        count_label.set_text('Player win')
        turn = 3
    elif (check == 4):
        count_label.set_text('AI win')
        turn = 3
    else:
        rulebased(canvas)  # 코드 실행


frame = simplegui.create_frame("Connect 5", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)
count_label = frame.add_label(str('Your turn'))
frame.start()


