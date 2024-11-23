# Kraften som funksjon av strekning og masse
def F(s, m):
    g = 9.81
    return m * g * ((1) / (15 * (s + 1)**0.43))


# Posisjon ved start og slutt, meter
s0 = 0
s1 = 20

# Tilbakelagt strekning, meter
s = s0

# Vekten til Kjell og akebrett, kg
masse = 60

# Fart og tid
v = 0 
t = 0
deltaT = 0.001  # Tidssteg i sekunder for bedre nøyaktighet

while s < s1:
    # Beregn kraften ved nåværende strekning
    Krefter = F(s, masse)
    
    # Beregn akselerasjonen
    a = Krefter / masse
    
    # Oppdater farten
    v += a * deltaT
    
    # Beregn endring i strekning
    deltaS = v * deltaT
    
    # Oppdater strekningen
    s += deltaS
    
    # Oppdater tiden
    t += deltaT

# Når vi har nådd 20 meter
print(f"Farten når vi når 20 meter: {v:.2f} m/s")
print(f"Tid brukt på å nå 20 meter: {t:.2f} sekunder")
