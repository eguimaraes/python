def calculateMatrixBellMean(arq):
    matrixBell=np.loadtxt(arq) 
    matrixBellMean=np.mean(matrixBell,axis=1)
    np.savetxt("matrixBellMean.txt",matrixBellMean)
