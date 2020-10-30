import matplotlib.pyplot as plt
import numpy as np
import healpy as hp


NSIDE = 32
print(
    "Approximate resolution at NSIDE {} is {:.2} deg".format(
        NSIDE, hp.nside2resol(NSIDE, arcmin=True) / 60
    )
)
NPIX = hp.nside2npix(NSIDE)
print(NPIX)

m = np.arange(NPIX)
hp.mollview(m, title="Mollview image RING")
hp.graticule()
plt.show()
