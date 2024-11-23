import matplotlib.pyplot as plt
import numpy as np

# Kraften som funksjon av strekning og masse
def F(s, m):
    g = 9.81
    return m * g * ((1) / (15 * (s + 1)**0.43))

# Formel for luftmotstand gitt ved fart og en proposjonalitetskvotient
def L(v, k):
    return k * v**2

'''
    Man ønsker lavest mulig k-verdi, for best mulig aerodynamikk
    Luftmotstanden øker tilsvarende kvadratet av farte * kvotient.
    Derfor vil høy fart gi høy motstand, som kan gjøres liten
    ved god kvotient.
'''



# Posisjon ved start og slutt, meter
s0 = 0
s1 = 20

# Tilbakelagt strekning, meter
s = s0

# Vekten til Kjell og akebrett, kg
masse = 60

# Fart og tid
v = 0 
vUtenLuftmotstand = 0
t = 0
deltaT = 0.001  # Tidssteg i sekunder for bedre nøyaktighet

# Proposjonalitetskvotient
k = 3

sPoints = []
vPointsLuftmotstand = []
vPointsUtenLuftmotstand = []

while s < s1:
    # Beregn kraften ved nåværende strekning
    Krefter = F(s, masse)
    
    Luftmotstand = L(v, k)
    
    print(Luftmotstand)
    
    SumKrefter = Krefter - Luftmotstand
    
    # Beregn akselerasjonen
    a = SumKrefter / masse
    aUtenLuftmotstand = Krefter / masse
    
    # Oppdater farten
    v += a * deltaT
    vUtenLuftmotstand += aUtenLuftmotstand * deltaT
    vPointsLuftmotstand.append(v)
    vPointsUtenLuftmotstand.append(vUtenLuftmotstand)
    
    # Beregn endring i strekning
    deltaS = v * deltaT
    
    # Oppdater strekningen
    s += deltaS
    sPoints.append(s)
    
    # Oppdater tiden
    t += deltaT

# Når vi har nådd 20 meter
print(f"Farten når vi når 20 meter: {v:.2f} m/s")
print(f"Tid brukt på å nå 20 meter: {t:.2f} sekunder")


# Plotting
plt.plot(sPoints, vPointsLuftmotstand, label="Fart med luftmotstand")
plt.plot(sPoints, vPointsUtenLuftmotstand, label="Fart uten luftmotstand")
plt.xlabel("Strekning (m)")
plt.ylabel("Fart (m/s)")
plt.legend()
plt.show()
