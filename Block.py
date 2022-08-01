import pygame
import numpy

import Constants as C


class Block:

    def __init__(self, rectList = None, colour = 'RED', orientation = 'N', flipped = True, position = (0,0) ):
        '''


        '''

        if(rectList == None):
            self.corners = [[0, 1, 0], [1, 1, 1], [1, 0, 0]]
        self.colour  = colour
        self.orientation = orientation
        self.flipped = flipped
        self.positionLU = position
        self.positionRD = (position[0] + len(self.corners[0]), position[1] + len(self.corners))

    def setBlockPos(self, position = (0,0)):
        self.positionLU = position


    def draw(self, screen):
        for row_id, row_val in enumerate(self.corners):
            for col_id, col_val in enumerate(row_val):
                if col_val == True:
                    pygame.draw.rect(screen, self.colour, (C.BLOCK_SIZE * (col_id + self.positionLU[0]), C.BLOCK_SIZE * (row_id + self.positionLU[1]), C.BLOCK_SIZE, C.BLOCK_SIZE))
                    pygame.draw.rect(screen, (255,255,255), (C.BLOCK_SIZE * (col_id + self.positionLU[0]) + 5, C.BLOCK_SIZE * (row_id + self.positionLU[1]) + 5, C.BLOCK_SIZE - 10, C.BLOCK_SIZE - 10))

    def flipp(self):
        new = []
        for row in self.corners:
            new.append(row[::-1])
        self.corners = new

    def move(self, direction):
        if(direction == "LEFT"):
            if (self.positionLU[0] >= 1):
                self.positionRD = (self.positionRD[0] - 1, self.positionRD[1])
                self.positionLU = (self.positionLU[0] - 1, self.positionLU[1])
        elif(direction == 'UP'):
            if(self.positionLU[1] >= 1):
                self.positionRD = (self.positionRD[0], self.positionRD[1] - 1)
                self.positionLU = (self.positionLU[0], self.positionLU[1] - 1)
        elif(direction == 'DOWN'):
            print(self.positionRD[0])
            if (self.positionRD[1] <= 18):
                self.positionRD = (self.positionRD[0], self.positionRD[1] + 1)
                self.positionLU = (self.positionLU[0], self.positionLU[1] + 1)
        elif(direction == 'RIGHT'):
            print(self.positionRD[0])
            if (self.positionRD[0] <= 18):
                self.positionRD = (self.positionRD[0] + 1, self.positionRD[1])
                self.positionLU = (self.positionLU[0] + 1, self.positionLU[1])
    def turn(self, direction):
        l = self.corners
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
