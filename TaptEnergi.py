import matplotlib.pyplot as plt

data = open('ballsprett.txt', 'r').read()
values = data.split()

tider = values[::2]
fallLengde = values[1::2] 



# Ballens vekt, gram
masse = 0.370

# Høyde ved start, meter
h0 = 134

g = 9.81

Es = masse * g * h0

h = h0



plt.plot(tider, fallLengde)


# Iterate over the indices and values
for index, tidspunkt in enumerate(tider):
    
    momentFallLengde = float(fallLengde[index])
    
    deltaH = abs(h0 - momentFallLengde) / 100
    
    # a = f/m
    
    # 
    nyStatiskEnergi = masse * g * deltaH
    
    print(nyStatiskEnergi)
    

#plt.show()