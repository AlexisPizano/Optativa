import re

archivo = "fime.txt"

with open(archivo, "r") as archivo:
    texto = archivo.read()

expresion_regular=re.compile(r"(Est)[o,a,e]")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))
    
    
expresion_regular=re.compile(r"\d+(,\d+)*(\.\d+)?")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))