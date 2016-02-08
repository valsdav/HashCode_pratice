
class Block:
    
    def __init__(self, x,y, drawn, filled = False ):
        self.x = x
        self.y = y 
        self.drawn = drawn
        self.filled = filled
        
    def fill(self):
        self.filled = True
        
    def unfill(self):
        self.filled = False
        
    def is_good(self):
        return (self.drawn and not self.filled)
    
    def is_good_l(self):
        return self.drawn
    
