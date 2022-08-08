import pygame.draw
import Constants as C
import numpy as np
import Block

colors = { "" : 0, 'RED' : 1, 'BLUE' : 2, 'GREEN' : 3, 'YELLOW' : 4}


class Board:
    def __init__(self):
        self.n = 22
        self.status = np.zeros((self.n,self.n),np.int8)
        self.setup()
        self.text_obj = []
        self.text_rect = []
        for i in range(self.n):
            self.text_obj.append([])
            self.text_rect.append([])
        for i in range(self.n):
            for j in range(self.n):
                self.text_obj[i].append(pygame.font.SysFont(None, 20).render(str(i) + " " + str(j), True, (0, 0, 0)))
                self.text_rect[i].append(self.text_obj[i][j].get_rect())
                self.text_rect[i][j].topleft = (C.BLOCK_SIZE * i + 5, C.BLOCK_SIZE * j + 5)


    def setup(self):
        # rb = Block.Block([[1]], 'RED', position=(0,0))
        # self.place(rb)
        # bb = Block.Block([[1]], 'BLUE', position=(self.n -1, 0))
        # self.place(bb)
        # gb = Block.Block([[1]], 'GREEN', position=(0, self.n -1 ))
        # self.place(gb)
        # yb = Block.Block([[1]], 'YELLOW', position=(self.n-1, self.n-1))
        # self.place(yb)
        self.status[0][0] = 1
        self.status[self.n - 1][0] = 2
        self.status[0][self.n - 1] = 3
        self.status[self.n - 1][self.n -1] = 4



    def check_contact(self, block):
        x, y = block.positionLU
        col = colors[block.colour]
        for row_id, row_val in enumerate(block.corners):
            for col_id, col_val in enumerate(row_val):
                if col_val == True:
                    if (self.status[col_id + x][row_id + y] != 0):
                        return False
                    try:
                        print("checking", col_id + x + 1, row_id + y + 1, self.status[col_id + x + 1][row_id + y + 1])
                        print("checking", col_id + x - 1, row_id + y -1, self.status[col_id + x - 1][row_id + y - 1])
                        if (self.status[col_id + x + 1][row_id + y + 1] == col or
                            self.status[col_id + x - 1][row_id + y - 1] == col or
                            self.status[col_id + x + 1][row_id + y - 1] == col or
                            self.status[col_id + x - 1][row_id + y + 1] == col ):

                            return True
                    except:
                        pass
        return False

    def checkPlace(self, block):
        x,y  = block.positionLU
        col  = colors[block.colour]
        for row_id, row_val in enumerate(block.corners):
            for col_id, col_val in enumerate(row_val):
                if col_val == True:
                    if(self.status[col_id+x][row_id + y] != 0):
                        return False
                    try:
                        if(self.status[col_id+x+1][row_id + y] == col or
                       self.status[col_id+x-1][row_id + y] == col or
                       self.status[col_id+x][row_id + y+1] == col or
                       self.status[col_id+x][row_id + y-1] == col):
                            return False
                    except:
                        pass
        return self.check_contact(block)

    def place(self, block):
        if(self.checkPlace(block)):
            for row_id, row_val in enumerate(block.corners):
                for col_id, col_val in enumerate(row_val):
                    if col_val == True:
                        self.status[col_id + block.positionLU[0]][row_id + block.positionLU[1]] = colors[block.colour]
            return True
        else:
            return False


    def draw(self, screen):
        for i in range(self.n):
            for j in range(self.n):
                pygame.draw.rect(screen, C.colorsRGB[self.status[i][j]][0], (C.BLOCK_SIZE*i, C.BLOCK_SIZE*j, C.BLOCK_SIZE, C.BLOCK_SIZE))
                pygame.draw.rect(screen, (255, 255, 255),
                                 (C.BLOCK_SIZE * i + 5, C.BLOCK_SIZE * j + 5, C.BLOCK_SIZE - 10,
                                  C.BLOCK_SIZE - 10))
                screen.blit(self.text_obj[i][j], self.text_rect[i][j])

