#import Files and Packages
import numpy as np
import shutil
import os
import pandas as pd
from scipy.spatial.transform import Rotation as R
#setup Job
jobNamePrefix="Hfake"
angles=[-180,-140,-100,-60,-20,0,20,60,100,140,180] # adjust for your test
theta=range(-10,11) # adjust for your test
psi=0
xOr=-8.5 # adjust for your test
yOr=0.0 # adjust for your test
zOr=0.0 # adjust for your test
#Create Results file and write collumms Headers
resultsFileName=(str(xOr)+"_"+str(yOr)+"_"+str(zOr)+"_"+"Resultados.csv").replace(".","_").replace("-","MINUS")
resultados=open(resultsFileName,"tw+")
resultados.write("Job,x,y,z,theta,phi,psi,I\n")
resultados.close()

#iterates along angles
for i in theta:
    for j in angles:
        rz=R.from_euler('zyz',[j,i,-j],degrees=True)# calculate rotation matrix
        rzm=rz.as_matrix()*np.array([[1,-1,-1],[-1,1,1],[-1,1,1]]) #rotate Grasp coordinate system matrix
        x=rzm[0] # Extracts x axis new coordinates after rotation
        y=rzm[1] # Extracts y axis new coordinates after rotation
        dw=os.getcwd() #get local filesystem directory name
        dwO=dw+"\working" #get working directory name
        dwFileBase=(str(xOr)+"_"+str(yOr)+"_"+str(zOr)+"_"+jobNamePrefix+"_"+str(i)+"_"+str(j)).replace(".","_").replace("-","MINUS")
        dwD=dwFileBase
        dwFile=dwD+"\\batch"
        dwFileTor=dwFile+".tor"
        dwFileGxp=dwFile+".gxp"
        shutil.copytree(dwO, dwD)
        tor= open(dwFileTor,"rt")
        #open and replace TOR file
        linha=tor.read()
        tor.close()
        replaceSTROr='struct(x: %%%% m, y: %%%% m, z: %%%% m),'
        replaceSTRxOr='struct(x: $$$$, y: $$$$, z: $$$$),'
        replaceSTRyOr='struct(x: &&&&, y: &&&&, z: &&&&),'
        replaceSTROrNew="struct(x: "+str(xOr)+" m, y: "+str(yOr)+" m, z:"+str(zOr)+ " m),"
        replaceSTRxNew="struct(x: "+str(x[0])+", y: "+str(x[1])+", z:"+str(x[2])+ "),"
        replaceSTRyNew="struct(x: "+str(y[0])+", y: "+str(y[1])+", z:"+str(y[2])+ "),"
        linha=linha.replace(replaceSTROr, replaceSTROrNew)
        linha=linha.replace(replaceSTRxOr, replaceSTRxNew)
        linha=linha.replace(replaceSTRyOr, replaceSTRyNew) 
        tor= open(dwFileTor,"wt")
        tor.write(linha)
        tor.close()
        os.chdir(dwFileBase)
        #calculate peek
        os.system("grasp-analysis batch.gxp "+dwFileBase+".out "+dwFileBase+".log")
        resultadoRaw=pd.DataFrame(data=(np.loadtxt(open("spherical_grid.grd","rt").readlines()[17:])), columns=['a', 'b', 'c','d'])
        peek=(np.log10(np.sqrt(np.power(resultadoRaw['a'],2)+np.power(resultadoRaw['b'],2)))*20).max()
        os.chdir(dw)
        #write calculate date to result file
        resultados=open(resultsFileName,"at+")
        resultados.write(dwFileBase+","+str(xOr)+","+str(yOr)+","+str(zOr)+","+str(i)+","+str(j)+","+str(psi)+","+str(i)+","+str(peek)+"\n")
        resultados.close()
        #return to base diretory to start a new step
        

