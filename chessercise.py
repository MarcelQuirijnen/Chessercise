import argparse
import types

###################
# helper structures
###################
# map chess column notation to matrix index
chess_map_from_alpha_to_index = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
# map matrix indices to chess columns
chess_map_from_index_to_alpha = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

###################
# Helper functions
###################
def boardToMatrix(pos):
    """ Convert typical chess notation (a1-a8 -- h1-h8), to matrix notation [0-7]x[0-7] """
    # strip whitespace and convert to lowercase
    column, row = list(pos.strip().lower())
    # start counting from 0
    row = int(row) - 1
    # convert a-h to 0-7
    column = chess_map_from_alpha_to_index[column]
    return row, column


def isStartRowPosition(pos):
    """ Is the given position located on the pawns startrow? """
    # Assumptions : Row 2 is the start row for our set of pawns
    startRow = ["".join([chess_map_from_index_to_alpha[i], '2']) for i in range(8)]
    return pos in startRow


def rookMoves(moves, row, column):
    """ list up all the Rook moves """
    # example : --position d4 -> matrix coords: 3,3
    # Compute the horizontal moves
    for j in range(8):
        if j != column:
            moves.append((row, j))
    # [(1, 0), (1, 1), (1, 2), (1, 4), (1, 5), (1, 6), (1, 7)]

    # Compute the vertical moves
    for i in range(8):
        if i != row:
            moves.append((i, column))
    # [ <the above> + (0, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)]


def kingMoves(moves, i, j):
    """ list up all the King moves """
    # example : --position d4 -> matrix coords: 3,3
    moves.append((i, j-1))
    moves.append((i, j+1))
    # (3, 2), (3, 4)

    for row in range(i+1, i+2):
        moves.append((row, j-1))
        moves.append((row, j+1))
        moves.append((row, j))
    # the above + (4, 2), (4, 4), (4, 3)

    for row in range(i-1, i-2, -1):
        moves.append((row, j-1))
        moves.append((row, j+1))
        moves.append((row, j))
    # the above + (2, 2), (2, 4), (2, 3)


def bishopMoves(moves, i, j):
    """ list up all the Bishop moves """
    # example : --position d4 -> matrix coords: 3,3
    # get moves above current/given bishop position
    col1 = col2 = j
    for row in range(i, 7):
        moves.append((row+1, col1-1))
        moves.append((row+1, col2+1))
        col1 -= 1
        col2 += 1
    # (4, 2), (4, 4), (5, 1), (5, 5), (6, 0), (6, 6), (7, -1), (7, 7)

    # get moves below current/given bishop position
    col1 = col2 = j
    for row in range(i, 0, -1):
        moves.append((row-1, col1-1))
        moves.append((row-1, col2+1))
        col1 -= 1
        col2 += 1
    # the above + (2, 2), (2, 4), (1, 1), (1, 5), (0, 0), (0, 6)


def knightMoves(moves, i, j):
    """ list up all the Knight moves """
    moves.append([i + 2, j - 1])
    moves.append([i + 1, j - 2])
    moves.append([i + 2, j + 1])
    moves.append([i + 1, j + 2])
    moves.append([i - 1, j + 2])
    moves.append([i - 2, j + 1])
    moves.append([i - 2, j - 1])
    moves.append([i - 1, j - 2])


def getKnightMoves(pos):
    """ return all possible moves of a knight from a given position on the chessboard """
    i, j = boardToMatrix(pos)
    potentialMoves = []

    # example : --position d4 -> matrix coords: 3,3
    # positions on the board to knight can move to, relative to his current position
    knightMoves(potentialMoves, i, j)
    # [[2, 1], [3, 2], [3, 4], [2, 5], [0, 5], [-1, 4], [-1, 2], [0, 1]]

    # Filter out the values that are off the board (negative values  or values > 7)
    temp = [i for i in potentialMoves if i[0] >= 0 and i[1] >= 0 and i[0] <= 7 and i[1] <= 7]
    # [[2, 1], [3, 2], [3, 4], [2, 5], [0, 5], [0, 1]]

    # Map the leftover values to board coordinates
    allMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    # ['c6', 'b5', 'e6', 'f5', 'f3', 'e2', 'c2', 'b3']

    return '"'+','.join(allMoves)+'"'


