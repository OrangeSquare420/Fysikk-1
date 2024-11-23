import numpy as np
import matplotlib.pyplot as plt

'''
Simuler bevegelsen til en bil som akselererer opp til en maksimal hastighet og deretter bremser.
'''

# Konstanter
a_max = 3  # maksimal akselerasjon i m/s^2
v_max = 30  # maksimal hastighet i m/s
b = -5  # bremsing i m/s^2
dt = 0.1  # tidssteg
t_acc = 10  # tid til å akselerere
t_brake = 5  # tid til å bremse

# Tidslinje
tid = np.arange(0, t_acc + t_brake, dt)

# Lagring
hastighet = []
v = 0

# Numerisk løsning
for t in tid:
    if t < t_acc:
        a = a_max if v < v_max else 0
    else:
        a = b
    v += a * dt
    if v < 0:  # Unngå negativ hastighet
        v = 0
    hastighet.append(v)

# Plot
plt.plot(tid, hastighet)
plt.title("Bil som akselererer og bremser")
plt.xlabel("Tid (s)")
plt.ylabel("Hastighet (m/s)")
plt.grid()
plt.show()
