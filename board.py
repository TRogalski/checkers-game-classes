from pawn import Pawn

class Board:
    def __init__(self):
        self.whites_coordinates=[[5,1],[5,3],[5,5],[5,7],[6,0],[6,2],[6,4],[6,6],[7,1],[7,3],[7,5],[7,7]]
        self.blacks_coordinates=[[0,0],[0,2],[0,4],[0,6],[1,1],[1,3],[1,5],[1,7],[2,0],[2,2],[2,4],[2,6]]       
        self.whites={}
        self.blacks={}
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
        
    def print_game_message(self):
        print("Welcome to checkers!")

    def create_pawns(self):
        for number in range(12):
            self.whites[number]=Pawn('w',self.whites_coordinates[number],'w'+str(number))
            self.blacks[number]=Pawn('b',self.blacks_coordinates[number],'b'+str(number))
            
    def print_pawn_positions(self):
        for key in self.whites:
            self.whites[key].print_pawn_position()
        for key in self.blacks:
            self.blacks[key].print_pawn_position()

    def update_board(self):
        for i in range(8):
            for j in range (8):
                if [i,j] in self.whites_coordinates:
                    self.board[i][j]=' w |'
                elif[i,j] in self.blacks_coordinates:
                    self.board[i][j]=' b |'
                else:
                    self.board[i][j]='   |'

    def print_board(self):
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
    board_game=Board()
    board_game.print_game_message()
    board_game.create_pawns()
    print("Now moves: ",board_game.now_moves)
          
    while board_game.keep_playing==True:
        board_game.update_board()
        board_game.print_board()
        board_game.ask_for_movement()
        board_game.switch_player()
    
