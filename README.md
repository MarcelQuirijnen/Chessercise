# Chessercise

This exercise returns a list of all the potential board positions a given chess piece could advance to, with one move, from the given position, with the assumption there are no other pieces on the board.

### Prerequisites

Python 2.7 or Python 3.x
Ruby 2.3
No special libraries.

### Download & install

```
git clone git@bitbucket.org:sugarcreek/chessercise.git
```
### Python Usage

```
usage: chessercise.py [-h] [-p PIECE] [-l POSITION]

optional arguments:
  -h, --help 				        	show this help message and exit
  -p PIECE, --piece PIECE				chess piece name: ie. ROOK, KNIGHT, QUEEN, etc
  -l POSITION, --position POSITION		chess notation string: ie. e4, d6, etc
```
Examples:
```
python chessercise.py -p bishop -l e3
"d4,f4,c5,g5,b6,h6,a7,d2,f2,c1,g1"
```
```
python chessercise.py -p KING -l g5
"f5,h5,f6,h6,g6,f4,h4,g4"
```
### Ruby Usage

```
usage: chessercise.rb [-h] [-p PIECE] [-l POSITION]

optional arguments:
  -h, --help 				        	show this help message and exit
  -p PIECE, --piece PIECE				chess piece name: ie. ROOK, KNIGHT, QUEEN, etc
  -l POSITION, --position POSITION		chess notation string: ie. e4, d6, etc
```
Examples:
```
ruby chessercise.rb -p bishop -l e3
"d4,f4,c5,g5,b6,h6,a7,d2,f2,c1,g1"
```
```
ruby chessercise.rb -p KING -l g5
"f5,h5,f6,h6,g6,f4,h4,g4"
```

## Running the tests - python

```
python chessercise_test.py -v

test_getBishopMoves (__main__.ChessMoveTest) ... ok
test_getKingMoves (__main__.ChessMoveTest) ... ok
test_getKnightMoves (__main__.ChessMoveTest) ... ok
test_getPawnMoves (__main__.ChessMoveTest) ... ok
test_getQueenMoves (__main__.ChessMoveTest) ... ok
test_getRookMoves (__main__.ChessMoveTest) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```
## Running the tests - ruby

```
ruby tc_chessercise.rb

Loaded suite tc_chessercise
Started
......

Finished in 0.001442416 seconds.
---------------------------------------------------------------------------------------------------------------------------------

6 tests, 6 assertions, 0 failures, 0 errors, 0 pendings, 0 omissions, 0 notifications
100% passed
---------------------------------------------------------------------------------------------------------------------------------
4159.69 tests/s, 4159.69 assertions/s
```
or just 1 test
```
ruby tc_chessercise.rb --name test_getQueenMoves

Loaded suite tc_chessercise
Started
.

Finished in 0.000603301 seconds.
---------------------------------------------------------------------------------------------------------------------------------

1 tests, 1 assertions, 0 failures, 0 errors, 0 pendings, 0 omissions, 0 notifications
100% passed
---------------------------------------------------------------------------------------------------------------------------------
1657.55 tests/s, 1657.55 assertions/s
```


## Versioning

Version 1.0


## Authors

* Marcel Quirijnen


## License

MIT
