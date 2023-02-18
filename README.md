# possibleQueen
It provides the knowledge/logics how or how many "Queen" can be placed on a chess board so that no two queens cross each other.
hi,im IN,a junior computer-mathematics developer.
# Import Module:
Import module "possiblequeen"
```
from possiblequeen import PossibleQueen as PQ
```
# Create chess board:
Create a chess board with the following way by passing "n" number of columns in the chess board
```
pq=PQ(8)#created chess board of 8 columns
```
# Returning diagonal indices:
# 1)Return left upper diagonal of x,y
```
pq.dialu(4,4)#returns index position of left upper diagonals of 4,4
```
# 2)Return right upper diagonal of x,y
```
pq.diaru(4,4)#returns index position of right upper diagonals of 4,4
```
# 3)Return right lower diagonal of x,y
```
pq.diarl(4,4)#returns index position of right lower diagonals of 4,4
```
# 4)Return left lower diagonal of x,y
```
pq.diall(4,4)#returns index position of left lower diagonals of 4,4
```
# Filling diagonal indices:
# 1)Fill left upper diagonal of x,y
```
pq.fill_lu(4,4)#fills index position of left upper diagonals of 4,4 with 1 on logic_chess_board array
```
# 2)Fill right upper diagonal of x,y
```
pq.fill_ru(4,4)#fills index position of right upper diagonals of 4,4 with 1 on logic_chess_board array
```
# 3)Fill right lower diagonal of x,y
```
pq.fill_rl(4,4)#fills index position of right lower diagonals of 4,4 with 1 on logic_chess_board array
```
# 4)Fill left lower diagonal of x,y
```
pq.fill_ll(4,4)#fills index position of left lower diagonals of 4,4 with 1 on logic_chess_board array
```
