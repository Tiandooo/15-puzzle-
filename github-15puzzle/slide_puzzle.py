# *_*coding:utf-8 *_*
# Slide Puzzle

import pygame
import sys
import random
from pygame.locals import *


BOARDWIDTH = 2
BOARDHEIGHT = 2
TILESIZE = 120
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
FPS = 30
BLANK = None

#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BRIGHTBLUE =    (  0,  50, 255)
DARKBLUE =           (  3,  54,  73)
GREEN =         (  0, 204,   0)
AAAA   =         ( 84, 255, 159)
BLANK_TILE_COLOR = (69, 119, 208)
BLUE =               (0, 0, 255)
BGCOLOR = DARKBLUE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 30
YISHUFONTSIZE = 22
HIGHLIGHTCOLOR = (0, 0, 0)

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
high_picture_list = []  #用来保存高难图片分割
simple_picture_list = [] #存储中难图片分割
easy_picture_list = [] #存放低难图片分割
number = "number"
picture = "picture"
mode = None
hide_num = True
hide_but_hide = True
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT,\
    LEVEL_1_SURF,LEVEL_1_RECT, BOARDHEIGHT, BOARDWIDTH, LEVEL_2_SURF, LEVEL_2_RECT, LEVEL_3_RECT, LEVEL_3_SURF,\
    XMARGIN, YMARGIN, TIMES_SURF, TIMES_RECT, RESET, TIMES_BG_SURF, TIMES_BG_RECT, 艺术字体,fangkuairect,fangkuaisurf,\
    TILESIZE, num_fangkuai_list, num_fangkuai_dict, high_surf, high_rect, simple_surf,simple_rect, easy_surf, easy_rect,\
    mode, MODE_CHANGE_SURF, MODE_CHANGE_RECT, HIDE_NUM_SURF, HIDE_NUM_RECT, hide_num, hide_but_hide,MODE_CHANGE_TEXT_SURF,\
    MODE_CHANGE_TEXT_RECT, HIDE_NUM_TEXT_SURF, HIDE_NUM_TEXT_RECT, RESET_TEXT_SURF, RESET_TEXT_RECT, SOLVE_TEXT_SURF, \
    SOLVE_TEXT_RECT,BACK_SURF, BACK_RECT, STARTBGFILE

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    STARTSURF = pygame.Surface(DISPLAYSURF.get_size())
    MODESURF = pygame.Surface(DISPLAYSURF.get_size())
    pygame.display.set_caption('Slide Puzzle')
    BASICFONT = pygame.font.Font('msyh.ttf', BASICFONTSIZE)
    艺术字体 = pygame.font.Font('msyh.ttf', YISHUFONTSIZE)
    BGFILE = pygame.image.load("apic2261.jpg")
    STARTBGFILE = pygame.image.load("startbg.jpg")
    fangkuaisurf80 = pygame.image.load("fangkuai80.png")
    fangkuairect80 = fangkuaisurf80.get_rect()
    fangkuaisurf100 = pygame.image.load("fangkuai100.png")
    fangkuairect100 = fangkuaisurf100.get_rect()
    fangkuaisurf120 = pygame.image.load("fangkuai120.png")
    fangkuairect120 = fangkuaisurf120.get_rect()
    num_fangkuai_list = [[fangkuaisurf80,fangkuairect80], [fangkuaisurf100, fangkuairect100], [fangkuaisurf120, fangkuairect120]]
    num_fangkuai_dict = {80: num_fangkuai_list[0], 100: num_fangkuai_list[1], 120: num_fangkuai_list[2]}
    start_font_surf, start_font_rect = makeButton("start.png", 400, 450)
    DISPLAYSURF.blit(STARTBGFILE, (0, 0))
    STARTSURF.blit(STARTBGFILE, (0, 0))
    times = 0
    # Store the option buttons and their rectangles in OPTIONS.
    RESET_SURF, RESET_RECT = makeButton("reset.png", WINDOWWIDTH - 120, WINDOWHEIGHT - 150)
    SOLVE_SURF, SOLVE_RECT = makeButton("solve.png", WINDOWWIDTH - 120, WINDOWHEIGHT - 70)
    LEVEL_1_SURF, LEVEL_1_RECT = makeButton("level_select.png", 260, WINDOWHEIGHT - 200)
    LEVEL_1_TEXT_SURF, LEVEL_1_TEXT_RECT = makeText("简单",WHITE, 230, WINDOWHEIGHT - 217, 30)
    LEVEL_1_TEXT_CLICKED_SURF, LEVEL_1_TEXT_CLICKED_RECT = makeText("简单", BLUE, 230, WINDOWHEIGHT - 217, 30)
    LEVEL_2_SURF, LEVEL_2_RECT = makeButton("level_select.png", 260, WINDOWHEIGHT - 290)
    LEVEL_2_TEXT_SURF, LEVEL_2_TEXT_RECT = makeText("中等", WHITE, 230, WINDOWHEIGHT - 307, 30)
    LEVEL_2_TEXT_CLICKED_SURF, LEVEL_2_TEXT_CLICKED_RECT = makeText("中等", BLUE, 230, WINDOWHEIGHT - 307, 30)
    LEVEL_3_SURF, LEVEL_3_RECT = makeButton("level_select.png", 260, WINDOWHEIGHT - 380)
    LEVEL_3_TEXT_SURF, LEVEL_3_TEXT_RECT = makeText("困难",WHITE, 230, WINDOWHEIGHT - 397, 30)
    LEVEL_3_TEXT_CLICKED_SURF, LEVEL_3_TEXT_CLICKED_RECT = makeText("困难", BLUE, 230, WINDOWHEIGHT - 397, 30)
    TIMES_BG_SURF, TIMES_BG_RECT = makeButton("times_bg.png", 685, 75)
    PICTURE_SURF, PICTURE_RECT = makeButton("mode_select.png", 560, 280)
    NUM_SURF, NUM_RECT = makeButton("mode_select.png", 560, 380)
    PICTURE_TEXT_SURF, PICTURE_TEXT_RECT = makeText("图片模式", WHITE, 503, 260,30)
    PICTURE_TEXT_CLICKED_SURF, PICTURE_TEXT_CLICKED_RECT = makeText("图片模式", BLUE, 503, 260, 30)
    NUM_TEXT_SURF, NUM_TEXT_RECT = makeText("数字模式", WHITE, 503, 360,30)
    NUM_TEXT_CLICKED_SURF, NUM_TEXT_CLICKED_RECT = makeText("数字模式", BLUE, 503, 360, 30)
    HIDE_NUM_SURF, HIDE_NUM_RECT = makeButton("hide_num.png", 400, 530)
    MODE_CHANGE_TEXT_SURF, MODE_CHANGE_TEXT_RECT = makeText("CHANGE MODE", WHITE, 32,387,30)
    HIDE_TEXT = "显示数字"
    HIDE_NUM_TEXT_SURF, HIDE_NUM_TEXT_RECT = makeText(HIDE_TEXT, WHITE, 335, 515, 30)
    BACK_SURF, BACK_RECT = makeButton("fanhui.png", 40, 550)
    MODE_START_SURF, MODE_START_RECT = makeButton("MODE_START.png", 400, 500)
    START_FONT_SURF, START_FONT_RECT = makeText("开始游戏", WHITE, 340, 480, 30)
    tips = "选择难度和模式后点击开始游戏。"
    rules1 = "游戏规则：你需要将所有方块恢复到正确位置,"
    rules2 = "当点击次数超过25次时可以使用解决游戏按钮。"
    NAMESURF, NAMERECT = makeButton("name.png", 400, 200)
    TIPS_SURF, TIPS_RECT = makeText(tips, (225,255,255), 190, 50, 33)
    RULES_SURF, RULES_RECT = makeText(rules1, (225,255,255), 150, 100, 27)
    RULES2_SURF, RULES2_RECT = makeText(rules2, (225,255,255), 150, 130, 27)
    AUTHOR_SURF, AUTHOR_RECT = makeButton("author.PNG",600, 300)
    for i in range(1,16,1):   #导入高难图片
        if i < 10:
            high_surf = pygame.image.load("images_high/high_0{0}.jpg".format(str(i)))
            high_rect = high_surf.get_rect()
            high_picture_list.append([high_surf, high_rect])
        else:
            high_surf = pygame.image.load("images_high/high_{0}.jpg".format(str(i)))
            high_rect = high_surf.get_rect()
            high_picture_list.append([high_surf, high_rect])
    high_surf = pygame.image.load("images_high/high.jpg")
    high_rect = high_surf.get_rect()

    for i in range(1,9,1):  #导入中难图片
        simple_surf = pygame.image.load("images_simple/simple_0{0}.jpg".format(str(i)))
        simple_rect = simple_surf.get_rect()
        simple_picture_list.append([simple_surf, simple_rect])
    simple_surf = pygame.image.load("images_simple/simple.jpg")
    simple_rect = simple_surf.get_rect()

    for i in range(1, 4, 1):
        easy_surf = pygame.image.load("images_easy/easy_0{0}.jpg".format(str(i)))
        easy_rect = easy_surf.get_rect()
        easy_picture_list.append([easy_surf, easy_rect])
    easy_surf = pygame.image.load("images_easy/easy.jpg")
    easy_rect = easy_surf.get_rect()
    TIMES_SURF, TIMES_RECT = makeText(("次数：" + str(times)), (255, 0, 0), 629, 64, 25)
    n1 = True   # 用来判断是否开始游戏，若开始则退出
    mode_option = True
    playing = True
    level = None
    while True:
        while n1:
                STARTSURF.blit(start_font_surf, start_font_rect)
                STARTSURF.blit(NAMESURF, NAMERECT)
                STARTSURF.blit(AUTHOR_SURF, AUTHOR_RECT)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONUP:
                        if start_font_rect.collidepoint(event.pos):
                            n1 = False
                            mode_option = True
                    DISPLAYSURF.blit(STARTSURF, (0, 0))
                    pygame.display.update()
                    FPSCLOCK.tick(FPS)
        while mode_option:
            MODESURF.blit(STARTBGFILE, (0, 0))
            click_flag = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONUP:
                    if PICTURE_RECT.collidepoint(event.pos):
                        mode = "picture"
                    elif NUM_RECT.collidepoint(event.pos):
                        mode = "number"
                    if LEVEL_1_RECT.collidepoint(event.pos):
                        level = 1
                    elif LEVEL_2_RECT.collidepoint(event.pos):
                        level = 2
                    elif LEVEL_3_RECT.collidepoint(event.pos):
                        level = 3
                    elif BACK_RECT.collidepoint(event.pos):
                        playing = False
                        n1 = True
                        mode_option = False
                    elif MODE_START_RECT.collidepoint(event.pos):
                        if level and mode:
                            mode_option = False
                            playing = True

            MODESURF.blit(LEVEL_1_SURF, LEVEL_1_RECT)
            MODESURF.blit(LEVEL_1_TEXT_SURF, LEVEL_1_TEXT_RECT)
            MODESURF.blit(LEVEL_2_SURF, LEVEL_2_RECT)
            MODESURF.blit(LEVEL_2_TEXT_SURF, LEVEL_2_TEXT_RECT)
            MODESURF.blit(LEVEL_3_SURF, LEVEL_3_RECT)
            MODESURF.blit(LEVEL_3_TEXT_SURF, LEVEL_3_TEXT_RECT)
            MODESURF.blit(PICTURE_SURF, PICTURE_RECT)
            MODESURF.blit(NUM_SURF, NUM_RECT)
            MODESURF.blit(PICTURE_SURF, PICTURE_RECT)
            MODESURF.blit(PICTURE_TEXT_SURF, PICTURE_TEXT_RECT)
            MODESURF.blit(NUM_TEXT_SURF, NUM_TEXT_RECT)
            MODESURF.blit(BACK_SURF, BACK_RECT)
            MODESURF.blit(MODE_START_SURF, MODE_START_RECT)
            MODESURF.blit(START_FONT_SURF, START_FONT_RECT)
            MODESURF.blit(TIPS_SURF, TIPS_RECT)
            MODESURF.blit(RULES_SURF, RULES_RECT)
            MODESURF.blit(RULES2_SURF, RULES2_RECT)
            if level == 1:
                MODESURF.blit(LEVEL_1_TEXT_CLICKED_SURF, LEVEL_1_TEXT_CLICKED_RECT)
            elif level == 2:
                MODESURF.blit(LEVEL_2_TEXT_CLICKED_SURF, LEVEL_2_TEXT_CLICKED_RECT)
            elif level == 3:
                MODESURF.blit(LEVEL_3_TEXT_CLICKED_SURF, LEVEL_3_TEXT_CLICKED_RECT)
            if mode == "picture":
                MODESURF.blit(PICTURE_TEXT_CLICKED_SURF, PICTURE_TEXT_CLICKED_RECT)
            elif mode == "number":
                MODESURF.blit(NUM_TEXT_CLICKED_SURF, NUM_TEXT_CLICKED_RECT)
            DISPLAYSURF.blit(MODESURF, (0, 0))
            pygame.display.update()
            FPSCLOCK.tick(FPS)
        while playing:
            if level == 1:
                BOARDWIDTH, BOARDHEIGHT = 2, 2
                TILESIZE = 120
                XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
                YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
                SOLVEDBOARD = getStartingBoard()
                mainBoard, solutionSeq = generateNewPuzzle(20)  # clicked on New Game button
                allMoves = []
                level = None
            elif level == 2:
                BOARDWIDTH, BOARDHEIGHT = 3, 3
                TILESIZE = 100
                XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
                YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
                SOLVEDBOARD = getStartingBoard()
                mainBoard, solutionSeq = generateNewPuzzle(40)  # clicked on New Game button
                allMoves = []
                level = None
            elif level == 3:
                BOARDWIDTH, BOARDHEIGHT = 4, 4
                TILESIZE = 80
                XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
                YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
                SOLVEDBOARD = getStartingBoard()
                mainBoard, solutionSeq = generateNewPuzzle(80)  # clicked on New Game button
                allMoves = []
                level = False

            DISPLAYSURF.blit(STARTBGFILE,(0, 0))
            slideTo = None
            msg = '点击方块或使用键盘进行滑动。'
            if mainBoard == SOLVEDBOARD:
                times = 0
                msg = '游戏胜利！恭喜！'
                drawBoard(mainBoard, msg)
                pygame.display.update()
                pygame.time.wait(1000)
                if BOARDHEIGHT <= 4:
                    if BOARDHEIGHT==2:
                        BOARDWIDTH,BOARDHEIGHT = 3, 3
                        TILESIZE = 100
                        XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
                        YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
                        SOLVEDBOARD = getStartingBoard()
                        mainBoard, solutionSeq = generateNewPuzzle(40)  # clicked on New Game button
                        allMoves = []
                        continue
                    elif BOARDHEIGHT == 3 and BOARDWIDTH == 3:
                        BOARDWIDTH, BOARDHEIGHT = 4, 4
                        TILESIZE = 80
                        XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
                        YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
                        SOLVEDBOARD = getStartingBoard()
                        mainBoard, solutionSeq = generateNewPuzzle(80)  # clicked on New Game button
                        allMoves = []
                        continue
                    elif BOARDHEIGHT == 4 and BOARDWIDTH == 4:
                        BOARDWIDTH, BOARDHEIGHT = 2, 2
                        TILESIZE = 120
                        XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
                        YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
                        SOLVEDBOARD = getStartingBoard()
                        mainBoard, solutionSeq = generateNewPuzzle(20)  # clicked on New Game button
                        allMoves = []
                        continue

            TIMES_SURF, TIMES_RECT = makeText(("次数：" + str(times)), (255, 0, 0), 629, 64, 25)

            drawBoard(mainBoard, msg)
            DISPLAYSURF.blit(TIMES_SURF, TIMES_RECT)
            pygame.display.update()
            checkForQuit()
            for event in pygame.event.get():
                if event.type == MOUSEMOTION:
                    left, top = event.pos[0], event.pos[1]

                if event.type == MOUSEBUTTONUP:
                    spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                    if (spotx, spoty) == (None, None):
                        if RESET_RECT.collidepoint(event.pos):
                            times = 0
                            resetAnimation(mainBoard, allMoves) # clicked on Reset button
                            allMoves = []
                        elif BACK_RECT.collidepoint(event.pos):
                            n1 = False
                            playing = False
                            mode_option = True
                        elif SOLVE_RECT.collidepoint(event.pos):
                            if times >=25:
                                times = 0
                                resetAnimation(mainBoard, solutionSeq + allMoves) # clicked on Solve button
                        elif HIDE_NUM_RECT.collidepoint(event.pos):
                            if hide_num == False:
                                hide_num = True
                                HIDE_TEXT = "显示数字"
                            else:
                                hide_num = False
                                HIDE_TEXT = "隐藏数字"
                            HIDE_NUM_TEXT_SURF, HIDE_NUM_TEXT_RECT = makeText(HIDE_TEXT, WHITE, 335, 515, 30)
                    else:
                        blankx, blanky = getBlankPosition(mainBoard)
                        if spotx == blankx + 1 and spoty == blanky:
                            slideTo = LEFT
                            times += 1
                        elif spotx == blankx - 1 and spoty == blanky:
                            slideTo = RIGHT
                            times += 1
                        elif spotx == blankx and spoty == blanky + 1:
                            slideTo = UP
                            times += 1
                        elif spotx == blankx and spoty == blanky - 1:
                            slideTo = DOWN
                            times += 1
                elif event.type == KEYUP:
                    if event.key in (K_LEFT, K_a) and isValidMove(mainBoard, LEFT):
                        slideTo = LEFT
                        times += 1
                    elif event.key in (K_RIGHT, K_d) and isValidMove(mainBoard, RIGHT):
                        slideTo = RIGHT
                        times += 1
                    elif event.key in (K_UP, K_w) and isValidMove(mainBoard, UP):
                        slideTo = UP
                        times += 1
                    elif event.key in (K_DOWN, K_s) and isValidMove(mainBoard, DOWN):
                        slideTo = DOWN
                        times += 1
          #     for rect in BUTTON_LIST:
           #         if rect.collidepoint(left, top):
            #            if rect == SOLVE_RECT and times < 25:
             #               pass
              #          else:
               #             pygame.draw.rect(DISPLAYSURF, (255, 255, 255),(rect.left - 5, rect.top - 5, rect.width + 8, rect.height + 8), 4)
                #            '''
            if slideTo:
                slideAnimation(mainBoard, slideTo, '点击方块或使用键盘进行滑动。', int(TILESIZE/3)) # show slide on screen
                makeMove(mainBoard, slideTo)
                allMoves.append(slideTo) # record the slide
            pygame.display.update()
            FPSCLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back



