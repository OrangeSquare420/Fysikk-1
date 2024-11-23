'''
Author: Sindre
Dato 19.09.2024
Oppgave:
    a) Lag funksjon for å finne bølgelengden til et foton som kan eksitere et hydrogenatom slik at det går fra tilstand m til n
    b) Regne ut alle bølgelengder i hydrogenspekter fra m tom n = 10, hvor n er et heltall
    c) Visualiser verdiene i et plot med logistisk skala

'''

import matplotlib.pyplot as plt
import numpy as np

B = 2.18 * 10**(-18) # Bohrs konstant
H = 6.26 * 10**(-34) # Plancks konstant
C = 3 * 10**8 # Lysets hastighet i vakuum

# Finne energien gitt i et foton i den n-te energitilstanden
def EnergiIFoton(n):    
    return -1 * (B / n**2)

# Finne bølgelengden
# Lamda = C / f - Hvis f = 0, så er ikke bølgen en bølge
def Lamda(f):
    if (f == 0):
        return 0
    else:
        return C / f

def Delta(a, b):
    return abs(a - b)

def Hertz(E):
    return E / H

# m = start, n = slutt
def EnergyForExiting(m, n):
    Em = EnergiIFoton(m)
    En = EnergiIFoton(n)
    print(Em, En)
    
    return Delta(Em, En)
    

ValuesOfWaveLength = []
ValuesOfN = []
ValuesOfEnergy = []
ValuesOfHertz = []

    
m = 1
n = 1
numOfIrritations = 10

# For å eksitere et elektron, kreves det at et foton med energien E = abs(Em - En)

while n < numOfIrritations:
    print(n)
    Energy = EnergyForExiting(m, n)
    print("Energy:", Energy)
    Freq = Hertz(Energy)
    print("Freq:", Freq)
    WaveLength = Lamda(Freq)
    print("WaveLength:", WaveLength)
    
    ValuesOfWaveLength.append(WaveLength)
    ValuesOfEnergy.append(Energy)
    ValuesOfHertz.append(Freq)
    ValuesOfN.append(n)
    print("-------------------")
    print("")
    
    n += 1


# Plotting energiforskjeller
plt.plot(ValuesOfN, ValuesOfWaveLength, label="Bølgelengde for å eksitere elektroner i n-te energitilstand", color='blue')
plt.scatter(ValuesOfN, ValuesOfWaveLength, color='blue', s=50)  # Legg til prikker

plt.xlabel("Energitilstand n")
plt.ylabel("Energi (Joule)")
plt.yscale("log")
plt.legend()
plt.title("Bølgelengde / Lambda for eksitering av hydrogenatomet")
plt.grid()
plt.show()