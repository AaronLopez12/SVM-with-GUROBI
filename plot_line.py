import numpy as np
import matplotlib.pyplot as plt

def plot_line(A, B, C,P1,P2,data):
    # Genera un rango de valores de x
    x = np.linspace(-4, 4, 400)  # Puedes ajustar el rango según tus necesidades

    # Calcula y en función de x usando la ecuación Ax + By + C = 0
    y = (-A * x - C) / B

    # Calcula las pendientes de las líneas paralelas
    m1 = -A / B
    m2 = -A / B

    # Calcula las ecuaciones de las líneas paralelas
    y1 = m1 * (x - P1[0]) + P1[1]
    y2 = m2 * (x - P2[0]) + P2[1]

    colors = ['#FF3800' if label == 1 else '#00C7FF' for label in Data[:, 2]]

    plt.figure()
    plt.plot(x, y1, label=f'Soporte', linestyle = "dashdot", c = "black")
    plt.plot(x, y2, label=f'Soporte', linestyle = "dashdot", c = "black")
    plt.plot(x, y, label=f'{A}x + {B}y + {C} = 0')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title(r'Máquina de soporte vectorial')
    plt.legend()

    plt.scatter(Data[:,0], Data[:,1], c = colors)
    plt.tight_layout()
    plt.show()

# Ejemplo de uso
A = 1.38
B = 0.999
C = -0.5636
Data = np.genfromtxt("archivo.csv", delimiter = ",")
plot_line(A, B, C,Data[16],Data[99], Data)
