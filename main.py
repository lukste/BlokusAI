import pygame
import Block
import BlockSet
import Board
from BlockSet import *
import Constants as C


pygame.init()

screen = pygame.display.set_mode((C.BLOCK_SIZE * 20, C.BLOCK_SIZE * 20))


running = True
bs = BloSet()
#print(bs.randomBlock())
#print("bs: ", bs.blocks)
b = bs.randomBlock()

board = Board.Board()
while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if (event.type == pygame.KEYDOWN):
            if(event.key==pygame.K_SPACE):
                b.flipp()
            if(event.key == pygame.K_RIGHT):
                b.move("RIGHT")
            if (event.key == pygame.K_LEFT):
                b.move("LEFT")
            if (event.key == pygame.K_UP):
                b.move("UP")
            if (event.key == pygame.K_DOWN):
                b.move("DOWN")
            if (event.key == pygame.K_a):
                b.turn("LEFT")
            if (event.key == pygame.K_d):
                b.turn("RIGHT")
            if (event.key == pygame.K_RETURN):
                board.place(b)
            #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 50, 50))
    screen.fill((0, 0, 0))

    board.draw(screen)
    b.draw(screen)
    pygame.display.flip()