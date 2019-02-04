import numpy as np
import util

def meanstd(nrLoopStart,nrLoopEnd,arqIn,arqOut): 
    util.write2Dsk(arqOut,"i,mean,std\n")
    for i in range(nrLoopStart,nrLoopEnd):
        B_elltotal=np.loadtxt(arqIn+str(i)+".txt")
        mean=np.mean(B_elltotal, dtype=np.float64)
        print "mean_map ==", mean
        std=np.std(B_elltotal, dtype=np.float64)
        print "std_map ==", std
        util.write2Dsk(arqOut,str(i))
        util.write2Dsk(arqOut,",")
        util.write2Dsk(arqOut,str(mean))
        util.write2Dsk(arqOut,",")
        util.write2Dsk(arqOut,str(std))
        util.write2Dsk(arqOut,"\n")
