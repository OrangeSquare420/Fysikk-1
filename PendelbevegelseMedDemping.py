import numpy as np
import matplotlib.pyplot as plt

'''
Utforsk bevegelsen til et dempet pendel, hvor akselerasjonen avhenger av både posisjon og hastighet.
'''

# Konstanter
g = 9.81  # tyngdeakselerasjon i m/s^2
l = 2.0  # lengde på pendel i meter
b = 0.1  # dempingsfaktor
theta0 = np.radians(30)  # startvinkel i radianer

# Initialverdier
t_max = 10
dt = 0.01
theta = theta0
omega = 0  # startvinkelhastighet

# Lagring for plotting
tid = np.arange(0, t_max, dt)
vinkler = []

# Numerisk løsning
for t in tid:
    alpha = -g/l * np.sin(theta) - b * omega  # ikke-konstant akselerasjon
    omega += alpha * dt
    theta += omega * dt
    vinkler.append(theta)

# Plot
plt.plot(tid, np.degrees(vinkler))
plt.title("Dempet pendelbevegelse")
plt.xlabel("Tid (s)")
plt.ylabel("Vinkel (grader)")
plt.grid()
plt.show()
