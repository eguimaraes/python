a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
np.concatenate((a, b), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6]])
np.concatenate((a, b.T), axis=1)
array([[1, 2, 5],
       [3, 4, 6]])
np.concatenate((a, b), axis=None)
array([1, 2, 3, 4, 5, 6])
