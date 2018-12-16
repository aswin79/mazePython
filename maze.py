import numpy as np
from time import process_time

class gridSolve:
    
    def __init__(self):
        self.resetGrid()
        
    # to reset across solving methods       
    def resetGrid(self):        
        self.grid = [[0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 1],
            [0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 2]]
        nR=len(self.grid)
        nC=len(self.grid[0])
        self.visitedNP= np.zeros((nR, nC))
        self.gridNP= np.asarray(self.grid)
        self.startPtNP=np.array([(0), (0)])
        self.steps=0
        x=self.startPtNP[0]
        y=self.startPtNP[1]
        self.visitedNP[x][y]=1
    
    # next state not valid if it is outside the grid, already visited or is marked as blocked in maze
    def isValid(self,xi,yi):    
        x=self.startPtNP[0]
        y=self.startPtNP[1]
        (xL,yL)=self.gridNP.shape 
        xN=x+xi    
        yN=y+yi
        if ((xi==yi) or ((xi!=0) and (yi!=0)) or (xN<0) or (xN>=xL) or (yN<0) or (yN>=yL) or (self.visitedNP[xN][yN]==1) or (self.gridNP[xN][yN]==1)):
            return 0
        else:
            return 1
                 
    # simple recursively self calling maze walker. can go in 4 dirs, right, down, up, left        
    def iterateOverSolve(self):
        x=self.startPtNP[0]
        y=self.startPtNP[1]
        start=self.startPtNP
        (xL,yL)=self.gridNP.shape 
        if (self.grid[x][y] ==2):
            print("Done! with steps:",self.steps)
            return 1
        else:
            self.steps = self.steps+ 1
        for xi in range (-1,2) :
            for yi in range (-1,2) :
                xN=x+xi    
                yN=y+yi
                self.startPtNP=start
                if (self.isValid(xi,yi)==0):
                    continue;
                print(x,y,"=>",xN,yN)
                self.visitedNP[xN][yN]  =1
                self.startPtNP=(xN,yN)
                if(self.iterateOverSolve()==1):
                  return 1              
        print(" Need to backtrack from",(x,y),"!")    
        return 0        
    
    # simple BFS maze walker. can go in 4 dirs, right, down, up, left        
    def BFS(self):
        x=self.startPtNP[0]
        y=self.startPtNP[1]
        frontier=Queue()
        frontier.put(self.startPtNP)
        
        while (not(frontier.empty())):
            self.startPtNP=frontier.get();
            x=self.startPtNP[0]
            y=self.startPtNP[1]
            if (self.grid[x][y] ==2):
              print("Done! with steps:",self.steps)
              return 1
            else:
              self.steps = self.steps+ 1
            for xi in range (-1,2) :
                for yi in range (-1,2) :
                    xN=x+xi    
                    yN=y+yi
                    if (self.isValid(xi,yi)==0):
                        continue;
                    print(x,y,"=>",xN,yN)
                    self.visitedNP[xN][yN]  =1
                    nextPtNP=(xN,yN)
                    frontier.put(nextPtNP)
        return 0
    
    
g = gridSolve()
start = process_time()

if (g.iterateOverSolve () ==0):
    print("not found after:",g.steps)
   
end = process_time()
elapsedTime = end-start 
print("Elapsed time:",elapsedTime)
