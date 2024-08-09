import unittest

from chessercise import getPawnMoves, getBishopMoves, getKingMoves, getQueenMoves, getRookMoves, getKnightMoves


class ChessMoveTest(unittest.TestCase):
    # @unittest.skip("Skipping test test_getPawnMoves")
    def test_getPawnMoves(self):
        self.assertEqual(getPawnMoves('d4'), '"d5"')

    # @unittest.skip("Skipping test test_getKnightMoves")
    def test_getKnightMoves(self):
        self.assertEqual(getKnightMoves('d4'), '"c6,b5,e6,f5,f3,e2,c2,b3"')

    # @unittest.skip("Skipping test test_getBishopMoves")
    def test_getBishopMoves(self):
        self.assertEqual(getBishopMoves('d4'), '"c5,e5,b6,f6,a7,g7,h8,c3,e3,b2,f2,a1,g1"')

    # @unittest.skip("Skipping test test_getRookMoves")
    def test_getRookMoves(self):
        self.assertEqual(getRookMoves('d4'), '"a4,b4,c4,e4,f4,g4,h4,d1,d2,d3,d5,d6,d7,d8"')

    # @unittest.skip("Skipping test test_getKingMoves")
    def test_getKingMoves(self):
        self.assertEqual(getKingMoves('d4'), '"c4,e4,c5,e5,d5,c3,e3,d3"')

    # @unittest.skip("Skipping test test_getQueenMoves")
    def test_getQueenMoves(self):
        self.assertEqual(getQueenMoves('d4'), '"a4,b4,c4,e4,f4,g4,h4,d1,d2,d3,d5,d6,d7,d8,c5,e5,b6,f6,a7,g7,h8,c3,e3,b2,f2,a1,g1"')


if __name__ == '__main__':
    unittest.main()