def getRookMoves(pos):
    """ return all possible moves of the rook from a given position on the chessboard """

    i, j = boardToMatrix(pos)
    row, column = i, j
    potentialMoves = []

    rookMoves(potentialMoves, row, column)

    # Map the values to board coordinates
    allMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in potentialMoves]
    # ['a4', 'b4', 'c4', 'e4', 'f4', 'g4', 'h4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8']

    return '"'+','.join(allMoves)+'"'


def getQueenMoves(pos):
    """ return all possible moves of the queen from a given position on the chessboard """
    i, j = boardToMatrix(pos)
    potentialMoves = []

    # Queen moves consist of sum of Rook moves and Bishop moves, hence lifting out those parts of the code
    rookMoves(potentialMoves, i, j)
    bishopMoves(potentialMoves, i, j)

    # Filter out the values that are off the board (negative values  or values > 7)
    temp = [i for i in potentialMoves if i[0] >= 0 and i[1] >= 0 and i[0] <= 7 and i[1] <= 7]

    # Map the leftover values to board coordinates
    allMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    # ['a4', 'b4', 'c4', 'e4', 'f4', 'g4', 'h4', 'd1', 'd2', 'd3', 'd5', 'd6', 'd7', 'd8', 'c5', 'e5', 'b6', 'f6', 'a7', 'g7', 'h8', 'c3', 'e3', 'b2', 'f2', 'a1', 'g1']

    return '"'+','.join(allMoves)+'"'


def getKingMoves(pos):
    """ return all possible moves of a king from a given position on the chessboard """
    i, j = boardToMatrix(pos)
    potentialMoves = []

    kingMoves(potentialMoves, i, j)

    # Map the leftover values to board coordinates
    allMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in potentialMoves]
    # ['c4', 'e4', 'c5', 'e5', 'd5', 'c3', 'e3', 'd3']

    return '"'+','.join(allMoves)+'"'


def getBishopMoves(pos):
    """ return all possible moves of a bishop from a given position on the chessboard """
    i, j = boardToMatrix(pos)
    potentialMoves = []

    bishopMoves(potentialMoves, i, j)

    # Filter out the values that are off the board (negative values  or values > 7)
    temp = [i for i in potentialMoves if i[0] >= 0 and i[1] >= 0 and i[0] <= 7 and i[1] <= 7]

    # Map the leftover values to board coordinates
    allMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    # ['c5', 'e5', 'b6', 'f6', 'a7', 'g7', 'h8', 'c3', 'e3', 'b2', 'f2', 'a1', 'g1']

    return '"'+','.join(allMoves)+'"'


def getPawnMoves(pos):
    """
    return all possible moves of a pawn from a given position on the chessboard
    if pawn is in start position (row 2) it can move 2 places
    """
    i, j = boardToMatrix(pos)
    potentialMoves = []

    # example : --position d4 -> matrix coords: 3,3
    # if pawn is in start position, it can move 2 places up (and only up), otherwise move only 1 place
    if isStartRowPosition(pos):
        potentialMoves.append((i+2, j))
    else:
        potentialMoves.append((i+1, j))

    # Filter out the values that are off the board (negative values or values > 7)
    temp = [i for i in potentialMoves if i[0] >= 0 and i[1] >= 0 and i[0] <= 7 and i[1] <= 7]

    # Map the leftover values to board coordinates
    allMoves = ["".join([chess_map_from_index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    # ['d5']

    return '"'+','.join(allMoves)+'"'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--piece", help="chess piece name: ie. ROOK, KNIGHT, QUEEN, etc")
    parser.add_argument("-l", "--position", help="chess notation string: ie. e4, d6, etc")
    args = parser.parse_args()

    piece = args.piece.strip().lower()
    position = args.position.strip().lower()

    chessPieces = {
        'pawn': getPawnMoves,
        'bishop': getBishopMoves,
        'rook': getRookMoves,
        'knight': getKnightMoves,
        'queen': getQueenMoves,
        'king': getKingMoves
    }

    func = chessPieces.get(piece, "Unknown chess piece.")
    if isinstance(func, types.FunctionType):
        print(func(position))
    else:
        print(func)