def getStartingBoard():
    # Return a board data structure with tiles in the solved state.
    # For example, if BOARDWIDTH and BOARDHEIGHT are both 3, this function
    # returns [[1, 4, 7], [2, 5, 8], [3, 6, BLANK]]
    counter = 1
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(counter)
            counter += BOARDWIDTH
        board.append(column)
        counter -= BOARDWIDTH * (BOARDHEIGHT - 1) + BOARDWIDTH - 1

    board[BOARDWIDTH-1][BOARDHEIGHT-1] = BLANK
    return board


def getBlankPosition(board):
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if board[x][y] == BLANK:
                return (x, y)


def makeMove(board, move):
    # This function does not check if the move is valid.
    blankx, blanky = getBlankPosition(board)

    if move == UP:
        board[blankx][blanky], board[blankx][blanky + 1] = board[blankx][blanky + 1], board[blankx][blanky]
    elif move == DOWN:
        board[blankx][blanky], board[blankx][blanky - 1] = board[blankx][blanky - 1], board[blankx][blanky]
    elif move == LEFT:
        board[blankx][blanky], board[blankx + 1][blanky] = board[blankx + 1][blanky], board[blankx][blanky]
    elif move == RIGHT:
        board[blankx][blanky], board[blankx - 1][blanky] = board[blankx - 1][blanky], board[blankx][blanky]


