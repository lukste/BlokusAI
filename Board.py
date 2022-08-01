import pygame.draw
import Constants as C
import Block

colors = { "" : 0, 'RED' : 1, 'BLUE' : 2, 'GREEN' : 3, 'YELLOW' : 4}


class Board:
    def __init__(self):
        self.n = 20
        self.status = []
        for i in range(self.n):
            self.status.append([])
            for j in range(self.n):
                self.status[i].append(0)
        # for i in range(self.n):
        #     print()
        #     for j in range(self.n):
        #         print(self.status[i][j], end=',')

    def place(self, block):
        for row_id, row_val in enumerate(block.corners):
            for col_id, col_val in enumerate(row_val):
                if col_val == True:
                    self.status[col_id+block.position[0]][row_id + block.position[1]] = colors[block.colour]
        print()
        for i in range(self.n):
            print()
            for j in range(self.n):
                print(self.status[j][i], end=',')

    def draw(self, screen):
        for i in range(self.n):
            for j in range(self.n):
                pygame.draw.rect(screen, C.colorsRGB[self.status[i][j]][0], (C.BLOCK_SIZE*i, C.BLOCK_SIZE*j, C.BLOCK_SIZE, C.BLOCK_SIZE))
                pygame.draw.rect(screen, (255, 255, 255), (C.BLOCK_SIZE * i +5, C.BLOCK_SIZE* j +5, C.BLOCK_SIZE-10,
                                 C.BLOCK_SIZE-10))
