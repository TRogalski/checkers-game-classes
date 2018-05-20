import sys


from pawn import Pawn

class Board:
    def __init__(self):
        '''self.pawn_coordinates = {'w': [[3, 7], [6, 0], [1, 5], [7, 1], [7, 3], [7, 5], [7, 7]],
                               'b': [[0, 0], [0, 2], [1, 3], [3, 3], [1, 1], [2, 0]]}'''
        self.pawn_coordinates={'w':[[5,1],[5,3],[5,5],[5,7],
                                    [6,0],[6,2],[6,4],[6,6],
                                    [7,1],[7,3],[7,5],[7,7]],
                               'b':[[0,0],[0,2],[0,4],[0,6],
                                    [1,1],[1,3],[1,5],[1,7],
                                    [2,0],[2,2],[2,4],[2,6]]}
        self.pawns_that_can_beat = []    
        self.pawns = {}
        self.board = [['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '']]

        self.now_moves = 'w'
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.starting_coordinates = None
        self.ending_coordinates = None
        self.all_pawn_positions = None
        
    def create_pawns(self):     
        for color in self.pawn_coordinates.keys():
            for number in range(len(self.pawn_coordinates[color])):
                self.pawns[str(number+1)+color] = Pawn(color, self.pawn_coordinates[color][number])                           
    
    def list_pawn_coordinates(self):
        self.pawn_coordinates['w'] = []
        self.pawn_coordinates['b'] = []

        for item in self.pawns.keys():
            self.pawn_coordinates[self.pawns[item].color].append(self.pawns[item].position)
            
    def update_board(self):
        self.all_pawn_positions = list(self.pawn_coordinates.values())
        self.all_pawn_positions = self.all_pawn_positions[0]+self.all_pawn_positions[1]
        for color in self.pawn_coordinates.keys():
            for i in range(8):
                for j in range (8):
                    if [i, j] in self.pawn_coordinates[color]:
                        for item in self.pawns.keys():
                            if self.pawns[item].position == [i, j]:
                                if self.pawns[item].king:
                                    self.board[i][j]=' ' + color.upper() + ' |'
                                else:
                                    self.board[i][j]=' ' + color.lower() + ' |'
                    elif [i, j] not in self.all_pawn_positions:
                        self.board[i][j]='   |'

    def display_board(self):
        print('','   1  ', '2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ')       
        for index, line in enumerate(self.board):
            print(' '+self.alphabet[index], ''.join(line))
            print('  ', '___|'*8)

    def update_pawn_movements(self):
        ally_color=self.now_moves
        enemy_color={'w':'b','b':'w'}[ally_color]
        
        for item in self.pawns.keys():
            self.pawns[item].return_possible_regular_movements(self.pawn_coordinates)
            self.pawns[item].return_possible_beatings(self.pawn_coordinates)

    def update_routine(self):
        self.list_pawn_coordinates()
        self.update_pawn_movements()
        self.update_board()
        self.display_board()
        
    def switch_player(self):
        players={'w': 'b','b': 'w'}
        self.now_moves = players[self.now_moves]

    def quit_qame(self):
        print("Thank you for playing!")
        sys.exit()
        
    def display_queue_status(self):
        print("Now moves: "+self.now_moves)

    def mark_pawns_that_can_beat(self):
        self.pawns_that_can_beat = []
        for item in self.pawns.keys():
            if self.pawns[item].possible_beating and self.pawns[item].color == self.now_moves:
                self.pawns_that_can_beat.append(self.pawns[item].position)
  
    def ask_for_starting_coordinates(self):
        self.mark_pawns_that_can_beat()
        print("Can beat:",self.pawns_that_can_beat)
        while True:
            self.starting_coordinates = input("Which pawn do you want to move? (q to exit): ")

            if self.starting_coordinates=="q":
                self.quit_qame()

            try:   
                self.starting_coordinates = self.translate_coordinates(self.starting_coordinates)

            except:
                print("Please insert valid pawn coordinates.")
                continue

            if self.starting_coordinates not in self.pawn_coordinates[self.now_moves]:
                print("Select pawn of your color.")
                continue
            
            if all([self.pawns_that_can_beat,
                    self.starting_coordinates not in self.pawns_that_can_beat]):
                print("There are pawns which can beat, please select one of them.")
                continue

            if all([not self.get_possible_moves(self.starting_coordinates),
                    self.starting_coordinates not in self.pawns_that_can_beat]):
                print("Selected pawn position is incorrect, please try again.")
                continue
            break

    def ask_for_ending_coordinates(self):
        print("Selected pawn: ",self.starting_coordinates)      
        while True:
            self.ending_coordinates=input("Where do you want to move? (q to exit): ")
            
            if self.ending_coordinates=="q":
                self.quit_qame()

            try:
                self.ending_coordinates=self.translate_coordinates(self.ending_coordinates)
            except:
                print("Please insert valid pawn coordinates.")
                continue

            beating_moves=self.get_possible_beatings(self.starting_coordinates)
            king=self.get_pawn_rank(self.starting_coordinates)
            
            if all([king,
                    beating_moves,
                    not self.ending_coordinates_in_beating_moves(beating_moves,self.ending_coordinates)]):
                print("Selected pawn can beat, please pick correct beating coordinates.")
                continue

            if all([not king,
                    beating_moves,
                    self.ending_coordinates not in beating_moves]):
                print("Selected pawn can beat, please pick correct beating coordinates.")
                continue

            if all([not beating_moves,
                    self.ending_coordinates not in self.get_possible_moves(self.starting_coordinates)]):
                print("This pawn cannot move there, please input valid coordinates.")
                continue
            break
                
    def translate_coordinates(self, coordinates_to_translate):
        coordinates = list(coordinates_to_translate)
        coordinates[1] = int(coordinates[1])-1
        coordinates[0] = self.alphabet.index(coordinates[0].upper())
        return coordinates

    def move(self):

        possible_beatings=self.check_if_beating_possible(self.starting_coordinates)
        
        if possible_beatings:
            while True:
                self.make_a_beating()
                self.update_routine()
                self.starting_coordinates=self.ending_coordinates[:]
                possible_beatings=self.check_if_beating_possible(self.starting_coordinates)
                if possible_beatings:
                    self.ask_for_ending_coordinates()
                else:
                    break
            #below line only if no other moves are possilbe
            self.promote_if_eligible(self.ending_coordinates)
            
        else:
            self.make_a_move()
            self.promote_if_eligible(self.ending_coordinates)
            self.update_routine()
        
    
    def make_a_move(self):
        for item in self.pawns.keys():
            if all([self.pawns[item].position==self.starting_coordinates,
                    self.ending_coordinates in self.pawns[item].possible_movement]):
                self.pawns[item].position=self.ending_coordinates
                break

    def make_a_beating(self):
        beating_moves=self.get_possible_beatings(self.starting_coordinates)
        corresponding_beaten=self.get_corresponding_beaten(self.starting_coordinates)
        king=self.get_pawn_rank(self.starting_coordinates)

        if king:
            print("TUTAJ",self.ending_coordinates_in_beating_moves(beating_moves,self.ending_coordinates))
            if self.ending_coordinates_in_beating_moves(beating_moves,self.ending_coordinates):
                corresponding_beaten_index=self.return_corresponding_beaten_index(beating_moves,self.ending_coordinates)
                print(corresponding_beaten_index)
                pawn_to_be_removed=corresponding_beaten[corresponding_beaten_index]
                self.remove_a_pawn(pawn_to_be_removed)
                self.update_position(self.starting_coordinates,self.ending_coordinates)
                
        else:
            if self.ending_coordinates in beating_moves:
                corresponding_beaten_index=beating_moves.index(self.ending_coordinates)
                pawn_to_be_removed=corresponding_beaten[corresponding_beaten_index]
                self.remove_a_pawn(pawn_to_be_removed)
                self.update_position(self.starting_coordinates,self.ending_coordinates)

    def return_corresponding_beaten_index(self,beating_moves,position):
        beating_index=0
        for item in beating_moves:

            if any([position==item,
                    position in item]):
                return beating_index
            beating_index+=1
           
    def ending_coordinates_in_beating_moves(self,beating_moves,position):
        for item in beating_moves:

            if any([position in item,
                    position==item]):
                return True
  
        return False

    def get_pawn_rank(self,position):
        for item in self.pawns.keys():
            if self.pawns[item].position==position:
                return self.pawns[item].king

    def update_position(self,starting_position,ending_position):
        for item in self.pawns.keys():
            if self.pawns[item].position==starting_position:
                self.pawns[item].position=ending_position
                break
        
    def get_possible_beatings(self,position):
        for item in self.pawns.keys():
            if self.pawns[item].position==position:
                return self.pawns[item].possible_beating
                
    
    def get_corresponding_beaten(self,position):
        for item in self.pawns.keys():
            if self.pawns[item].position==position:
                return self.pawns[item].corresponding_beaten

    def get_possible_moves(self,position):
        for item in self.pawns.keys():
            if self.pawns[item].position==position:
                return self.pawns[item].possible_movement
    
    def remove_a_pawn(self,position):
        for item in self.pawns.keys():
            if self.pawns[item].position==position:
                del self.pawns[item]
                break

    def check_if_beating_possible(self,position):
        for item in self.pawns.keys():
            if self.pawns[item].position==position:
                if len(self.pawns[item].possible_beating)>0:
                    return True
                else:
                    return False
                
    def promote_if_eligible(self,position):
        #this has to happen after the final move was made
        promotion_fields={'b':[[7,1],[7,3],[7,5],[7,7]],'w':[[0,0],[0,2],[0,4],[0,6]]}
        if position in promotion_fields[self.now_moves]:
            self.promote_a_pawn(position)

    def promote_a_pawn(self,position):
        for item in self.pawns.keys():
            if self.pawns[item].position==position:
                self.pawns[item].king=True
                break
    
    def update_board_variables(self):
        self.list_pawn_coordinates()
        self.update_pawn_movements()

    def display_actual_board(self):
        self.update_board()
        self.display_board()



    def return_game_status(self):
        white_pawns=len(self.pawn_coordinates['w'])
        black_pawns=len(self.pawn_coordinates['b'])

        print("Remaining whites: ",white_pawns,"Remaining blacks:",black_pawns)

        if any([white_pawns==0,
                black_pawns==0]):
            self.quit_game()
        
    
if __name__ == '__main__':
    board = Board()
    board.create_pawns()
    board.update_routine()
    while True:
        board.return_game_status()
        board.display_queue_status()
        board.ask_for_starting_coordinates()
        board.ask_for_ending_coordinates()
        board.move()
        board.switch_player()
        
