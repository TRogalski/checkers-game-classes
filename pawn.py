class Pawn():

    def __init__(self,color,position):
        self.color=color
        self.position=position
        self.possible_movement=[]
        self.possible_beating=[]
        self.corresponding_beaten=[]
        self.did_beat=False
        self.king=False
        
        if self.color=='w':
            self.regular_moves=[[-1,-1],[-1,1]]
            self.regular_beating_moves=[[-2,-2],[-2,2]]
        elif self.color=='b':
            self.regular_moves=[[1,-1],[1,1]]
            self.regular_beating_moves=[[2,-2],[2,2]]
        
    def return_possible_regular_movements(self,pawn_coordinates):
        self.possible_movement=[]
        if self.king:
            self.possible_movement=self.return_checked_possible_king_moves(pawn_coordinates)
        else:
            for coordinate in self.regular_moves:
                candidate_coordinate=[x+y for x,y in zip (coordinate,self.position)]
                if candidate_coordinate not in pawn_coordinates and self.check_if_within_board(candidate_coordinate):
                    self.possible_movement.append(candidate_coordinate)
        #print(self.position,self.return_checked_possible_king_moves(pawn_coordinates))
        
    def check_if_within_board(self,coordinate):
        coordinate=[number for number in coordinate if number>=0 and number<=7]
        if len(coordinate)==2:
            return True
        else:
            return False
        
    def return_possible_beatings(self,pawn_coordinates,enemy_pawn_coordinates,now_moves):
        self.possible_beating=[]
        self.corresponding_beaten=[]
        if now_moves==self.color:
            if self.king:
                self.return_possible_king_beatings(pawn_coordinates,enemy_pawn_coordinates,now_moves)
            else:
                for coordinate_1, coordinate_2 in zip(self.regular_moves,self.regular_beating_moves):
                    candidate_coordinate=[x+y for x,y in zip (coordinate_2,self.position)]
                    candidate_beating=[x+y for x,y in zip (coordinate_1,self.position)]
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
            for coordinate_1, coordinate_2 in zip(four_directions_moves,multiple_beating_moves):
                candidate_coordinate=[x+y for x,y in zip(coordinate_2,self.position)]
                candidate_beating=[x+y for x,y in zip(coordinate_1,self.position)]

                if all([candidate_coordinate not in pawn_coordinates,
                        self.check_if_within_board(candidate_coordinate),
                        candidate_beating in enemy_pawn_coordinates]):
                    self.possible_beating.append(candidate_coordinate)
                    self.corresponding_beaten.append(candidate_beating)

    def return_possible_king_beatings(self,pawn_coordinates,enemy_pawn_coordinates,now_moves):
        self.possible_beating=[]
        self.corresponding_beaten=[]
        candidate_coord=[]
        preceeding=[]
        #succeeding=[]
        moves_to_be_checked=self.return_candidate_king_moves()

        for coordinates in enemy_pawn_coordinates:
            if coordinates in moves_to_be_checked:
                diffs=[(x-y)/abs(x-y) for x,y in zip(coordinates,self.position)]
                dist=abs(coordinates[0]-self.position[0])
                for i in range(1,dist+1):
                    candidate_coord=[x*i+y for x,y in zip(diffs,self.position)]
                    preceeding.append(candidate_coord)
                    print(len(preceeding))
                    '''candidate_coord=[x*i+y for x,y in zip(diffs,coordinates)]
                    if candidate_coord[0]>=0 and candidate_coord[0]<=7 and candidate_coord[1]>=0 and candidate_coord[1]<=7:
                        succeeding.append(candidate_coord)'''
                path_clear=True
                if len(preceeding)>1:
                    for i in range (0,len(preceeding)-1):
                        if preceeding[i:i+1] in pawn_coordinates:
                            path_clear=False
                            break
                free_field=[int(x+y) for x,y in zip (diffs,coordinates)]
                if path_clear and free_field not in pawn_coordinates and free_field[0]>=0 and free_field[0]<=7 and free_field[1]>=0 and free_field[1]<=7:
                    self.possible_beating.append(free_field)
                    self.corresponding_beaten.append(coordinates)
        

    def return_possible_king_beatings_continued(self,pawn_coordinates,enemy_pawn_coordinates,now_moves):
        pass

    def return_candidate_king_moves(self):
        possible_moves=[[-1,1],[1,-1],[-1,-1],[1,1]]

        raw_movement_candidates=[]     
        for item in possible_moves:
            for multiplier in range(1,8):
                raw_movement_candidates.append([multiplier*coordinate for coordinate in item])

        final_possible_movements=[]
        for item in raw_movement_candidates:
            final_possible_movements.append([x+y for x,y in zip(self.position,item)])
        final_possible_movements=[i for i in final_possible_movements if i[0]>=0 and i[0]<=7 and i[1]>=0 and i[1]<=7]
        return final_possible_movements

    def return_checked_possible_king_moves(self,pawn_coordinates):
        moves_to_be_checked=self.return_candidate_king_moves()

        candidate_to_be_removed=[]
        
        for coordinates in pawn_coordinates:
            if coordinates in moves_to_be_checked:
                moves_to_be_checked.remove(coordinates)
                diffs=[(x-y)/abs(x-y) for x,y in zip(coordinates,self.position)]

                candidate_to_be_removed=[x+y for x,y in zip(coordinates,diffs)]
                i=1
                while candidate_to_be_removed in moves_to_be_checked:
                    moves_to_be_checked.remove(candidate_to_be_removed)
                    i+=1
                    candidate_to_be_removed=[x+y*i for x,y in zip(coordinates,diffs)]

        return moves_to_be_checked
