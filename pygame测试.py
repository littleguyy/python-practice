# py -3.6 -m pip install pygame # 用这指令装pygame
import pygame

pygame.init()
游戏分辨率=pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')
时钟=pygame.time.Clock()

崩=False

while not 崩:

    for 事件 in pygame.event.get():
        if 事件.type == pygame.QUIT:
            崩=True

        print(事件)
    pygame.display.update()
    时钟.tick(60)
pygame.quit()
quit()
