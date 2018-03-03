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
            
        for coordinate in self.regular_moves:
            candidate_coordinate=[x+y for x,y in zip (coordinate,self.position)]
            if candidate_coordinate not in pawn_coordinates and self.check_if_within_board(candidate_coordinate):
                self.possible_movement.append(candidate_coordinate)
           

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


