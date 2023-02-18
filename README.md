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
# Returning indices:
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
# 5)Return linear left indices of x,y
```
pq.linleft(4,4)#returns index position of left indices of 4,4
```
# 6)Return linear upper indices of x,y
```
pq.linupper(4,4)#returns index position of upper indices of 4,4
```
# 7)Return linear right indices of x,y
```
pq.linright(4,4)#returns index position of right indices of 4,4
```
# 8)Return linear lower indices of x,y
```
pq.linlower(4,4)#returns index position of lower indices of 4,4
```
# Filling indices:
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
# 5)Fill linear left indices of x,y
```
pq.fill_left(4,4)#fills index position of linear left indices of 4,4 with 1 on logic_chess_board array
```
# 6)Fill linear upper indices of x,y
```
pq.fill_upper(4,4)#fills index position of linear upper indices of 4,4 with 1 on logic_chess_board array
```
# 7)Fill linear right indices of x,y
```
pq.fill_right(4,4)#fills index position of linear right indices of 4,4 with 1 on logic_chess_board array
```
# 8)Fill linear lower indices of x,y
```
pq.fill_lower(4,4)#fills index position of linear lower indices of 4,4 with 1 on logic_chess_board array
```
# 9)Fill center index of x,y
```
pq.fill_center(4,4)#fills index position of 4,4 with 1 on logic_chess_board array
```
# 10)Fill all indices of x,y on diagonal and linear indices
```
pq.fill(4,4)#fills all diagonal and linear indices of 4,4 with 1 on logic_chess_board array and also fills 1 in current_chess_board array
```
# OTHER USEFUL FUNCTIONS
# 1)Returning logic chess board
```
pq.return_logic_chess_board()#returns logic of the chess board(logic_chess_board array)
```
# 2)Returning current chess board
```
pq.return_current_chess_board()#returns current chessboard of the chess board with maker 1(current_chess_board array)
```
# 3)Returning queen count on current_chess_board
```
pq.return_queen()#returns number of queens on current_chess_board
```
# 4)isPossible():
```
pq.isPossible(4,4)#returns true/false depending upon whether qeen can be placed on (4,4)
```
