import numpy as np
import matplotlib.pyplot as plt

'''
Simuler fritt fall med luftmotstand, hvor akselerasjonen varierer med hastigheten.
'''


# Konstanter
m = 70  # masse i kg
g = 9.81  # tyngdeakselerasjon i m/s^2
c = 0.25  # luftmotstandskonstant i kg/m

# Initialverdier
t_max = 10  # simuleringstid i sekunder
dt = 0.01  # tidssteg
v = 0  # starthastighet

# Lagring for plotting
tid = np.arange(0, t_max, dt)
hastighet = []

# Numerisk løsning
for t in tid:
    a = g - (c/m) * v**2  # ikke-konstant akselerasjon
    v += a * dt
    hastighet.append(v)

# Plot
plt.plot(tid, hastighet)
plt.title("Fritt fall med luftmotstand")
plt.xlabel("Tid (s)")
plt.ylabel("Hastighet (m/s)")
plt.grid()
plt.show()