def isValidMove(board, move):
    blankx, blanky = getBlankPosition(board)
    return (move == UP and blanky != len(board[0]) - 1) or \
           (move == DOWN and blanky != 0) or \
           (move == LEFT and blankx != len(board) - 1) or \
           (move == RIGHT and blankx != 0)


def getRandomMove(board, lastMove=None):
    # start with a full list of all four moves
    validMoves = [UP, DOWN, LEFT, RIGHT]

    # remove moves from the list as they are disqualified
    if lastMove == UP or not isValidMove(board, DOWN):
        validMoves.remove(DOWN)
    if lastMove == DOWN or not isValidMove(board, UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not isValidMove(board, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not isValidMove(board, LEFT):
        validMoves.remove(LEFT)

    # return a random move from the list of remaining moves
    return random.choice(validMoves)


def getLeftTopOfTile(tileX, tileY):
    left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
    top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
    return (left, top)


def getSpotClicked(board, x, y):
    # from the x & y pixel coordinates, get the x & y board coordinates
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = getLeftTopOfTile(tileX, tileY)
            tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)


def drawTile(tilex, tiley, number,adjx=0, adjy=0):
    # draw a tile at board coordinates tilex and tiley, optionally a few
    # pixels over (determined by adjx and adjy)
    left, top = getLeftTopOfTile(tilex, tiley)
    #处理数字对象
    textSurf = BASICFONT.render(str(number), True, TEXTCOLOR)
    textRect = textSurf.get_rect()
    textRect.center = left + int(TILESIZE / 2) + adjx, top + int(TILESIZE / 2) + adjy
    #根据模式绘制滑块
    if number:
        if mode == "number":
            num_fangkuai_dict[TILESIZE][1].center = (left + TILESIZE / 2 + adjx, top + TILESIZE / 2 + adjy)
            DISPLAYSURF.blit(num_fangkuai_dict[TILESIZE][0], num_fangkuai_dict[TILESIZE][1])   #根据TILESIZE绘制图片
            DISPLAYSURF.blit(textSurf, textRect)
        # 拼图图片
        if mode == "picture":
            if BOARDWIDTH == 2:
                easy_picture_list[number - 1][1].center = (left + TILESIZE / 2 + adjx, top + TILESIZE / 2 + adjy)
                DISPLAYSURF.blit(easy_picture_list[number - 1][0], easy_picture_list[number - 1][1])
            if BOARDWIDTH == 3:
                simple_picture_list[number - 1][1].center = (left + TILESIZE / 2 + adjx, top + TILESIZE / 2 + adjy)
                DISPLAYSURF.blit(simple_picture_list[number - 1][0], simple_picture_list[number - 1][1])
            if BOARDWIDTH == 4:
                high_picture_list[number - 1][1].center = (left + TILESIZE / 2 + adjx, top + TILESIZE / 2 + adjy)
                DISPLAYSURF.blit(high_picture_list[number-1][0], high_picture_list[number-1][1])
            if hide_num == False:
                DISPLAYSURF.blit(textSurf, textRect)




    else:
        pygame.draw.rect(DISPLAYSURF, BLANK_TILE_COLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))




