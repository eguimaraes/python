from tempfile import TemporaryFile
outfile = TemporaryFile()
x = np.arange(10)
np.save(outfile, x)
outfile.seek(0) # Only needed here to simulate closing & reopening file
np.load(outfile)
