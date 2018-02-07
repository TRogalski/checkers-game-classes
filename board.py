from pawn import Pawn

class Board:
    def __init__(self):
        self.pawn_coordinates={'w':[[5,1],[5,3],[5,5],[5,7],[6,0],[6,2],[6,4],[6,6],[7,1],[7,3],[7,5],[7,7]],
                                  'b':[[0,0],[0,2],[0,4],[0,6],[1,1],[1,3],[1,5],[1,7],[2,0],[2,2],[2,4],[2,6]]}
      
        self.pawns={}
        
        self.board=[['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '']]

        self.now_moves='w'
        self.keep_playing=True
        self.alphabet=['A','B','C','D','E','F','G','H']

    def create_pawns(self):
        for number in range(12):
            for color in self.pawn_coordinates.keys():
                self.pawns[str(number+1)+color]=Pawn(color,self.pawn_coordinates[color][number])                           
    
    def list_pawn_coordinates(self):
        self.pawn_coordinates['w']=[]
        self.pawn_coordinates['b']=[]

        for item in self.pawns.keys():
            self.pawn_coordinates[self.pawns[item].color].append(self.pawns[item].position)
            
    def update_board(self):
        all_pawn_positions=list(self.pawn_coordinates.values())
        all_pawn_positions=all_pawn_positions[0]+all_pawn_positions[1]
        for color in self.pawn_coordinates.keys():
            for i in range(8):
                for j in range (8):
                    if [i,j] in self.pawn_coordinates[color]:
                        self.board[i][j]=' ' + color + ' |'
                    elif [i,j] not in all_pawn_positions:
                        self.board[i][j]='   |'

    def display_board(self):
        print('','   1  ','2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ')       
        for index, line in enumerate(self.board):
            print(' '+self.alphabet[index],''.join(line))
            print('  ','___|'*8)
        
    def switch_player(self):
        players={'w':'b','b':'w'}
        self.now_moves=players[self.now_moves]
        print("Now moves: ", self.now_moves)

    def ask_for_movement(self):
        starting_position=input("Which pawn do you want to move?: ")
        end_position=input("Where do you want to move this pawn?: ")
#######################################################################################
        self.check_if_move_is_valid(starting_position,end_position)

    def check_if_move_is_valid(self,starting_position,end_position):

        starting_position=self.translate_coordinates(starting_position)
        end_position=self.translate_coordinates(end_position)

        if all([self.check_if_now_moves_is_on_starting_position(starting_position),
               self.check_if_end_position_is_occupied(end_position)]):
            if self.check_if_beating_is_being_done(starting_position,end_position):
                if self.now_moves=='w':
                    self.whites_coordinates[self.whites_coordinates.index(starting_position)]=end_position
                elif self.now_moves=='b':
                    self.blacks_coordinates[self.blacks_coordinates.index(starting_position)]=end_position
            else:                
                if self.check_if_move_in_right_direction(starting_position,end_position):
                    if self.now_moves=='w':
                        self.whites_coordinates[self.whites_coordinates.index(starting_position)]=end_position
                    else:
                        self.blacks_coordinates[self.blacks_coordinates.index(starting_position)]=end_position
        print(starting_position,end_position)

    def check_if_beating_is_being_done(self,starting_position,end_position):
        differences=[y-x for x,y in zip(starting_position,end_position)]
        if self.now_moves=='w' and differences in [[-2,2],[-2,-2]]:
            if [x+y for x,y in zip(starting_position,[-1,-1])] in self.blacks_coordinates:
                self.blacks_coordinates.pop(self.blacks_coordinates.index([x+y for x,y in zip(starting_position,[-1,-1])]))
                return True
            if [x+y for x,y in zip(starting_position,[-1,1])] in self.blacks_coordinates:
                self.blacks_coordinates.pop(self.blacks_coordinates.index([x+y for x,y in zip(starting_position,[-1,1])]))
                return True
        if self.now_moves=='b' and differences in [[2,2],[-2,2]]:
            if [x+y for x,y in zip(starting_position,[1,-1])] in self.whites_coordinates:
                self.whites_coordinates.pop(self.whites_coordinates.index([x+y for x,y in zip(starting_position,[1,-1])]))
                return True
            if [x+y for x,y in zip(starting_position,[1,1])] in self.whites_coordinates:
                self.whites_coordinates.pop(self.whites_coordinates.index([x+y for x,y in zip(starting_position,[1,1])]))
                return True
        return False
                
    def check_if_now_moves_is_on_starting_position(self,starting_position):
        if self.now_moves=='w' and starting_position in self.whites_coordinates:
            return True
        if self.now_moves=='b' and starting_position in self.blacks_coordinates:
            return True
        return False

    def check_if_end_position_is_occupied(self,end_position):
        if end_position in self.whites_coordinates or end_position in self.blacks_coordinates:
            return False
        else:
            return True

    def check_if_move_in_right_direction(self,starting_position,end_position):
        differences=[y-x for x,y in zip(starting_position,end_position)]
        if self.now_moves=='w' and differences in [[-1,-1],[-1,1]]:
            return True
        if self.now_moves=='b' and differences in [[1,-1],[1,1]]:
            return True
        return False
    
    def translate_coordinates(self,coordinates_to_translate):
        coordinates_to_translate=list(coordinates_to_translate)
        coordinates_to_translate[1]=int(coordinates_to_translate[1])-1
        coordinates_to_translate[0]=self.alphabet.index(coordinates_to_translate[0].upper())
        return coordinates_to_translate
    
if __name__=='__main__':

    board=Board()
    board.create_pawns()
    board.update_board()
    board.display_board()


        


