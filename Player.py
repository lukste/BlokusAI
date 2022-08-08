import BlockSet
from itertools import cycle

class Player:

    def __init__(self, color = 'RED'):
        self.blocks = BlockSet.BloSet().get_block_set(color)
        self.blocks_cycle = cycle(self.blocks)
        self.color = color
        self.i = 0



    def place_block(self, block):
        self.blocks.pop(block)

    def next_block(self, position=(0,0)):
        b = next(self.blocks_cycle)
        b.setBlockPos(position)
        return b