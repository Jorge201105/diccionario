# conversionde temperaturas T(K) 
""" T(F) = 9*T(C)*5 +32
    T(C) = (F-32)%1.8
    T(C) = K-273
    T(K) = T(C) +273
"""

import sys

if len(sys.argv) != 2:
    print("(el comando necesita un argumento) python archivo.py celcius")
    sys.exit(1)

celcius = float(sys.argv[1])
print(celcius)
conversiones= {
        "fahranheit": (celcius*9/5)+32,
        "kelvin":celcius+273.15,
        "rankie":(celcius*9/5)+491.67
    }

print(f"{celcius} equivalen a :")

for k,v in conversiones.items():

