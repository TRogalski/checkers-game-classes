import unittest
from pawn import Pawn
from board import Board


class TestPawn(unittest.TestCase):

    """test of a return_possible_regular_movements on a starting positions"""

    def setUp(self):
        self.all_pawn_positions=[[5,1],[5,3],[5,5],[5,7],[6,0],[6,2],
                                 [6,4],[6,6],[7,1],[7,3],[7,5],[7,7],
                                 [0,0],[0,2],[0,4],[0,6],[1,1],[1,3],
                                 [1,5],[1,7],[2,0],[2,2],[2,4],[2,6]]

    def test_return_possible_regular_movements_1(self):
        pawn=Pawn('w',[5,1])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[[4,0],[4,2]])

    def test_return_possible_regular_movements_2(self):
        pawn=Pawn('w',[5,3])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[[4,2],[4,4]])

    def test_return_possible_regular_movements_3(self):
        pawn=Pawn('w',[5,5])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[[4,4],[4,6]])

    def test_return_possible_regular_movements_4(self):
        pawn=Pawn('w',[5,7])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[[4,6]])

    def test_return_possible_regular_movements_5(self):
        pawn=Pawn('w',[6,0])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])
       
    def test_return_possible_regular_movements_6(self):
        pawn=Pawn('w',[6,2])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_7(self):
        pawn=Pawn('w',[6,4])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_8(self):
        pawn=Pawn('w',[6,6])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_9(self):
        pawn=Pawn('w',[7,1])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_10(self):
        pawn=Pawn('w',[7,3])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])
       
    def test_return_possible_regular_movements_11(self):
        pawn=Pawn('w',[7,5])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_12(self):
        pawn=Pawn('w',[7,7])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_13(self):
        pawn=Pawn('b',[0,0])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_14(self):
        pawn=Pawn('b',[0,2])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_15(self):
        pawn=Pawn('b',[0,4])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])
       
    def test_return_possible_regular_movements_16(self):
        pawn=Pawn('b',[0,6])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_17(self):
        pawn=Pawn('b',[1,1])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_18(self):
        pawn=Pawn('b',[1,3])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_19(self):
        pawn=Pawn('b',[1,5])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])

    def test_return_possible_regular_movements_20(self):
        pawn=Pawn('b',[1,7])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[])
       
    def test_return_possible_regular_movements_21(self):
        pawn=Pawn('b',[2,0])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[[3,1]])

    def test_return_possible_regular_movements_22(self):
        pawn=Pawn('b',[2,2])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[[3,1],[3,3]])

    def test_return_possible_regular_movements_23(self):
        pawn=Pawn('b',[2,4])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[[3,3],[3,5]])

    def test_return_possible_regular_movements_24(self):
        pawn=Pawn('b',[2,6])
        pawn.return_possible_regular_movements(self.all_pawn_positions)
        self.assertEqual(pawn.possible_movement,[[3,5],[3,7]])

    def test_return_possible_beatings_1(self):

        """All pawns regular - should be one possible beating"""

        board=Board()
        board.pawn_coordinates={'w': [[4, 0], [5, 3], [5, 5], [5, 7], [6, 0], [5, 1],
                                      [6, 4], [6, 6], [7, 1], [7, 3], [7, 5], [7, 7]],
                                'b': [[0, 0], [0, 2], [0, 4], [0, 6], [1, 1], [1, 3],
                                      [1, 5], [1, 7], [3, 1], [3, 3], [2, 4], [2, 6]]}
        board.now_moves='w'
        board.create_pawns()
        board.update_board()
        board.update_pawn_movements()
        board.mark_pawns_that_can_beat()
        self.assertEqual(board.pawns_that_can_beat,[[4,0]])

    def test_return_possible_beatings_2(self):

        """All pawns regular - should be one possible beating"""

        board=Board()
        board.pawn_coordinates={'w': [[4, 0], [4, 2], [5, 5], [5, 7], [6, 0], [6, 2],
                                      [6, 4], [6, 6], [7, 1], [7, 3], [7, 5], [7, 7]],
                                'b': [[0, 0], [0, 2], [0, 4], [0, 6], [1, 1], [1, 3],
                                      [1, 5], [1, 7], [3, 1], [2, 2], [2, 4], [2, 6]]}
        board.now_moves='b'
        board.create_pawns()
        board.update_board()
        board.update_pawn_movements()
        board.mark_pawns_that_can_beat()
        self.assertEqual(board.pawns_that_can_beat,[[3,1]])


    def test_return_possible_beatings_3(self):

        """All pawns regular - should get two possible beatings"""
        
        board=Board()
        board.pawn_coordinates={'w': [[4, 0], [4, 2], [5, 5], [4, 6], [6, 0], [6, 2],
                                      [6, 4], [6, 6], [7, 1], [7, 3], [7, 5], [7, 7]],
                                'b': [[0, 0], [0, 2], [0, 4], [0, 6], [1, 1], [1, 3],
                                      [1, 5], [1, 7], [3, 1], [2, 2], [3, 3], [2, 6]]}
        board.now_moves='b'
        board.create_pawns()
        board.update_board()
        board.update_pawn_movements()
        board.mark_pawns_that_can_beat()
        self.assertEqual(board.pawns_that_can_beat,[[3, 1], [3, 3]])

    def test_return_possible_beatings_4(self):

        """All pawns regular - should get two possible beatings"""

        board=Board()
        board.pawn_coordinates={'w': [[4, 0], [4, 4], [5, 5], [4, 6],
                                      [6, 2], [6, 4], [5, 7], [7, 1],
                                      [7, 3], [7, 5], [7, 7]],
                                'b': [[0, 0], [0, 2], [0, 4], [0, 6],
                                      [1, 1], [4, 2], [1, 5], [1, 7],
                                      [3, 1], [3, 3], [2, 6]]}
        board.now_moves='w'
        board.create_pawns()
        board.update_board()
        board.update_pawn_movements()
        board.mark_pawns_that_can_beat()
        self.assertEqual(board.pawns_that_can_beat,[[4, 0], [4, 4]])
         
if __name__=='__main__':
    unittest.main()
