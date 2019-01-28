import numpy as np
import scipy.linalg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


x = [10, 15, 20, 25, 30, 35, 40, 10, 15, 20, 25, 30, 35, 40, 10, 15, 20, 25, 30, 35, 40, 10, 15, 20, 25, 30, 35, 40, 10, 15, 20, 25, 30, 35, 40, 10, 15, 20, 25, 30, 35, 40,
     45, 50, 55, 60, 65, 70, 75, 45, 50, 55, 60, 65, 70, 75, 45, 50, 55, 60, 65, 70, 75, 45, 50, 55, 60, 65, 70, 75, 45, 50, 55, 60, 65, 70, 75, 45, 50, 55, 60, 65, 70, 75,]

y = [10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 30, 30, 35, 35, 35, 35, 35, 35, 35,
     10, 10, 10, 10, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20, 20, 25, 25, 25, 25, 25, 25, 25, 30, 30, 30, 30, 30, 30, 30, 35, 35, 35, 35, 35, 35, 35,]

calibration_point = (18.528956, -66.816985)

for i in range(84):
    x[i] = -67.216985 + (x[i]/40)
    y[i] = 18.528956 - (y[i]/111)

z = [0.013, 0.012, 0.045, 0.023, 0.09, 0.083, 0.39,
     0.042, 0.051, 0.074, 0.084, 0.072, 0.14, 0.25,
     0.016, 0.14, 0.15, 0.12, 0.14, 0.35, 0.18,
     0.016, 0.014, 0.015, 0.09, 0.024, 0.015, 0.18,
     0.019, 0.042, 0.23, 0.016, 0.016, 0.013, 0.1,
     0.025, 0.02, 0.013, 0.021, 0.014, 0.01, 0.023,

     0.013, 0.012, 0.32, 0.012, 0.14, 0.073, 0.12,
     0.0113, 0.024, 0.017, 0.012, 0.15, 0.08, 0.015,
     0.019, 0.22, 0.33, 0.016, 0.026, 0.32, 0.33,
     0.017, 0.14, 0.09, 0.013, 0.157, 0.12, 0.19,
     0.005, 0.010, 0.015, 0.16, 0.017, 0.012, 0.09,
     0.025, 0.02, 0.23, 0.21, 0.17, 0.08, 0.35]

for i in range(84):
    if z[i] < 0.1:
        z[i] = z[i]*2

print(len(x))
print(len(y))
print(len(z))
data = np.c_[x, y, z]

mn = np.min(data, axis=0)
mx = np.max(data, axis=0)
X,Y = np.meshgrid(np.linspace(mn[0], mx[0], 20), np.linspace(mn[1], mx[1], 20))
XX = X.flatten()
YY = Y.flatten()

order = 2  # 1: linear, 2: quadratic
if order == 1:
    # best-fit linear plane
    A = np.c_[data[:, 0], data[:, 1], np.ones(data.shape[0])]
    C, _, _, _ = scipy.linalg.lstsq(A, data[:, 2])  # coefficients

    # evaluate it on grid
    Z = C[0] * X + C[1] * Y + C[2]

    # or expressed using matrix/vector product
    # Z = np.dot(np.c_[XX, YY, np.ones(XX.shape)], C).reshape(X.shape)

elif order == 2:
    # best-fit quadratic curve
    A = np.c_[np.ones(data.shape[0]), data[:, :2], np.prod(data[:, :2], axis=1), data[:, :2] ** 2]
    C, _, _, _ = scipy.linalg.lstsq(A, data[:, 2])

    print("Best fit function: f = ", C[0], "x + ", C[1], "y + ", C[2], "xy + ", C[3], "x^2 + ", C[4], "y^2")
    # evaluate it on a grid
    Z = np.dot(np.c_[np.ones(XX.shape), XX, YY, XX * YY, XX ** 2, YY ** 2], C).reshape(X.shape)

# plot points and fitted surface
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, alpha=0.2)
ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='y', s=50)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
ax.set_zlabel('avg(Q)')
ax.axis('equal')
ax.axis('tight')
plt.show()
