class Pawn():

    def __init__(self,color,position,pawn_id):
        self.pawn_id=pawn_id
        self.color=color
        self.position=position

    def print_pawn_position(self):
        print(self.position,self.pawn_id,self.color)
