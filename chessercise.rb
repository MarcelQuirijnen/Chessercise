require 'optparse'
#require_relative 'optparse_required_switches'  # Not a stdlib feature, danged!

###################
# helper structures
###################
# map chess column notation to matrix index
$chess_map_from_alpha_to_index = {"a" => 0, "b" => 1, "c" => 2, "d" => 3, "e" => 4, "f" => 5, "g" => 6, "h" => 7}
# use $chess_map_from_alpha_to_index.key(some-index-value + 1) to get the alpha value

###################
# Helper functions
###################
def boardToMatrix(pos)
    # Convert typical chess notation (a1-a8 -- h1-h8), to matrix notation [0-7]x[0-7]
    
    # strip whitespace and convert to lowercase
    col, row = pos.strip.downcase.split('')
    # start counting from 0
    row = row.to_i - 1
    # convert a-h to 0-7
    # puts col.kind_of?(String)
    column = $chess_map_from_alpha_to_index[col]
    return row, column
end

def matrixToBoardList(matrix)
    # convert given matrix coords into a list of board coords
    boardList = []
    unless matrix.empty?
        (0..matrix.length-1).step(2).each do |index|
            boardList.push($chess_map_from_alpha_to_index.key(matrix[index+1]) + (matrix[index] + 1).to_s)
        end
    end
    return boardList
end

def isStartRowPosition(pos)
    # Is the given position located on the pawns startrow?

    # Assumptions : Row 2 is the start row for our set of pawns
    digits = 0..7
    startRow = ''
    digits.sort.each do |digit|
        startRow << $chess_map_from_alpha_to_index.key(digit)
        startRow << '2 '
    end
    return startRow.include?(pos)
end

def offBoardFilter(moves, min, max)
    (0..moves.length-1).step(2).each do |index|
        if moves[index] < min or moves[index] > max
            moves[index] = moves[index+1] = -1
        elsif moves[index+1] < min or moves[index+1] > max
            moves[index] = moves[index+1] = -1
        end
    end
    moves.delete_if { |a| a < 0 }
end

def kingMoves(i, j)
    # list up all the King moves
    moves = []
    moves.push(i, j-1)
    moves.push(i, j+1)
    (i+1..i+1).each do |row|
        moves.push(row, j-1)
        moves.push(row, j+1)
        moves.push(row, j)
    end
    (i-1).downto(i-1) do |row|
        moves.push(row, j-1)
        moves.push(row, j+1)
        moves.push(row, j)
    end
    return moves
end

def bishopMoves(i, j)
    # list up all the Bishop moves
    moves = []
    # get moves above current/given bishop position
    col1 = col2 = j
    (i..6).each do |row|
        moves.push(row+1, col1-1)
        moves.push(row+1, col2+1)
        col1 -= 1
        col2 += 1
    end
    # get moves below current/given bishop position
    col1 = col2 = j
    (i).downto(1) do |row|
        moves.push(row-1, col1-1)
        moves.push(row-1, col2+1)
        col1 -= 1
        col2 += 1
    end
    return moves
end

def rookMoves(row, column)
    # list up all the Rook moves
    moves = []
    # Compute the horizontal moves
    (0..7).each do |j|
        unless j == column
            moves.push(row, j)
        end
    end
    # Compute the vertical moves
    (0..7).each do |j|
        unless j == row
            moves.push(j, column)
        end
    end
    return moves
end

def knightMoves(i, j)
    # list up all the Knight moves
    moves = []
    
    moves.push(i + 1, j + 2)
    moves.push(i + 1, j - 2)
    moves.push(i + 2, j + 1)
    moves.push(i + 2, j - 1)
    moves.push(i - 1, j + 2)
    moves.push(i - 1, j - 2)
    moves.push(i - 2, j + 1)
    moves.push(i - 2, j - 1)
    return moves
end


