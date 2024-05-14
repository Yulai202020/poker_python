class Player:
    def __init__(self, hand):
        self.hand = hand
    
    def get_hand(self):
        return self.hand
    
    def set_hand(self, new_hand):
        self.hand = new_hand
