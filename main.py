import pygame
import Block

pygame.init()

screen = pygame.display.set_mode((800, 600))


running = True
b = Block.Block()
b.setBlockPos((100,100))
while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.KEYDOWN):
            if(event.key==pygame.K_SPACE):
                b.flipp()
            if(event.key==pygame.K_RIGHT):
                b.turn("RIGHT")
            if (event.key == pygame.K_LEFT):
                b.turn("LEFT")
            #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 50, 50))
    screen.fill((0, 0, 0))
    b.draw(screen)
    pygame.display.flip()