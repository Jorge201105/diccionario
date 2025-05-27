import sys

if len(sys.argv) != 2:
    print("(el comando necesita un argumento) python archivo.py celcius")
    sys.exit(1)

archivo = sys.argv[1]

# el numero de caraceres distintos
# el numero de palabras distintas

# leer archivo

with open(archivo,"r",encoding="utf-8") as f:
   # print(f)
    #print(f.read())
    texto = f.read()



total_palabras= texto.split() # contador de palabras

letras_distintas = set(texto)
palabras_distintas= set(total_palabras)
print(total_palabras)
print(palabras_distintas)
print(len(letras_distintas), len(palabras_distintas))


# Contar palabras distintas (sin quitar puntuación, respetando mayúsculas)
palabras = texto.split()
palabras_distintas = set(palabras)

# Contar caracteres distintos (con mayúsculas y signos)
caracteres_distintos = set(texto.replace(" ", "").replace("\n", ""))

# Mostrar resultados
print("Palabras distintas (con puntuación y mayúsculas):", len(palabras_distintas))
print("Caracteres distintos (mayúsculas y signos incluidos):", len(caracteres_distintos))