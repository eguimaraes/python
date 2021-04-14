#https://docs.astropy.org/en/stable/table/index.html
from astropy.table import QTable
import astropy.units as u
import numpy as np

a = np.array([1, 4, 5], dtype=np.int32)
b = [2.0, 5.0, 8.5]
c = ['x', 'y', 'z']
d = [10, 20, 30] * u.m / u.s

t = QTable([a, b, c, d],names=('a', 'b', 'c', 'd'),meta={'name': 'first table'})
