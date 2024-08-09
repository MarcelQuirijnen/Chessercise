require_relative 'chessercise.rb'
require 'test/unit'

class TestChessMove < Test::Unit::TestCase
    def test_getPawnMoves
        assert_equal getPawnMoves('d4'), "d5"
    end

    def test_getKnightMoves
        assert_equal getKnightMoves('d4'), "f5,b5,e6,c6,f3,b3,e2,c2"
    end

    def test_getBishopMoves
        assert_equal getBishopMoves('d4'), "c5,e5,b6,f6,a7,g7,h8,c3,e3,b2,f2,a1,g1"
    end

    def test_getRookMoves
        assert_equal getRookMoves('d4'), "a4,b4,c4,e4,f4,g4,h4,d1,d2,d3,d5,d6,d7,d8"
    end

    def test_getKingMoves
        assert_equal getKingMoves('d4'), "c4,e4,c5,e5,d5,c3,e3,d3"
    end

    def test_getQueenMoves
        assert_equal getQueenMoves('d4'), "a4,b4,c4,e4,f4,g4,h4,d1,d2,d3,d5,d6,d7,d8,c5,e5,b6,f6,a7,g7,h8,c3,e3,b2,f2,a1,g1"   
    end
end