def getPawnMoves(pos)
    # return all possible moves of a pawn from a given position on the chessboard
    # if pawn is in start position (row 2) it can move 2 places
    
    i, j = boardToMatrix(pos)
    potentialMoves = []

    # if pawn is in start position, it can move 2 places up (and only up), otherwise move only 1 place
    if isStartRowPosition(pos)
        potentialMoves.push(i+2, j)
    else
        potentialMoves.push(i+1, j)
    end

    # Filter out the values that are off the board (negative values or values > 7)
    offBoardFilter(potentialMoves, 0, 7)
    
    # Map the leftover values to board coordinates
    boardList = matrixToBoardList(potentialMoves)

    boardList.join('')
end

def getKnightMoves(pos)
    i, j = boardToMatrix(pos)

    # positions on the board the knight can move to, relative to his current position
    potentialMoves = knightMoves(i, j)

    # Filter out the values that are off the board (negative values  or values > 7)
    offBoardFilter(potentialMoves, 0, 7)

    # Map the leftover values to board coordinates
    boardList = matrixToBoardList(potentialMoves)
    
    return boardList * ','
end

def getKingMoves(pos)
    i, j = boardToMatrix(pos)

    potentialMoves = kingMoves(i, j)

    # Map the leftover values to board coordinates
    boardList = matrixToBoardList(potentialMoves)
    
    return boardList * ','
end

def getBishopMoves(pos)
    i, j = boardToMatrix(pos)

    potentialMoves = bishopMoves(i, j)

    # Filter out the values that are off the board (negative values  or values > 7)
    offBoardFilter(potentialMoves, 0, 7)

    # Map the leftover values to board coordinates
    boardList = matrixToBoardList(potentialMoves)
    
    return boardList * ','
end

def getQueenMoves(pos)
    # return all possible moves of the queen from a given position on the chessboard
    i, j = boardToMatrix(pos)

    # Queen moves consist of sum of Rook moves and Bishop moves, hence lifting out those parts of the code
    potentialMoves = rookMoves(i, j)
    potentialMoves += bishopMoves(i, j)

    # Filter out the values that are off the board (negative values  or values > 7)
    offBoardFilter(potentialMoves, 0, 7)

    # Map the leftover values to board coordinates
    boardList = matrixToBoardList(potentialMoves)
    
    return boardList * ','
end

def getRookMoves(pos)
    i, j = boardToMatrix(pos)
    row, column = i, j

    potentialMoves = rookMoves(row, column)

    # Map the values to board coordinates
    boardList = matrixToBoardList(potentialMoves)
    
    return boardList * ','
end


# We'd like to use this code as a program or a module
# not sure if this is very 'rubyist' like
if __FILE__ == $0
    # get cmdline options
    options = {}
    OptionParser.new do |opts|
      opts.banner = "Usage: chessercise.rb -p ChessPiece -l d4"
      opts.on('-p ARG', '--piece ARG', "Chess piece: Pawn, Rook, Bishop, King, Knight or Queen") do |v|
        options[:piece] = v
      end
      opts.on('-l ARG', '--position ARG', "Position on the board using chess notation: d4") do |v|
        options[:position] = v
      end
      opts.on('-h', '--help', 'Display this help') do 
        puts opts
        exit
      end
    end.parse!

    # make sure we have all required input
    raise OptionParser::MissingArgument.new('Board piece not specified.') if options[:piece].nil?
    raise OptionParser::MissingArgument.new('Location on the board not specified.') if options[:position].nil?

    # puts options
    # {:piece=>"rook", :position=>"d4"}

    case options[:piece]
    when 'pawn'
        p getPawnMoves(options[:position])
    when 'bishop'
        p getBishopMoves(options[:position])
    when 'rook'
        p getRookMoves(options[:position])
    when 'knight'
        p getKnightMoves(options[:position])
    when 'king'
        p getKingMoves(options[:position])
    when 'queen'
        p getQueenMoves(options[:position])
    else
        puts "Unknown chess piece."
    end
end