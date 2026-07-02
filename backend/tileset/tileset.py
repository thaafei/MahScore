from meld import Meld, Pair 


class TileSet():
    def __init__(self):
        self.melds = []
        self.pair = []
    
    def add_meld(self, meld: Meld):
        self.melds = self.melds + meld
    
