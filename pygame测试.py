# py -3.6 -m pip install pygame # 用这指令装pygame
import pygame

pygame.init()

窗口高=600
窗口宽=800

黑=(0,0,0)
白=(255,255,255)
红=(255,0,0)

游戏分辨率=pygame.display.set_mode((窗口宽,窗口高))
pygame.display.set_caption('游戏测试')
时钟=pygame.time.Clock()

图=pygame.image.load('i:/images.jpg')

def 图位置(x,y):
    游戏分辨率.blit(图,(x,y))

x=(窗口宽*0.45)
y=(窗口高*0.5)

崩=False

while not 崩:

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            崩=True
        # print(事件)
        
        
    游戏分辨率.fill(白)
    if 事件.type == pygame.MOUSEMOTION:
        x,y=事件.pos
    图位置(x,y)
    
    pygame.display.update()
    时钟.tick(60)
    
pygame.quit()
quit()
