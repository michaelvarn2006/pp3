import numpy as np

def fmt(x, eps=1e-9):
    xf = float(x)
    if abs(xf - round(xf)) < eps:
        return str(int(round(xf)))
    s = ('{:.12f}'.format(xf)).rstrip('0').rstrip('.')
    return s if s != '' else '0'

def print_matrix(mat):
    for row in np.asarray(mat):
        print(' '.join(fmt(x) for x in row))


#1.
myarray = np.arange(10, 70, 2)

#2.
A = np.reshape(myarray, (6, 5))
A = A.T

#3.
A = A * 2.5
A[0, :] = A[0, :] - 5

#4.
rng = np.random.default_rng()
B = rng.uniform(0, 10, (6, 3))

#5.
a = np.sum(A, axis=1)
b = np.sum(B, axis=0)


#6.
C = A.dot(B)

#7.
A = np.delete(A, 2, axis=1)
B = np.hstack((B, rng.uniform(10, 20, (6, 3))))

#8.
detA = float(np.linalg.det(A))
detB = float(np.linalg.det(B))
invB = np.linalg.inv(B)

#9.
A = np.linalg.matrix_power(A, 6)
B = np.linalg.matrix_power(B, 14)

#10.
X = np.array([[2.3, 0, -3.4, -12],
              [2.6, 8.4, -9, 3],
              [1.3, 4.5, -17, 2],
              [1.8, 0, 15, 16]])
AX = np.array([-14, 0.4, -3.6, 17.4])
res = np.linalg.solve(X, AX)


