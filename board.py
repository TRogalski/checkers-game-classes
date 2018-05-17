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
        for item in self.pawns.keys():
            self.pawns[item].return_possible_regular_movements(self.pawn_coordinates['w']+self.pawn_coordinates['b'])
            self.pawns[item].return_possible_beatings()
        
    def switch_player(self):
        players={'w': 'b','b': 'w'}
        self.now_moves = players[self.now_moves]

    def display_queue_status(self):
        print("Now moves: "+self.now_moves)

    def mark_pawns_that_can_beat(self):
        self.pawns_that_can_beat = []

        for item in self.pawns.keys():
            if self.pawns[item].possible_beating and self.pawns[item].color == self.now_moves:
                self.pawns_that_can_beat.append(self.pawns[item].position)
  
    def ask_for_starting_coordinates(self):
        self.mark_pawns_that_can_beat()
        self.starting_coordinates = input("Which pawn do you want to move? (q to exit): ")
        self.starting_coordinates = self.translate_coordinates(self.starting_coordinates)

    def ask_for_ending_coordinates(self):
        self.ending_coordinates=input("Where do you want to move? (q to exit): ")
        self.ending_coordinates=self.translate_coordinates(self.ending_coordinates)

    def translate_coordinates(self, coordinates_to_translate):
        coordinates = list(coordinates_to_translate)
        coordinates[1] = int(coordinates[1])-1
        coordinates[0] = self.alphabet.index(coordinates[0].upper())
        return coordinates

    def make_a_move(self):
        for item in self.pawns.keys():
            if self.pawns[item].position==self.starting_coordinates:
                print(self.pawns[item].possible_movement)
                
    def return_possible_movements_of_a_pawn(self, position, option):
        for item in self.pawns.keys():
            if self.pawns[item].position == position:
                if option == 1:
                    return self.pawns[item].possible_movement+self.pawns[item].possible_beating
                elif option == 2:
                    return self.pawns[item].possible_movement
                elif option == 3:
                    return self.pawns[item].possible_beating

    def update_board_variables(self):
        self.list_pawn_coordinates()
        self.update_pawn_movements()

    def display_actual_board(self):
        self.update_board()
        self.display_board()

        
if __name__ == '__main__':
    board = Board()
    board.create_pawns()
    board.update_board_variables()
    board.display_actual_board()
    while True:
        board.display_queue_status()
        board.update_pawn_movements()
        board.ask_for_starting_coordinates()
        board.ask_for_ending_coordinates()
        board.make_a_move()
        board.switch_player()
        
