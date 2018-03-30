from pawn import Pawn

class Board:
    def __init__(self):
        self.pawn_coordinates={'w': [[3, 7], [6, 0], [1, 5], [7, 1], [7, 3], [7, 5], [7, 7]],
                               'b': [[0, 0], [0, 2], [1, 3], [3, 3], [1, 1], [2, 0]]}
        '''self.pawn_coordinates={'w':[[5,1],[5,3],[5,5],[5,7],
                                    [6,0],[6,2],[6,4],[6,6],
                                    [7,1],[7,3],[7,5],[7,7]],
                               'b':[[0,0],[0,2],[0,4],[0,6],
                                    [1,1],[1,3],[1,5],[1,7],
                                    [2,0],[2,2],[2,4],[2,6]]}'''
        self.pawns_that_can_beat=[]    
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
        self.alphabet=['A','B','C','D','E','F','G','H']
        self.starting_coordinates=None
        self.ending_coordinates=None
        self.all_pawn_positions=None

    def check_if_eligible_for_promotion(self, now_moves,ending_coordinates):
        if now_moves=='w' and ending_coordinates in [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7]]:
            return True
        elif now_moves=='b' and ending_coordinates in [[7,0],[7,1],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7]]:
            return True
        else:
            return False
        
    def create_pawns(self):     
        for color in self.pawn_coordinates.keys():
            for number in range(len(self.pawn_coordinates[color])):
                self.pawns[str(number+1)+color]=Pawn(color,self.pawn_coordinates[color][number])                           
    
    def list_pawn_coordinates(self):
        self.pawn_coordinates['w']=[]
        self.pawn_coordinates['b']=[]

        for item in self.pawns.keys():
            self.pawn_coordinates[self.pawns[item].color].append(self.pawns[item].position)
            
    def update_board(self):
        self.all_pawn_positions=list(self.pawn_coordinates.values())
        self.all_pawn_positions=self.all_pawn_positions[0]+self.all_pawn_positions[1]
        for color in self.pawn_coordinates.keys():
            for i in range(8):
                for j in range (8):
                    if [i,j] in self.pawn_coordinates[color]:
                        for item in self.pawns.keys():
                            if self.pawns[item].position==[i,j]:
                                if self.pawns[item].king:
                                    self.board[i][j]=' ' + color.upper() + ' |'
                                else:
                                    self.board[i][j]=' ' + color.lower() + ' |'
                    elif [i,j] not in self.all_pawn_positions:
                        self.board[i][j]='   |'

    def display_board(self):
        print('','   1  ','2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ')       
        for index, line in enumerate(self.board):
            print(' '+self.alphabet[index],''.join(line))
            print('  ','___|'*8)

    def update_pawn_movements(self):
        for item in self.pawns.keys():
            self.pawns[item].return_possible_regular_movements(self.all_pawn_positions)
            self.pawns[item].return_possible_beatings(self.all_pawn_positions,self.pawn_coordinates[{'w':'b','b':'w'}[self.now_moves]],self.now_moves)

        
    def switch_player(self):
        players={'w':'b','b':'w'}
        self.now_moves=players[self.now_moves]

    def display_queue_status(self):
        print("Now moves: "+self.now_moves)


    def mark_pawns_that_can_beat(self):
        self.pawns_that_can_beat=[]
        
        for item in self.pawns.keys():
            if self.pawns[item].possible_beating and self.pawns[item].color==self.now_moves:
                self.pawns_that_can_beat.append(self.pawns[item].position)
                
    
    def ask_for_starting_coordinates(self):
        self.mark_pawns_that_can_beat()
        
        while True:
            try:
                self.starting_coordinates=input("Which pawn do you want to move? (q to exit): ")
                self.starting_coordinates=self.translate_coordinates(self.starting_coordinates)
                if self.pawns_that_can_beat and self.starting_coordinates not in self.pawns_that_can_beat:
                    print("Beating is possible, select a pawn which can beat!")
                    continue

                elif self.pawns_that_can_beat and self.starting_coordinates in self.pawns_that_can_beat:
                    break
                
                elif not self.pawns_that_can_beat and self.starting_coordinates in self.pawn_coordinates[self.now_moves]:
                    break
                else:
                    raise ValueError
            except SystemExit:
                exit()
            except ValueError:
                print("Invalid coordinates for a pawn, please input these again.")
                continue

    def return_possible_movements_of_a_pawn(self,position,option):
        for item in self.pawns.keys():
            if self.pawns[item].position==position:
                if option==1:
                    return self.pawns[item].possible_movement+self.pawns[item].possible_beating
                elif option==2:
                    return self.pawns[item].possible_movement
                elif option==3:
                    return self.pawns[item].possible_beating


    def is_beating_ending_correct(self):
        ending_moves=self.return_possible_movements_of_a_pawn(self.starting_coordinates,3)
        if ending_moves:
            for coordinates in ending_moves:
                if self.ending_coordinates in coordinates or self.ending_coordinates==coordinates:
                    return True
        return False
           
    def ask_for_ending_coordinates(self):
        
        while True:
            try:
                self.ending_coordinates=input("Where do you want to move? (q to exit): ")
                self.ending_coordinates=self.translate_coordinates(self.ending_coordinates)
                #ending coordinates - add function which will check if the ones inserted are correct
                if self.return_possible_movements_of_a_pawn(self.starting_coordinates,3) and not self.is_beating_ending_correct:
                    print("This pawn can beat. Input again...")
                    continue
                
                elif self.ending_coordinates in self.return_possible_movements_of_a_pawn(self.starting_coordinates,1):
                    break
                else:
                    raise ValueError
            except SystemExit:
                exit()
            except ValueError:
                print("Invalid coordinates for destination, please input these again.")
                continue
        
    def translate_coordinates(self,coordinates_to_translate):
        if coordinates_to_translate=='q':
            exit()
        else:
            coordinates=list(coordinates_to_translate)
            coordinates[1]=int(coordinates[1])-1
            coordinates[0]=self.alphabet.index(coordinates[0].upper())
            return coordinates

    def update_board_variables(self):
        self.list_pawn_coordinates()
        self.update_pawn_movements
        

    def display_actual_board(self):
        self.update_board()
        self.display_board()

    def remove_beaten_pawn(self,beaten_position):
        for item in self.pawns.keys():
            if self.pawns[item].position==beaten_position:
                self.pawns.pop(item)
                break
            
    def check_if_another_beating_possible(self):
        for item in self.pawns.keys():
            if self.pawns[item].position==self.ending_coordinates:
                self.pawns[item].return_possible_beatings_continued(self.all_pawn_positions,
                                                                    self.pawn_coordinates[{'w':'b','b':'w'}[self.now_moves]],
                                                                    self.now_moves)
                if not self.pawns[item].possible_beating:
                    return False
                else:
                    self.starting_coordinates=self.ending_coordinates
                    self.update_board_variables()
                    self.display_actual_board()
                    self.ask_for_ending_coordinates()
                    return True
    
    def make_a_move(self):
        must_move=True
        
        while must_move==True:
            if self.ending_coordinates in self.return_possible_movements_of_a_pawn(self.starting_coordinates,2):
                for item in self.pawns.keys():
                    if self.starting_coordinates==self.pawns[item].position:
                        self.pawns[item].position=self.ending_coordinates
                        if self.check_if_eligible_for_promotion(self.now_moves,self.ending_coordinates):
                            self.pawns[item].king=True
                must_move=False
            #beating logic needs to be added in here    
            elif self.ending_coordinates in self.return_possible_movements_of_a_pawn(self.starting_coordinates,3):
                for item in self.pawns.keys():
                    if self.starting_coordinates==self.pawns[item].position:
                        self.pawns[item].position=self.ending_coordinates
                        beaten_coordinates=self.pawns[item].corresponding_beaten[self.pawns[item].possible_beating.index(self.ending_coordinates)]

                self.remove_beaten_pawn(beaten_coordinates)
                must_move=self.check_if_another_beating_possible()
                   
if __name__=='__main__':

    board=Board()
    board.create_pawns()
    board.update_board_variables()
    board.display_actual_board()
    
    while True:
        board.display_queue_status()
        board.update_pawn_movements()
        board.ask_for_starting_coordinates()

        board.ask_for_ending_coordinates()
        board.make_a_move()
        board.update_board_variables()
        board.display_actual_board()
        board.pawn_coordinates

  
        
        board.switch_player()
        


        


