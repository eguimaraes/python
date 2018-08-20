import numpy as np
import astropy.io as astro
import h5py 
from astropy.io import fits as pyfits
from astropy.table import Table
import os


def somar(arquivo):
 data=np.empty((0,196608));
 f = h5py.File(arquivo+".hdf5", 'a')
 for keys in f.keys():
  data=np.append(data,f[keys][()],axis=0)
 f.create_dataset("soma", data=data)
 f.flush()
 f.close()


