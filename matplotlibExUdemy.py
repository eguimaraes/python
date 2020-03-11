import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=np.linspace(0,2*np.pi,num=30)
y=[np.sin(y) for y in x]
grafico=plt.figure()
eixos=grafico.add_axes([0.2, 0.2, 1,1]) # left, bottom, width, height (range 0 to 1)
eixos.set_xlabel('Eixo k') # Notice the use of set_ to begin methods
eixos.set_ylabel('Eixo h')
eixos.set_title('Primeiro Exemplo ddd')
eixos.plot(x,y,'r')
