import numpy as np
import math
import matplotlib.pyplot as plt
import random

cores=["b","g","r","c","m","y","k"]

a=1440
eixoX=np.arange(a)    
eixoy=[math.sin((i/180)*math.pi) for i in range(0,a)]
plt.plot(eixoX,eixoy,"o",color=random.choice(cores))
eixoy=[math.cos((i/180)*math.pi) for i in range(0,a)]
plt.plot(eixoX,eixoy,"o",color=random.choice(cores))


plt.show()