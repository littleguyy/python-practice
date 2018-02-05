# py -3.6 -m pip install pygame # 用这指令装pygame
import pygame
import time

pygame.init()

窗口高=600
窗口宽=800

黑=(0,0,0)
白=(255,255,255)
红=(255,0,0)

游戏画面=pygame.display.set_mode((窗口宽,窗口高))
pygame.display.set_caption('游戏测试')
时钟=pygame.time.Clock()

图=pygame.image.load('images.jpg')

def 图位置(x,y):
        游戏画面.blit(图,(x,y))

def text_objects(text, font):
        textSurface=font.render(text,True,黑)
        return textSurface, textSurface.get_rect()


def 显示文本(文本):
        largeText=pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect=text_objects(文本,largeText)
        TextRect.center=((窗口宽/2),(窗口高/2))
        游戏画面.blit(TextSurf, TextRect)

        pygame.display.update()
        
        time.sleep(2)

        
        

def 提示(text):
        显示文本(text)

def 游戏循环():
        x=(窗口宽*0.45)
        y=(窗口高*0.5)

        退=False

        while not 退:

            for 事件 in pygame.event.get():
                if 事件.type == pygame.QUIT:
                        退=True
                        
                print(事件)
            
            if 事件.type == pygame.MOUSEMOTION:
                    x,y=事件.pos
            游戏画面.fill(白)
            图位置(x,y)

            pygame.display.update()
            时钟.tick(60)

游戏循环()
提示('Bye Bye!')
pygame.quit()
quit()
