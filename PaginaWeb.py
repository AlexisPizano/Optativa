import requests
from bs4 import BeautifulSoup
import re

def contar_palabras_y_lineas(url):
    # Obtener el contenido HTML de la página web
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Utilizar BeautifulSoup para analizar el HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extraer el texto visible
        texto_visible = soup.get_text()
        
        # Contar las palabras
        palabras = re.findall(r'\b\w+\b', texto_visible)
        num_palabras = len(palabras)
        
        # Contar las líneas de texto
        lineas = texto_visible.split('\n')
        num_lineas = len(lineas)
        
        return num_palabras, num_lineas
    else:
        print("Error al obtener la página:", response.status_code)
        return None

# URL de la página web a analizar
url = 'https://concepto.de/respeto/'

# Llamar a la función para contar palabras y líneas
resultado = contar_palabras_y_lineas(url)
if resultado:
    num_palabras, num_lineas = resultado
    print("Número de palabras en la página:", num_palabras)
    print("Número de líneas de texto en la página:", num_lineas)
