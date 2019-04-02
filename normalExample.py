from scipy.integrate import quad
from scipy.interpolate import interp1d
from scipy.stats import norm
import matplotlib
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
from astropy.io import fits
from math import pi, sin, cos, sqrt, log, floor
from sympy.physics.wigner import gaunt

NSIDE = 64
valorNside=hp.nside2npix(NSIDE)
print(valorNside)                                               
mu, sigma = 0, 0.1 # mean and standard deviation 
freq_min
freq_width
frequences=freq_min+np.arange(nchanels)*freq_width             
mapa = np.random.normal(mu, sigma, (valorNside,30))
s = np.random.normal(mu, sigma, (3,2))
print(mapa.size)
print(mapa.shape)
