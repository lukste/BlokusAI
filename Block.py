import pygame

import Constants as C


class Block:

    def __init__(self, rectList = None, colour = 'RED', orientation = 'N', flipped = True ):
        if(rectList == None):
            self._corners = [[0,1,0],[1,1,1],[1,0,0]]
            #[pygame.Rect(50,0,C.BLOCK_SIZE, C.BLOCK_SIZE), pygame.Rect(0,50,C.BLOCK_SIZE, C.BLOCK_SIZE), pygame.Rect(50,50,C.BLOCK_SIZE, C.BLOCK_SIZE), pygame.Rect(100,50,C.BLOCK_SIZE, C.BLOCK_SIZE), pygame.Rect(0,100,C.BLOCK_SIZE, C.BLOCK_SIZE)]
        self.colour  = colour
        self.orientation = orientation
        self.flipped = flipped

    def setBlockPos(self, position = (0,0)):
        for row in self._corners:
            pass


    def draw(self, screen):
        for row_id, row_val in enumerate(self._corners):
            for col_id, col_val in enumerate(row_val):
                if col_val == True:
                    pygame.draw.rect(screen, self.colour, (C.BLOCK_SIZE*col_id,C.BLOCK_SIZE*row_id, C.BLOCK_SIZE, C.BLOCK_SIZE))

    def flipp(self):
        new = []
        for row in self._corners:
            new.append(row[::-1])
        self._corners = new


    def turn(self, direction):
        l = self._corners
        N = len(l)
        if(direction == 'LEFT'):
            for x in range(N // 2):
                for y in range(N - x - 1):
                    temp = l[x][y]
                    l[x][y] = l[y][N-1-x]
                    l[y][N-1-x] = l[N - 1 - x][N - 1 - y]
                    l[N - 1 - x][N - 1 - y] = l[N-1-y][x]
                    l[N-1-y][x] = temp

        elif(direction == 'RIGHT'):
            for x in range(N // 2):
                for y in range(N - x - 1):
                    temp = l[x][y]
                    l[x][y] = l[N - 1 - y][x]
                    l[N - 1 - y][x] = l[N - 1 - x][N - 1 - y]
                    l[N - 1 - x][N - 1 - y] = l[y][N - 1 - x]
                    l[y][N - 1 - x] = temp
