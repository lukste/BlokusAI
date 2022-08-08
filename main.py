import pygame
import Block
import BlockSet
import Board
import Player
from BlockSet import *
import Constants as C
from itertools import cycle

pygame.init()

screen = pygame.display.set_mode((C.BLOCK_SIZE * 22, C.BLOCK_SIZE * 22))

clock = pygame.time.Clock()
running = True
bs = BloSet()
#print(bs.randomBlock())
#print("bs: ", bs.blocks)


p1 = Player.Player("RED")
p2 = Player.Player("BLUE")
p3 = Player.Player("GREEN")
p4 = Player.Player("YELLOW")

players = [p1,p2,p3,p4]
players_cycle = cycle(players)
current_player = next(players_cycle)
b = current_player.next_block(position=(0,0))
board = Board.Board()
b.stick(board)


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
                if board.place(b):
                    current_player.place_block(b)
                    current_player = next(players_cycle)
                    b = current_player.next_block()
                    b.stick(board)
            if(event.key == pygame.K_q):
                b = current_player.next_block(position=(b.positionLU[0], b.positionLU[1]))
                b.stick(board)
        clock.tick(60)
    screen.fill((0, 0, 0))

    board.draw(screen)
    b.draw(screen)
    pygame.display.flip()