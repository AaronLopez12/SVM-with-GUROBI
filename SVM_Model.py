from gurobipy import *
import numpy as np

# Import de los datos
Data = np.genfromtxt("archivo.csv", delimiter = ",")

# Shape de los datos
n_data, dim = Data.shape

# Datos puros
X = Data[:, : dim - 1]

# Etiquetas de los datos
Y = Data[:, -1]

# Definición del modelo
model_1 = Model("Modelo 1 SVM")

# Número de indices
I = np.arange(0, n_data)

# Alfas variables de decisión
alfa = model_1.addVars(I, lb=0.0)

# Restriccion de valor de alfas mayores que 0
model_1.addConstrs(alfa[i] >= 0 for i in I)

# Restriccion de suma de aiyi = 0
model_1.addConstr( quicksum(alfa[i]*Y[i] for i in I) == 0)

# Función objetivo
L1 = -1 * quicksum( alfa[i] for i in I) 
L2 = 0.5*(quicksum(quicksum(Y[i1]*Y[i2]*np.dot(X[i1],X[i2])*alfa[i1]*alfa[i2] for i2 in I ) for i1 in I) )
model_1.setObjective( L1 + L2, GRB.MINIMIZE)

# Optimiza
model_1.optimize()

# Calculo de W
W = 0
for i in I:
	W += alfa[i].X*Y[i]*X[i] 
	
# Número de vectores de soporte con alfas > 1e-2
# Calculo del interceptor
Vectores_soporte = 0
b = 0
for i in I:
	if alfa[i].x >1e-2:
		Vectores_soporte +=1
		b += (Y[i] - np.dot(W, X[i]))
		print("alfa", i, ":", alfa[i].x)
b = b/Vectores_soporte







	


print("El vector W es: ", W)
print("El interceptor es: ", b)

