import random
import Constants as C
import Block


class BloSet:
    def __init__(self):
        print("Running")
        self.b1 = [[1]]
        self.b2 = [[1], [1]]
        self.b3 = [[1, 0],[1, 1]]
        self.b4 = [[1, 1],[1, 1]]
        self.b5 = [[0, 1, 0],[1, 1, 1],[1, 0, 0]]
        self.b6 = [[1, 1, 1, 1, 1]]
        self.b7 = [[1, 0, 0, 0],[1, 1, 1, 1]]
        self.b8 = [[1, 1, 1],
              [0, 1, 0],
              [0, 1, 0]]
        self.b9 = [[0, 1, 1],
              [0, 1, 0],
              [1, 1, 0]]
        self.b10 = [[1, 0, 0],
               [1, 0, 0],
               [1, 1, 1]]
        self.b11 = [[1, 0, 1],
               [1, 1, 1]]
        self.b12 = [[0, 0, 1, 0],
               [1, 1, 1, 1]]
        self.b13 = [[1, 1, 1, 0],
               [0, 0, 1, 1]]
        self.b14 = [[1, 1, 1],
               [1, 1, 0]]
        self.b15 = [[1, 0, 0],
               [1, 1, 0],
               [0, 1, 1]]
        self.b16 = [[0, 1, 0],
               [1, 1, 1]]
        self.b17 = [[1, 0, 0],
                    [1, 1, 1]]
        self.b18 = [[1, 1, 0],[0, 1, 1]]

        self.blocks = [getattr(self, 'b'+str(i)) for i in range(1,19)]
        print(self.blocks)

    def randomBlock(self, color = None):
        pass
        if color == None:
            return Block.Block(random.choice(self.blocks), random.choice(C.COLORS))
        else:
            return Block.Block(random.choice(self.blocks), color)

