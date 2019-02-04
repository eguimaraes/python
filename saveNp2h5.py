import tables
import numpy as np

filename = 'outarray.h5'
ROW_SIZE = 100
NUM_COLUMNS = 200

f = tables.open_file(filename, mode='w')
atom = tables.Float64Atom()

array_c = f.create_earray(f.root, 'data', atom, (0, ROW_SIZE))

for idx in range(NUM_COLUMNS):
    x = np.random.rand(1, ROW_SIZE)
    array_c.append(x)
f.close()
f = tables.open_file(filename, mode='a')
f.root.data.append(x)

f = tables.open_file(filename, mode='r')
print(f.root.data[1:10,2:20]) 
