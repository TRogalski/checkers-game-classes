class Pawn():

    def __init__(self,color,position):
        self.color = color
        self.position = position
        self.possible_movement = []
        self.possible_beating = []
        self.corresponding_beaten = []
        self.king=False

        self.movement_directions = {'w':[[-1, -1], [-1, 1]],
                                    'b':[[1, 1], [1, -1]]}

        self.beating_directions=[[-1, -1], [-1, 1],
                                 [1, 1], [1, -1]]
        
    def return_possible_regular_movements(self, pawn_coordinates):
        all_pawns = pawn_coordinates['w'] + pawn_coordinates['b']
        directions = self.movement_directions[self.color]
        self.possible_movement = []

        if self.king:
            for direction in self.beating_directions:
                jump_length = 1
                while True:
                    movement_candidate=[x + y * jump_length for x, y in zip(self.position, direction)]
                    if all([self.check_if_within_board(movement_candidate),
                            movement_candidate not in all_pawns]):
                        self.possible_movement.append(movement_candidate)
                        jump_length += 1
                    else:
                        break                                           
        else:
            for direction in directions:
                movement_candidate = [x + y for x, y in zip(self.position, direction)]
                if all([self.check_if_within_board(movement_candidate),
                        movement_candidate not in all_pawns]):
                    self.possible_movement.append(movement_candidate)

    def check_if_within_board(self, coordinate):
        if any([coordinate[0] < 0,
                coordinate[0] > 7,
                coordinate[1] < 0,
                coordinate[1] > 7]):
            return False
        else:
            return True

    def return_possible_beatings(self, pawn_coordinates):
        directions = self.beating_directions
        self.possible_beating = []
        self.corresponding_beaten = []
        enemy_pawns = pawn_coordinates[{'w':'b', 'b':'w'}[self.color]]
        ally_pawns = pawn_coordinates[self.color]
        all_pawns = pawn_coordinates['w'] + pawn_coordinates['b']

        if self.king:
            self.return_possible_king_beatings(all_pawns, ally_pawns, enemy_pawns)
        else:  
            for direction in directions:
                candidate_beating = [x + y for x, y in zip(self.position, direction)]
                if all([candidate_beating in enemy_pawns,
                        candidate_beating not in ally_pawns]):
                    candidate_free = [x + y for x, y in zip(candidate_beating, direction)]
                    if  all([candidate_free not in all_pawns,
                            self.check_if_within_board(candidate_free)]):
                        self.possible_beating.append(candidate_free)
                        self.corresponding_beaten.append(candidate_beating)
        print(self.position, "possible beating move:", self.possible_beating,
              "corresponding beaten:", self.corresponding_beaten)
               
    def return_possible_king_beatings(self, all_pawns, ally_pawns, enemy_pawns):
        self.possible_beating = []
        self.corresponding_beaten = []
        
        beatings=[]
        corresponding_beaten=[]

        for step in self.beating_directions:
            free_fields = []
            multi = 1
            while True:
                outer_step = [i * multi for i in step]
                candidate_beaten = [x + y for x, y in zip(self.position, outer_step)]
                if any([not self.check_if_within_board(candidate_beaten),
                        candidate_beaten in ally_pawns]):
                    break
                if candidate_beaten in enemy_pawns:
                        multiplier=1
                        while True:
                            inner_step=[i * multiplier for i in step]
                            candidate_free=[x + y for x, y in zip(candidate_beaten, inner_step)]
                            if any([not self.check_if_within_board(candidate_free),
                                    candidate_free in all_pawns]):
                                            break
                            free_fields.append(candidate_free)
                            multiplier += 1
                        if len(free_fields) > 0:
                            self.possible_beating.append(free_fields)
                            self.corresponding_beaten.append(candidate_beaten)
                multi += 1


