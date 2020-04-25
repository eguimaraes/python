import numpy as np
import re
import shutil
import os
import pandas as pd


def criaDir(name,start,end):
    for i in range(start,end):
        path=os.getcwd()+"\\"+name+"_"+str(i);
        os.mkdir(path)
    
criaDir("BAND",0,31)