def makeText(text, color, top, left,size):
    # create the Surface and Rect objects for some text.
    BASICFONT = pygame.font.Font("msyh.ttf", size)
    textSurf = BASICFONT.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)



def makeButton(path, top, left):
    buttonsurf = pygame.image.load(path)
    buttonrect = buttonsurf.get_rect()
    buttonrect.center = (top, left)
    return (buttonsurf, buttonrect)


def drawBoard(board, message):
    DISPLAYSURF.blit(STARTBGFILE, (0, 0))
    if mode == "picture":
        if BOARDWIDTH == 2:
            easy_rect = (50, 50)
            DISPLAYSURF.blit(easy_surf, easy_rect)
        if BOARDWIDTH == 3:
            simple_rect = (50, 50)
            DISPLAYSURF.blit(simple_surf, simple_rect)
        if BOARDWIDTH == 4:
            high_rect = (50, 50)
            DISPLAYSURF.blit(high_surf, high_rect)
    if message:
        textSurf, textRect = makeText(message, MESSAGECOLOR, 5, 5, 25)
        DISPLAYSURF.blit(textSurf, textRect)

    for tilex in range(BOARDWIDTH):
        for tiley in range(BOARDHEIGHT):
            if board[tilex][tiley]:
                drawTile(tilex, tiley, board[tilex][tiley])
            else:
                drawTile(tilex, tiley, False)
    left, top = getLeftTopOfTile(0, 0)
    width = BOARDWIDTH * TILESIZE
    height = BOARDHEIGHT * TILESIZE
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (left - 5, top - 5, width + 11, height + 11), 4)
    DISPLAYSURF.blit(RESET_SURF, RESET_RECT)
    DISPLAYSURF.blit(SOLVE_SURF, SOLVE_RECT)
    DISPLAYSURF.blit(TIMES_BG_SURF, TIMES_BG_RECT)
    DISPLAYSURF.blit(TIMES_SURF, TIMES_RECT)
    DISPLAYSURF.blit(BACK_SURF, BACK_RECT)
    if mode == "picture":
        DISPLAYSURF.blit(HIDE_NUM_SURF, HIDE_NUM_RECT)
        DISPLAYSURF.blit(HIDE_NUM_TEXT_SURF, HIDE_NUM_TEXT_RECT)




