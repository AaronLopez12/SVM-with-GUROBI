import numpy as np
import matplotlib.pyplot as plt

# Genera dos conjuntos de datos de dos dimensiones
np.random.seed(0)
X1 = np.random.randn(50, 2) + np.array([2, 2])
X2 = np.random.randn(50, 2) + np.array([-2, -2])

# Etiquetas de clase
y1 = np.ones(50)
y2 = -np.ones(50)

# Combina los conjuntos de datos
X = np.vstack([X1, X2])
y = np.hstack([y1, y2])

# Agrega una nueva columna al conjunto de datos para indicar el grupo (+1 o -1)
group_column = np.hstack([np.ones(50), -np.ones(50)])
X_with_groups = np.column_stack((X, group_column))

# Guarda los datos en un archivo CSV
np.savetxt("archivo.csv", X_with_groups, delimiter=',', fmt='%f, %f, %d')
plt.scatter(X[:, 0], X[:, 1])
plt.show()