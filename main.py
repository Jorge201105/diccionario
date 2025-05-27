
colores_rgb = {
    "rojo":"#FF0000" ,
    "verde":"#17a589"
    }

print(colores_rgb)

colores_rgb["amarillo"]= "#FFFF00"

print(colores_rgb)

retorno = colores_rgb.pop("verde")
print(retorno)

colores_rgb2 = {
    "aeaeea":"#dgdgdg" ,
    "dgddgd":"#fgdgdsgd"
    }
print(colores_rgb)

colores_rgb2.update(colores_rgb)
print(colores_rgb)
print(colores_rgb2)
print(colores_rgb2.values())# entrega los valores del diccionario
print(colores_rgb2.get("rojo"))# retorna el valor de una llave