from math import *

# Formel for luftmotstand ved gitt fart og proposjonalitetskvotient
def L(v, k):
    return k * v**2

# Startfart m/s
v0 = 30 / 3.6

# Fart m/s (starter med startfarten)
v = v0

# Tid før stopp
t = 0

# Friksjonstall
u = 0.08

# Tyngdekraft akselerasjon m/s^2
g = 9.81

# Masse i kg
masse = 100

# Normalkraft (antatt lik gravitasjonskraften)
N = masse * g

# Friksjonskraft
R = u * N

deltaT = 0.001

k = 0.3

while v > 0:
    luftmostand = L(v, k)

    # Summen av krefter som prøver å stoppe skiløperen
    sumKrefter = -R - luftmostand

    # Akselerasjon (negativ fordi vi bremser)
    retardasjon = sumKrefter / masse

    # Tiden per irritasjon
    t += deltaT

    # Fjerner farten fra reell fart
    v += retardasjon * deltaT

print("Tid før stopp:", t)
