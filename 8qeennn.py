import pygame
import sys
def main():
    field = [[0 for i in range(8)] for j in range(8)]
    count = 8
    setup(field)
    while count > 0:
        view()
        print("a")
        
def check(field_view,color_1,color_2,i,j,field):
    field[i][j] = 2
    for i_1 in range(8):
        field[i][i_1] = 1
        field[i_1][j] = 1
        color_1[i][i_1] = 255
        color_2[i][i_1] = 0
        color_1[i_1][j] = 255
        color_2[i_1][j] = 0
    color_1[i][j] = 255
    color_2[i][j] = 255
    return (field_view,color_1,color_2,i,j,field)
            
    
def setup(field):
    pygame.init()
    screen = pygame.display.set_mode((490,490))
    pygame.display.set_caption("8qeen")
    field_view = [[0 for i in range(8)] for j in range(8)]
    color_1 = [[100 for i in range(8)] for j in range(8)]
    color_2 = [[200 for i in range(8)] for j in range(8)]    
    flag = False
    font = pygame.font.SysFont(None, 130)
    text = font.render("8Queen", True, (0,0,0))
    font1 = pygame.font.SysFont(None, 50)
    text1 = font1.render("Retry to Press \"R\"", True, (0,0,0))
    view(color_1,color_2,screen,field_view,field,flag,text,text1)

def view(color_1,color_2,screen,field_view,field,flag,text,text1):
    while (1):
        count = 0
        for i in range(8):
            for j in range(8):
                if field[i][j] > 0:
                    count+=1
                if count == 64:
                    flag = True
                    screen.blit(text, (80,180))
                    screen.blit(text1, (100,280))
        pygame.display.flip()
        screen.fill((255,255,255))


            
        for i in range(8):
            for j in range(8):
                field_view[i][j] = pygame.draw.rect(screen,(color_1[i][j],color_2[i][j],0),(10+i*60,10+j*60,50,50))
        x,y = pygame.mouse.get_pos()
        
        #イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and flag == True:
                if event.key == pygame.K_r:
                    main()
            for i in range(8):
                for j in range(8):
                    if event.type == pygame.MOUSEBUTTONDOWN and field_view[i][j].collidepoint(x,y) == 1 and color_1[i][j] != 255:
                        check(field_view,color_1,color_2,i,j,field)
 
if __name__ == "__main__":
        main()
