import os
import re

carpeta_nombre = "C:/Users/lapiz_zb3g3dj/OneDrive/Documentos/ProgramasPLN2024"

archivos_lista = os.listdir(carpeta_nombre)

expresion_regular = re.compile(r"\.txt?$")

for archivo_nombre in archivos_lista:
    resultado_busqueda = expresion_regular.search(archivo_nombre)
    if resultado_busqueda:
        print(resultado_busqueda.group(0))
        print(archivo_nombre)
