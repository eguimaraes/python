from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from scipy.integrate import quad
from scipy.interpolate import interp1d
from scipy.stats import norm
import matplotlib
import numpy as np
import healpy as hp
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
from scipy.interpolate import griddata
import os
import sys
import random
import math

s=100
sizeM=np.arange(-1*s,s+1)

size=len(sizeM)

factor=1e15
x=sizeM
y=sizeM
dados=np.array([[random.random()*math.sin(random.random()*1.57)*factor for j in range(0,size)] for i in range(0,size)])
#print (dados)
cp = plt.contourf(x, y, dados,cmap=cm.viridis)
nome="Teste Contour MatPlotLib"
plt.title("Teste Contour MatPlotLib", fontsize=12)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.colorbar(cp)
plt.show()
