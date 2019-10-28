import numpy as np
import timeit

# seems like there is hardly any difference in access 
# sequential vs non sequential in numpy arrays

n_lines = 10000
n_columns = 1000

matrix = np.zeros((n_lines, n_columns), dtype=int)

# non sequential access
start = timeit.default_timer()
for col in range(n_columns):
    for line in range(n_lines):
        temp = matrix[line][col]
stop = timeit.default_timer()
print("Non sequential access time:", stop-start)


matrix = matrix.T
# non sequential access
start = timeit.default_timer()
for line in range(n_columns):
    for col in range(n_lines):
        temp = matrix[line][col]
stop = timeit.default_timer()
print("Sequential access time:", stop-start)


