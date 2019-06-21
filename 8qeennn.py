# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys
import time

def main():
    pygame.init()                                               # Pygameの初期化
    screen = pygame.display.set_mode((490,490))                # 大きさ600*500の画面を生成
    pygame.display.set_caption("GAME")                          # タイトルバーに表示する文字
    
    flag_1 = False
    flag_2 = False
    flag_3 = False
    flag_4 = False
    flag_5 = False
    flag_6 = False
    flag_7 = False
    flag_8 = False
    flag_R = False
    
    field = [[0 for i in range(8)] for j in range(8)]
    color_1 = [[100 for i in range(8)] for j in range(8)]
    color_2 = [[200 for i in range(8)] for j in range(8)]
    color_3 = int(0)
    
    font = pygame.font.SysFont(None, 130)
    text = font.render("8Queen", True, (0,255,255))
    font1 = pygame.font.SysFont(None, 50)
    text1 = font1.render("Retry to Press \"R\"", True, (0,255,255))

    while (1):
        pygame.display.update()                                 # 画面を更新
        screen.fill((0,0,0))                                    # 画面を黒色に塗りつぶし

        for i in range(8):
            for j in range(8):
                field[i][j] = pygame.draw.rect(screen,(color_1[i][j],color_2[i][j],color_3),(10+i*60,10+j*60,50,50))
        
        if flag_1 == True and flag_2 == True and flag_3 == True and flag_4 == True and flag_5 == True and flag_6 == True and flag_7 == True and flag_8 == True:
            screen.blit(text, (80,180))
            screen.blit(text1, (100,280))
            flag_R = True
            
        x,y = pygame.mouse.get_pos()
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:                              # 閉じるボタンが押されたら終了
                pygame.quit()                                   # Pygameの終了(画面閉じられる)
                sys.exit()
                
            if event.type == KEYDOWN and flag_R == True:
                if event.key == K_r:
                    main()

            #8*8マス全チェック 
            if event.type == MOUSEBUTTONDOWN and field[0][0].collidepoint(x,y) == 1 and color_1[0][0] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][0] = 255
                            color_2[i][0] = 0
                            color_1[0][j] = 255
                            color_2[0][j] = 0
                    color_1[0][0] = 255
                    color_2[0][0] = 255
                    flag_1 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[1][0].collidepoint(x,y) == 1 and color_1[1][0] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][0] = 255
                            color_2[i][0] = 0
                            color_1[1][j] = 255
                            color_2[1][j] = 0
                    color_1[1][0] = 255
                    color_2[1][0] = 255
                    flag_1 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[2][0].collidepoint(x,y) == 1 and color_1[2][0] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][0] = 255
                            color_2[i][0] = 0
                            color_1[2][j] = 255
                            color_2[2][j] = 0
                    color_1[2][0] = 255
                    color_2[2][0] = 255
                    flag_1 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[3][0].collidepoint(x,y) == 1 and color_1[3][0] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][0] = 255
                            color_2[i][0] = 0
                            color_1[3][j] = 255
                            color_2[3][j] = 0
                    color_1[3][0] = 255
                    color_2[3][0] = 255
                    flag_1 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[4][0].collidepoint(x,y) == 1 and color_1[4][0] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][0] = 255
                            color_2[i][0] = 0
                            color_1[4][j] = 255
                            color_2[4][j] = 0
                    color_1[4][0] = 255
                    color_2[4][0] = 255
                    flag_1 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[5][0].collidepoint(x,y) == 1 and color_1[5][0] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][0] = 255
                            color_2[i][0] = 0
                            color_1[5][j] = 255
                            color_2[5][j] = 0
                    color_1[5][0] = 255
                    color_2[5][0] = 255
                    flag_1 = True

            if event.type == MOUSEBUTTONDOWN and field[6][0].collidepoint(x,y) == 1 and color_1[6][0] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][0] = 255
                            color_2[i][0] = 0
                            color_1[6][j] = 255
                            color_2[6][j] = 0
                    color_1[6][0] = 255
                    color_2[6][0] = 255
                    flag_1 = True

            if event.type == MOUSEBUTTONDOWN and field[7][0].collidepoint(x,y) == 1 and color_1[7][0] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][0] = 255
                            color_2[i][0] = 0
                            color_1[7][j] = 255
                            color_2[7][j] = 0
                    color_1[7][0] = 255
                    color_2[7][0] = 255
                    flag_1 = True

            if event.type == MOUSEBUTTONDOWN and field[0][1].collidepoint(x,y) == 1 and color_1[0][1] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][1] = 255
                            color_2[i][1] = 0
                            color_1[0][j] = 255
                            color_2[0][j] = 0
                    color_1[0][1] = 255
                    color_2[0][1] = 255
                    flag_2 = True

            if event.type == MOUSEBUTTONDOWN and field[1][1].collidepoint(x,y) == 1 and color_1[1][1] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][1] = 255
                            color_2[i][1] = 0
                            color_1[1][j] = 255
                            color_2[1][j] = 0
                    color_1[1][1] = 255
                    color_2[1][1] = 255
                    flag_2 = True

            if event.type == MOUSEBUTTONDOWN and field[2][1].collidepoint(x,y) == 1 and color_1[2][1] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][1] = 255
                            color_2[i][1] = 0
                            color_1[2][j] = 255
                            color_2[2][j] = 0
                    color_1[2][1] = 255
                    color_2[2][1] = 255
                    flag_2 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[3][1].collidepoint(x,y) == 1 and color_1[3][1] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][1] = 255
                            color_2[i][1] = 0
                            color_1[3][j] = 255
                            color_2[3][j] = 0
                    color_1[3][1] = 255
                    color_2[3][1] = 255
                    flag_2 = True

            if event.type == MOUSEBUTTONDOWN and field[4][1].collidepoint(x,y) == 1 and color_1[4][1] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][1] = 255
                            color_2[i][1] = 0
                            color_1[4][j] = 255
                            color_2[4][j] = 0
                    color_1[4][1] = 255
                    color_2[4][1] = 255
                    flag_2 = True

            if event.type == MOUSEBUTTONDOWN and field[5][1].collidepoint(x,y) == 1 and color_1[5][1] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][1] = 255
                            color_2[i][1] = 0
                            color_1[5][j] = 255
                            color_2[5][j] = 0
                    color_1[5][1] = 255
                    color_2[5][1] = 255
                    flag_2 = True

            if event.type == MOUSEBUTTONDOWN and field[6][1].collidepoint(x,y) == 1 and color_1[6][1] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][1] = 255
                            color_2[i][1] = 0
                            color_1[6][j] = 255
                            color_2[6][j] = 0
                    color_1[6][1] = 255
                    color_2[6][1] = 255
                    flag_2 = True

            if event.type == MOUSEBUTTONDOWN and field[7][1].collidepoint(x,y) == 1 and color_1[7][1] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][1] = 255
                            color_2[i][1] = 0
                            color_1[7][j] = 255
                            color_2[7][j] = 0
                    color_1[7][1] = 255
                    color_2[7][1] = 255
                    flag_2 = True

            if event.type == MOUSEBUTTONDOWN and field[0][2].collidepoint(x,y) == 1 and color_1[0][2] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][2] = 255
                            color_2[i][2] = 0
                            color_1[0][j] = 255
                            color_2[0][j] = 0
                    color_1[0][2] = 255
                    color_2[0][2] = 255
                    flag_3 = True

            if event.type == MOUSEBUTTONDOWN and field[1][2].collidepoint(x,y) == 1 and color_1[1][2] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][2] = 255
                            color_2[i][2] = 0
                            color_1[1][j] = 255
                            color_2[1][j] = 0
                    color_1[1][2] = 255
                    color_2[1][2] = 255
                    flag_3 = True

            if event.type == MOUSEBUTTONDOWN and field[2][2].collidepoint(x,y) == 1 and color_1[2][2] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][2] = 255
                            color_2[i][2] = 0
                            color_1[2][j] = 255
                            color_2[2][j] = 0
                    color_1[2][2] = 255
                    color_2[2][2] = 255
                    flag_3 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[3][2].collidepoint(x,y) == 1 and color_1[3][2] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][2] = 255
                            color_2[i][2] = 0
                            color_1[3][j] = 255
                            color_2[3][j] = 0
                    color_1[3][2] = 255
                    color_2[3][2] = 255
                    flag_3 = True
                                        
            if event.type == MOUSEBUTTONDOWN and field[4][2].collidepoint(x,y) == 1 and color_1[4][2] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][2] = 255
                            color_2[i][2] = 0
                            color_1[4][j] = 255
                            color_2[4][j] = 0
                    color_1[4][2] = 255
                    color_2[4][2] = 255
                    flag_3 = True
                                        
            if event.type == MOUSEBUTTONDOWN and field[5][2].collidepoint(x,y) == 1 and color_1[5][2] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][2] = 255
                            color_2[i][2] = 0
                            color_1[5][j] = 255
                            color_2[5][j] = 0
                    color_1[5][2] = 255
                    color_2[5][2] = 255
                    flag_3 = True

            if event.type == MOUSEBUTTONDOWN and field[6][2].collidepoint(x,y) == 1 and color_1[6][2] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][2] = 255
                            color_2[i][2] = 0
                            color_1[6][j] = 255
                            color_2[6][j] = 0
                    color_1[6][2] = 255
                    color_2[6][2] = 255
                    flag_3 = True
                                
            if event.type == MOUSEBUTTONDOWN and field[7][2].collidepoint(x,y) == 1 and color_1[7][2] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][2] = 255
                            color_2[i][2] = 0
                            color_1[7][j] = 255
                            color_2[7][j] = 0
                    color_1[7][2] = 255
                    color_2[7][2] = 255
                    flag_3 = True
                                                
            if event.type == MOUSEBUTTONDOWN and field[0][3].collidepoint(x,y) == 1 and color_1[0][3] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][3] = 255
                            color_2[i][3] = 0
                            color_1[0][j] = 255
                            color_2[0][j] = 0
                    color_1[0][3] = 255
                    color_2[0][3] = 255
                    flag_4 = True
                                                
            if event.type == MOUSEBUTTONDOWN and field[1][3].collidepoint(x,y) == 1 and color_1[1][3] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][3] = 255
                            color_2[i][3] = 0
                            color_1[1][j] = 255
                            color_2[1][j] = 0
                    color_1[1][3] = 255
                    color_2[1][3] = 255
                    flag_4 = True
                                                                    
            if event.type == MOUSEBUTTONDOWN and field[2][3].collidepoint(x,y) == 1 and color_1[2][3] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][3] = 255
                            color_2[i][3] = 0
                            color_1[2][j] = 255
                            color_2[2][j] = 0
                    color_1[2][3] = 255
                    color_2[2][3] = 255
                    flag_4 = True
                                                                    
            if event.type == MOUSEBUTTONDOWN and field[3][3].collidepoint(x,y) == 1 and color_1[3][3] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][3] = 255
                            color_2[i][3] = 0
                            color_1[3][j] = 255
                            color_2[3][j] = 0
                    color_1[3][3] = 255
                    color_2[3][3] = 255
                    flag_4 = True
                                                                    
            if event.type == MOUSEBUTTONDOWN and field[4][3].collidepoint(x,y) == 1 and color_1[4][3] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][3] = 255
                            color_2[i][3] = 0
                            color_1[4][j] = 255
                            color_2[4][j] = 0
                    color_1[4][3] = 255
                    color_2[4][3] = 255
                    flag_4 = True
                                                                    
            if event.type == MOUSEBUTTONDOWN and field[5][3].collidepoint(x,y) == 1 and color_1[5][3] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][3] = 255
                            color_2[i][3] = 0
                            color_1[5][j] = 255
                            color_2[5][j] = 0
                    color_1[5][3] = 255
                    color_2[5][3] = 255
                    flag_4 = True
                                                                    
            if event.type == MOUSEBUTTONDOWN and field[6][3].collidepoint(x,y) == 1 and color_1[6][3] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][3] = 255
                            color_2[i][3] = 0
                            color_1[6][j] = 255
                            color_2[6][j] = 0
                    color_1[6][3] = 255
                    color_2[6][3] = 255
                    flag_4 = True
                                                                    
            if event.type == MOUSEBUTTONDOWN and field[7][3].collidepoint(x,y) == 1 and color_1[7][3] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][3] = 255
                            color_2[i][3] = 0
                            color_1[7][j] = 255
                            color_2[7][j] = 0
                    color_1[7][3] = 255
                    color_2[7][3] = 255
                    flag_4 = True
                                                                                        
            if event.type == MOUSEBUTTONDOWN and field[0][4].collidepoint(x,y) == 1 and color_1[0][4] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][4] = 255
                            color_2[i][4] = 0
                            color_1[0][j] = 255
                            color_2[0][j] = 0
                    color_1[0][4] = 255
                    color_2[0][4] = 255
                    flag_5 = True

            if event.type == MOUSEBUTTONDOWN and field[1][4].collidepoint(x,y) == 1 and color_1[1][4] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][4] = 255
                            color_2[i][4] = 0
                            color_1[1][j] = 255
                            color_2[1][j] = 0
                    color_1[1][4] = 255
                    color_2[1][4] = 255
                    flag_5 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[2][4].collidepoint(x,y) == 1 and color_1[2][4] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][4] = 255
                            color_2[i][4] = 0
                            color_1[2][j] = 255
                            color_2[2][j] = 0
                    color_1[2][4] = 255
                    color_2[2][4] = 255
                    flag_5 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[3][4].collidepoint(x,y) == 1 and color_1[3][4] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][4] = 255
                            color_2[i][4] = 0
                            color_1[3][j] = 255
                            color_2[3][j] = 0
                    color_1[3][4] = 255
                    color_2[3][4] = 255
                    flag_5 = True
                                                                                           
            if event.type == MOUSEBUTTONDOWN and field[4][4].collidepoint(x,y) == 1 and color_1[4][4] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][4] = 255
                            color_2[i][4] = 0
                            color_1[4][j] = 255
                            color_2[4][j] = 0
                    color_1[4][4] = 255
                    color_2[4][4] = 255
                    flag_5 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[5][4].collidepoint(x,y) == 1 and color_1[5][4] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][4] = 255
                            color_2[i][4] = 0
                            color_1[5][j] = 255
                            color_2[5][j] = 0
                    color_1[5][4] = 255
                    color_2[5][4] = 255
                    flag_5 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[6][4].collidepoint(x,y) == 1 and color_1[6][4] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][4] = 255
                            color_2[i][4] = 0
                            color_1[6][j] = 255
                            color_2[6][j] = 0
                    color_1[6][4] = 255
                    color_2[6][4] = 255
                    flag_5 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[7][4].collidepoint(x,y) == 1 and color_1[7][4] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][4] = 255
                            color_2[i][4] = 0
                            color_1[7][j] = 255
                            color_2[7][j] = 0
                    color_1[7][4] = 255
                    color_2[7][4] = 255
                    flag_5 = True

            if event.type == MOUSEBUTTONDOWN and field[0][5].collidepoint(x,y) == 1 and color_1[0][5] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][5] = 255
                            color_2[i][5] = 0
                            color_1[0][j] = 255
                            color_2[0][j] = 0
                    color_1[0][5] = 255
                    color_2[0][5] = 255
                    flag_6 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[1][5].collidepoint(x,y) == 1 and color_1[1][5] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][5] = 255
                            color_2[i][5] = 0
                            color_1[1][j] = 255
                            color_2[1][j] = 0
                    color_1[1][5] = 255
                    color_2[1][5] = 255
                    flag_6 = True
   
            if event.type == MOUSEBUTTONDOWN and field[2][5].collidepoint(x,y) == 1 and color_1[2][5] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][5] = 255
                            color_2[i][5] = 0
                            color_1[2][j] = 255
                            color_2[2][j] = 0
                    color_1[2][5] = 255
                    color_2[2][5] = 255
                    flag_6 = True
   
            if event.type == MOUSEBUTTONDOWN and field[3][5].collidepoint(x,y) == 1 and color_1[3][5] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][5] = 255
                            color_2[i][5] = 0
                            color_1[3][j] = 255
                            color_2[3][j] = 0
                    color_1[3][5] = 255
                    color_2[3][5] = 255
                    flag_6 = True
            if event.type == MOUSEBUTTONDOWN and field[4][5].collidepoint(x,y) == 1 and color_1[4][5] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][5] = 255
                            color_2[i][5] = 0
                            color_1[4][j] = 255
                            color_2[4][j] = 0
                    color_1[4][5] = 255
                    color_2[4][5] = 255
                    flag_6 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[5][5].collidepoint(x,y) == 1 and color_1[5][5] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][5] = 255
                            color_2[i][5] = 0
                            color_1[5][j] = 255
                            color_2[5][j] = 0
                    color_1[5][5] = 255
                    color_2[5][5] = 255
                    flag_6 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[6][5].collidepoint(x,y) == 1 and color_1[6][5] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][5] = 255
                            color_2[i][5] = 0
                            color_1[6][j] = 255
                            color_2[6][j] = 0
                    color_1[6][5] = 255
                    color_2[6][5] = 255
                    flag_6 = True
   
            if event.type == MOUSEBUTTONDOWN and field[7][5].collidepoint(x,y) == 1 and color_1[7][5] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][5] = 255
                            color_2[i][5] = 0
                            color_1[7][j] = 255
                            color_2[7][j] = 0
                    color_1[7][5] = 255
                    color_2[7][5] = 255
                    flag_6 = True

            if event.type == MOUSEBUTTONDOWN and field[0][6].collidepoint(x,y) == 1 and color_1[0][6] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][6] = 255
                            color_2[i][6] = 0
                            color_1[0][j] = 255
                            color_2[0][j] = 0
                    color_1[0][6] = 255
                    color_2[0][6] = 255
                    flag_7 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[1][6].collidepoint(x,y) == 1 and color_1[1][6] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][6] = 255
                            color_2[i][6] = 0
                            color_1[1][j] = 255
                            color_2[1][j] = 0
                    color_1[1][6] = 255
                    color_2[1][6] = 255
                    flag_7 = True
            
            if event.type == MOUSEBUTTONDOWN and field[2][6].collidepoint(x,y) == 1 and color_1[2][6] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][6] = 255
                            color_2[i][6] = 0
                            color_1[2][j] = 255
                            color_2[2][j] = 0
                    color_1[2][6] = 255
                    color_2[2][6] = 255
                    flag_7 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[3][6].collidepoint(x,y) == 1 and color_1[3][6] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][6] = 255
                            color_2[i][6] = 0
                            color_1[3][j] = 255
                            color_2[3][j] = 0
                    color_1[3][6] = 255
                    color_2[3][6] = 255
                    flag_7 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[4][6].collidepoint(x,y) == 1 and color_1[4][6] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][6] = 255
                            color_2[i][6] = 0
                            color_1[4][j] = 255
                            color_2[4][j] = 0
                    color_1[4][6] = 255
                    color_2[4][6] = 255
                    flag_7 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[5][6].collidepoint(x,y) == 1 and color_1[5][6] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][6] = 255
                            color_2[i][6] = 0
                            color_1[5][j] = 255
                            color_2[5][j] = 0
                    color_1[5][6] = 255
                    color_2[5][6] = 255
                    flag_7 = True
   
            if event.type == MOUSEBUTTONDOWN and field[6][6].collidepoint(x,y) == 1 and color_1[6][6] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][6] = 255
                            color_2[i][6] = 0
                            color_1[6][j] = 255
                            color_2[6][j] = 0
                    color_1[6][6] = 255
                    color_2[6][6] = 255
                    flag_7 = True
   
            if event.type == MOUSEBUTTONDOWN and field[7][6].collidepoint(x,y) == 1 and color_1[7][6] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][6] = 255
                            color_2[i][6] = 0
                            color_1[7][j] = 255
                            color_2[7][j] = 0
                    color_1[7][6] = 255
                    color_2[7][6] = 255
                    flag_7 = True
                    
            if event.type == MOUSEBUTTONDOWN and field[0][7].collidepoint(x,y) == 1 and color_1[0][7] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][7] = 255
                            color_2[i][7] = 0
                            color_1[0][j] = 255
                            color_2[0][j] = 0
                    color_1[0][7] = 255
                    color_2[0][7] = 255
                    flag_8 = True
                                        
            if event.type == MOUSEBUTTONDOWN and field[1][7].collidepoint(x,y) == 1 and color_1[1][7] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][7] = 255
                            color_2[i][7] = 0
                            color_1[1][j] = 255
                            color_2[1][j] = 0
                    color_1[1][7] = 255
                    color_2[1][7] = 255
                    flag_8 = True
                                        
            if event.type == MOUSEBUTTONDOWN and field[2][7].collidepoint(x,y) == 1 and color_1[2][7] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][7] = 255
                            color_2[i][7] = 0
                            color_1[2][j] = 255
                            color_2[2][j] = 0
                    color_1[2][7] = 255
                    color_2[2][7] = 255
                    flag_8 = True
                                        
            if event.type == MOUSEBUTTONDOWN and field[3][7].collidepoint(x,y) == 1 and color_1[3][7] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][7] = 255
                            color_2[i][7] = 0
                            color_1[3][j] = 255
                            color_2[3][j] = 0
                    color_1[3][7] = 255
                    color_2[3][7] = 255
                    flag_8 = True
                                        
            if event.type == MOUSEBUTTONDOWN and field[4][7].collidepoint(x,y) == 1 and color_1[4][7] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][7] = 255
                            color_2[i][7] = 0
                            color_1[4][j] = 255
                            color_2[4][j] = 0
                    color_1[4][7] = 255
                    color_2[4][7] = 255
                    flag_8 = True
                                        
            if event.type == MOUSEBUTTONDOWN and field[5][7].collidepoint(x,y) == 1 and color_1[5][7] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][7] = 255
                            color_2[i][7] = 0
                            color_1[5][j] = 255
                            color_2[5][j] = 0
                    color_1[5][7] = 255
                    color_2[5][7] = 255
                    flag_8 = True
                                        
            if event.type == MOUSEBUTTONDOWN and field[6][7].collidepoint(x,y) == 1 and color_1[6][7] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][7] = 255
                            color_2[i][7] = 0
                            color_1[6][j] = 255
                            color_2[6][j] = 0
                    color_1[6][7] = 255
                    color_2[6][7] = 255
                    flag_8 = True
                                        
            if event.type == MOUSEBUTTONDOWN and field[7][7].collidepoint(x,y) == 1 and color_1[7][7] != 255:
                    for i in range(8):
                        for j in range(8):
                            color_1[i][7] = 255
                            color_2[i][7] = 0
                            color_1[7][j] = 255
                            color_2[7][j] = 0
                    color_1[7][7] = 255
                    color_2[7][7] = 255
                    flag_8 = True
                    
if __name__ == "__main__":
    main()
