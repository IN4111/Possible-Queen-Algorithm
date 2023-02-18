import numpy as np
class PossibleQueen():
    def __init__(self,n):
        self.n=n
        self.current_chess_board=np.zeros([n,n],dtype="int64")
        self.logic_chess_board=np.zeros([n,n],dtype="int64")
    def dialu(self,x,y):
        xc=x
        yc=y
        xa=[]
        ya=[]
        while xc!=0:
            xc=xc-1
            xa.append(xc)
        while yc!=0:
            yc=yc-1
            ya.append(yc)
        result=[]
        max_result=min(len(xa),len(ya))
        for i in range(0,max_result):
            result.append([xa[i],ya[i]])
        return result
    def diaru(self,x,y):
        xc=x
        yc=y
        xa=[]
        ya=[]
        while xc!=0:
            xc=xc-1
            xa.append(xc)
        while yc!=self.n-1:
            yc=yc+1
            ya.append(yc)
        result=[]
        max_result=min(len(xa),len(ya))
        for i in range(0,max_result):
            result.append([xa[i],ya[i]])
        return result
    def diarl(self,x,y):
        xc=x
        yc=y
        xa=[]
        ya=[]
        while xc!=self.n-1:
            xc=xc+1
            xa.append(xc)
        while yc!=self.n-1:
            yc=yc+1
            ya.append(yc)
        result=[]
        max_result=min(len(xa),len(ya))
        for i in range(0,max_result):
            result.append([xa[i],ya[i]])
        return result
    def diall(self,x,y):
        xc=x
        yc=y
        xa=[]
        ya=[]
        while xc!=self.n-1:
            xc=xc+1
            xa.append(xc)
        while yc!=0:
            yc=yc-1
            ya.append(yc)
        result=[]
        max_result=min(len(xa),len(ya))
        for i in range(0,max_result):
            result.append([xa[i],ya[i]])
        return result
    def linleft(self,x,y):
        yc=y
        xa=[x for xe in range(0,y)]
        ya=[]
        result=[]
        while yc!=0:
            yc=yc-1
            ya.append(yc)
        for i in range(0,len(xa)):
            result.append([xa[i],ya[i]])
        return(result)
    def linupper(self,x,y):
        xc=x
        ya=[y for xe in range(0,x)]
        xa=[]
        result=[]
        while xc!=0:
            xc=xc-1
            xa.append(xc)
        for i in range(0,len(xa)):
            result.append([xa[i],ya[i]])
        return(result)
    def linright(self,x,y):
        yc=y
        xa=[x for ye in range(y+1,self.n)]
        ya=[]
        result=[]
        while yc!=7:
            yc=yc+1
            ya.append(yc)
        for i in range(0,len(xa)):
            result.append([xa[i],ya[i]])
        return(result)
    def linlower(self,x,y):
        xc=x
        ya=[y for xe in range(x+1,self.n)]
        xa=[]
        result=[]
        while xc!=7:
            xc=xc+1
            xa.append(xc)
        for i in range(0,len(ya)):
            result.append([xa[i],ya[i]])
        return(result)
    def fill_lu(self,x,y):
        for i,j in self.dialu(x,y):
            self.logic_chess_board[i][j]=1
    def fill_ru(self,x,y):
        for i,j in self.diaru(x,y):
            self.logic_chess_board[i][j]=1
    def fill_rl(self,x,y):
        for i,j in self.diarl(x,y):
            self.logic_chess_board[i][j]=1
    def fill_ll(self,x,y):
        for i,j in self.diall(x,y):
            self.logic_chess_board[i][j]=1
    def fill_left(self,x,y):
        for i,j in self.linleft(x,y):
            self.logic_chess_board[i][j]=1
    def fill_upper(self,x,y):
        for i,j in self.linupper(x,y):
            self.logic_chess_board[i][j]=1
    def fill_right(self,x,y):
        for i,j in self.linright(x,y):
            self.logic_chess_board[i][j]=1
    def fill_lower(self,x,y):
        for i,j in self.linlower(x,y):
            self.logic_chess_board[i][j]=1
    def fill_center(self,x,y):
        self.logic_chess_board[x][y]=1
    def isPossible(self,x,y):
            if self.logic_chess_board[x][y]==1:
                    return False
            return True
    def return_logic_chess_board(self,):
        return self.logic_chess_board
    def return_current_chess_board(self,):
        return self.current_chess_board
    def return_queen(self,):
        count=0
        for i in self.current_chess_board:
            for j in i:
                if(j==1):
                    count=count+1
        return count
    def fill(self,xx,yy):
        self.fill_center(xx,yy)
        self.fill_left(xx,yy)
        self.fill_upper(xx,yy)
        self.fill_right(xx,yy)
        self.fill_lower(xx,yy)
        self.fill_lu(xx,yy)
        self.fill_ru(xx,yy)
        self.fill_rl(xx,yy)
        self.fill_ll(xx,yy)
        self.place_queen_current_chess_board(xx,yy)
    def place_queen_current_chess_board(self,x,y):
        self.current_chess_board[x][y]=1
