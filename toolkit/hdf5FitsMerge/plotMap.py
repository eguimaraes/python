import h5py
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt


def plot(arquivo):
 f  = h5py.File(arquivo+".hdf5")
 data = np.asarray(list(f["soma"][()]))
 hp.mollview(data[0,:],title="Soma dos Arquivos")
 plt.show()
