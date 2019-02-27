import numpy as np
import matplotlib.pyplot as plt
import random

cores=["b","g","r","c","m","y","k","w"]

s=159
a=int(s*random.random())

for j in range(a):
    eixoX=np.arange(a)    
    eixoy=[float(i)*random.random() for i in range(0,a)]
    plt.plot(eixoX,eixoy,"o",color=random.choice(cores))
plt.show()

