import numpy as np
from io import StringIO 

def readBellTxt(prefix,i):         
    matrixBell=np.loadtxt(prefix+str(i)+".txt")
    return matrixBell
  

def getBell(prefix,start,end):
    sizeRow=xxx
    sizeCollun=xxx
    matrix=np.zeros((sizeRow,sizeCollun),dtype=float)
    print(matrix.size)
    print(matrix.shape)
    for i in range(start,end):
        matrixActual=readBellTxt("xxx",i)
        for j in range(sizeRow):
            print(str(j)+","+str(i))
            
            matrix[j,i]=matrixActual[j]
    np.savetxt("matrixB.txt",matrix)
     
    

