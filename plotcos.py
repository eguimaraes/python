import numpy as np
import math
import matplotlib.pyplot as plt
import random

cores=["b","g","r","c","m","y","k","w"]

a=360
eixoX=np.arange(a)    
eixoy=[math.cos(i) for i in range(0,a)]
plt.plot(eixoX,eixoy,"o",color=random.choice(cores))
plt.show()