def slideAnimation(board, direction, message, animationSpeed):
    # Note: This function does not check if the move is valid.

    blankx, blanky = getBlankPosition(board)
    if direction == UP:
        movex = blankx
        movey = blanky + 1
    elif direction == DOWN:
        movex = blankx
        movey = blanky - 1
    elif direction == LEFT:
        movex = blankx + 1
        movey = blanky
    elif direction == RIGHT:
        movex = blankx - 1
        movey = blanky

    # prepare the base surface
    DISPLAYSURF.blit(STARTBGFILE,(0, 0))
    drawBoard(board, message)
    baseSurf = DISPLAYSURF.copy()   #copy方法
    moveLeft, moveTop = getLeftTopOfTile(movex, movey)
    pygame.draw.rect(baseSurf, BLANK_TILE_COLOR, (moveLeft, moveTop, TILESIZE, TILESIZE))
        #绘制空白方块
    for i in range(0, TILESIZE, animationSpeed):
        checkForQuit()
        DISPLAYSURF.blit(baseSurf, (0, 0))
        if direction == UP:
            drawTile(movex, movey, board[movex][movey], 0, -i)  #移动方块
        if direction == DOWN:
            drawTile(movex, movey, board[movex][movey], 0, i)
        if direction == LEFT:
            drawTile(movex, movey, board[movex][movey], -i, 0)
        if direction == RIGHT:
            drawTile(movex, movey, board[movex][movey], i, 0)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def generateNewPuzzle(numSlides):
    # From a starting configuration, make numSlides number of moves (and
    # animate these moves).
    sequence = []
    board = getStartingBoard()
    drawBoard(board, '')
    pygame.display.update()
    pygame.time.wait(500) # pause 500 milliseconds for effect
    lastMove = None
    for i in range(numSlides):
        move = getRandomMove(board, lastMove)
        slideAnimation(board, move, '生成游戏中...', animationSpeed=int(TILESIZE / 2))
        makeMove(board, move)
        sequence.append(move)
        lastMove = move
    return (board, sequence)


def resetAnimation(board, allMoves):
    # make all of the moves in allMoves in reverse.
    revAllMoves = allMoves[:] # gets a copy of the list
    revAllMoves.reverse()

    for move in revAllMoves:
        if move == UP:
            oppositeMove = DOWN
        elif move == DOWN:
            oppositeMove = UP
        elif move == RIGHT:
            oppositeMove = LEFT
        elif move == LEFT:
            oppositeMove = RIGHT
        slideAnimation(board, oppositeMove, '', animationSpeed=int(TILESIZE / 2))
        makeMove(board, oppositeMove)
if __name__ == '__main__':
    main()
