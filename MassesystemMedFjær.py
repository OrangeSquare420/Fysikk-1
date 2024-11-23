import numpy as np
import matplotlib.pyplot as plt

'''Simuler bevegelsen til en masse som er festet til en fjær med en dempende kraft.'''

# Konstanter
m = 1.0  # masse i kg
k = 20  # fjærkonstant i N/m
b = 0.5  # dempingsfaktor
x0 = 1.0  # startposisjon i meter

# Initialverdier
t_max = 10
dt = 0.01
x = x0
v = 0

# Lagring for plotting
tid = np.arange(0, t_max, dt)
posisjon = []

# Numerisk løsning
for t in tid:
    a = -(k/m) * x - (b/m) * v  # ikke-konstant akselerasjon
    v += a * dt
    x += v * dt
    posisjon.append(x)

# Plot
plt.plot(tid, posisjon)
plt.title("Dempet harmonisk bevegelse")
plt.xlabel("Tid (s)")
plt.ylabel("Posisjon (m)")
plt.grid()
plt.show()