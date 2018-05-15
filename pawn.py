class Pawn():

    def __init__(self,color,position):
        self.color = color
        self.position = position
        self.possible_movement = []
        self.possible_beating = []
        self.corresponding_beaten = []
        self.did_beat = False
        self.king = False

        if self.color == 'w':
            self.regular_moves = [[-1, -1], [-1, 1]]
            self.regular_beating_moves = [[-2, -2], [-2, 2]]
        elif self.color == 'b':
            self.regular_moves = [[1, -1], [1, 1]]
            self.regular_beating_moves = [[2, -2], [2, 2]]

    def return_possible_regular_movements(self, pawn_coordinates):
        self.possible_movement = []
        if self.king:
            self.possible_movement = self.return_checked_possible_king_moves(pawn_coordinates)
        else:
            for coordinate in self.regular_moves:
                candidate_coordinate = [x+y for x,y in zip(coordinate, self.position)]
                if candidate_coordinate not in pawn_coordinates and self.check_if_within_board(candidate_coordinate):
                    self.possible_movement.append(candidate_coordinate)

    def check_if_within_board(self, coordinate):
        coordinate = [number for number in coordinate if number >= 0 and number <= 7]
        if len(coordinate) == 2:
            return True
        else:
            return False

    def return_possible_beatings(self, pawn_coordinates, enemy_pawn_coordinates,now_moves):
        self.possible_beating = []
        self.corresponding_beaten = []
        if now_moves == self.color:
            if self.king:
                self.return_possible_king_beatings(pawn_coordinates, enemy_pawn_coordinates, now_moves)
            else:
                for coordinate_1, coordinate_2 in zip(self.regular_moves, self.regular_beating_moves):
                    candidate_coordinate = [x+y for x,y in zip (coordinate_2, self.position)]
                    candidate_beating = [x+y for x,y in zip (coordinate_1, self.position)]
                    if all([candidate_coordinate not in pawn_coordinates,
                           self.check_if_within_board(candidate_coordinate),
                           candidate_beating in enemy_pawn_coordinates]):
                        self.possible_beating.append(candidate_coordinate)
                        self.corresponding_beaten.append(candidate_beating)
            
    def return_possible_beatings_continued(self,pawn_coordinates,enemy_pawn_coordinates,now_moves):
        self.possible_beating=[]
        self.corresponding_beaten=[]
        four_directions_moves=[[-1,-1],[-1,1],[1,-1],[1,1]]
        multiple_beating_moves=[[-2,-2],[-2,2],[2,-2],[2,2]]
        if now_moves==self.color:
            if self.king:
                self.return_possible_king_beatings(pawn_coordinates,enemy_pawn_coordinates,now_moves)
            else:
                for coordinate_1, coordinate_2 in zip(four_directions_moves,multiple_beating_moves):
                    candidate_coordinate=[x+y for x,y in zip(coordinate_2,self.position)]
                    candidate_beating=[x+y for x,y in zip(coordinate_1,self.position)]

                    if all([candidate_coordinate not in pawn_coordinates,
                            self.check_if_within_board(candidate_coordinate),
                            candidate_beating in enemy_pawn_coordinates]):
                        self.possible_beating.append(candidate_coordinate)
                        self.corresponding_beaten.append(candidate_beating)

    def return_step_type(self, target_coordinates, source_coordinates):
        return [(x-y)/abs(x-y) for x,y in zip(source_coordinates, target_coordinates)]

    def return_preceeding(self, coordinates, diffs):
        preceeding = []
        candidate_coord = [] 
        dist = abs(coordinates[0]-self.position[0])

        for i in range(0, dist):
            candidate_coord=[x*i+y for x,y in zip(diffs, coordinates)]
            if self.check_if_within_board(candidate_coord):
                preceeding.append(candidate_coord)
        return preceeding

    def return_succeeding(self, coordinates, diffs):
        canditdate_coord = []
        succeeding = []

        for i in range(0,7):
            candidate_coord=[-x*i+y for x,y in zip(diffs, coordinates)]
            if self.check_if_within_board(candidate_coord):
                succeeding.append(candidate_coord)
        return succeeding        

    def check_if_path_clear(self, preceeding, pawn_coordinates):
        if len(preceeding)>0:
            for i in range (0, len(preceeding)+2):     
                if preceeding[i:i+2]:
                    if preceeding[i:i+2] in pawn_coordinates:
                        return False
        return True

    def return_possible_ending_moves(self, diffs, coordinates, succeeding, pawn_coordinates):
        possible_ending_moves = []
        possible_ending_moves.append([int(-x+y) for x,y in zip (diffs, coordinates)])

        if len(succeeding)>1:
            for i in range(1, len(succeeding)-1):
                if all(x not in pawn_coordinates for x in [succeeding[i], succeeding[i+1]]):
                    possible_ending_moves.append(succeeding[i+1])
        return possible_ending_moves
    
    def return_possible_king_beatings(self, pawn_coordinates, enemy_pawn_coordinates, now_moves):
        self.possible_beating = []
        self.corresponding_beaten = []
        moves_to_be_checked = self.return_candidate_king_moves()

        for coordinates in enemy_pawn_coordinates:
            if coordinates in moves_to_be_checked:
                diffs=self.return_step_type(coordinates, self.position)
                dist=abs(coordinates[0]-self.position[0])
                preceeding=self.return_preceeding(coordinates, diffs)
                succeeding=self.return_succeeding(coordinates, diffs)
                path_to_pawn_clear=self.check_if_path_clear(preceeding, pawn_coordinates)
                possible_ending_moves=self.return_possible_ending_moves(diffs, coordinates, succeeding, pawn_coordinates)
                if path_to_pawn_clear:
                    self.possible_beating.append(possible_ending_moves)
                    self.corresponding_beaten.append(coordinates)
        print("Possible beating:",self.possible_beating)
        print("Corresponding beaten:",self.corresponding_beaten)

    def return_candidate_king_moves(self):
        possible_moves = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
        raw_movement_candidates = []     
        for item in possible_moves:
            for multiplier in range(1,7):
                raw_movement_candidates.append([multiplier*coordinate for coordinate in item])
        final_possible_movements = []
        for item in raw_movement_candidates:
            final_possible_movements.append([x+y for x,y in zip(self.position,item)])
        final_possible_movements = [i for i in final_possible_movements if self.check_if_within_board(i)]
        return final_possible_movements

    def return_checked_possible_king_moves(self, pawn_coordinates):
        moves_to_be_checked = self.return_candidate_king_moves()
        candidate_to_be_removed = []
        
        for coordinates in pawn_coordinates:
            if coordinates in moves_to_be_checked:
                moves_to_be_checked.remove(coordinates)
                diffs=[(x-y)/abs(x-y) for x,y in zip(coordinates,self.position)]
                candidate_to_be_removed = [x+y for x,y in zip(coordinates,diffs)]
                i=1
                while candidate_to_be_removed in moves_to_be_checked:
                    moves_to_be_checked.remove(candidate_to_be_removed)
                    i+=1
                    candidate_to_be_removed = [x+y*i for x,y in zip(coordinates,diffs)]
        return moves_to_be_checked
