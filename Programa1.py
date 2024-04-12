import re

## carpeta_nombre="D:\\oswaldo\\FIME ENE-AGO 2022\\PLN\\programas-phyton\\Documentos\\"
archivo_nombre="fime.txt"

with open(archivo_nombre,"r") as archivo:
    texto=archivo.read()

expresion_regular=re.compile(r".....? ")

resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))