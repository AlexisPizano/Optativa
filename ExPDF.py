import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

# Descargar recursos necesarios de NLTK
nltk.download('punkt')

def extraer_texto_desde_pdf(archivo_pdf):
    texto = ""
    with open(archivo_pdf, "rb") as archivo:
        lector_pdf = PyPDF2.PdfReader(archivo)
        total_paginas = len(lector_pdf.pages)
        for pagina_num in range(total_paginas):
            pagina = lector_pdf.pages[pagina_num]
            texto += pagina.extract_text()
    return texto

def contar_palabras_totales(texto):
    palabras = word_tokenize(texto.lower())
    total_palabras = len(palabras)
    return total_palabras

def contar_palabras_unicas(texto):
    palabras = word_tokenize(texto.lower())
    palabras_unicas = set(palabras)
    return len(palabras_unicas)

def obtener_distribucion_frecuencia(texto):
    palabras = word_tokenize(texto.lower())
    distribucion_frecuencia = FreqDist(palabras)
    return distribucion_frecuencia

def graficar_palabras_mas_comunes(distribucion_frecuencia, n=20):
    palabras_mas_comunes = distribucion_frecuencia.most_common(n)
    palabras, frecuencias = zip(*palabras_mas_comunes)
    plt.figure(figsize=(10, 6))
    plt.barh(range(n), frecuencias, tick_label=palabras, color='skyblue')
    plt.xlabel('Frecuencia')
    plt.ylabel('Palabra')
    plt.title('Las 20 palabras más comunes')
    plt.gca().invert_yaxis()
    plt.show()

def main():
    archivo_pdf = "InvestigacionNLTK.pdf"
    texto_extraido = extraer_texto_desde_pdf(archivo_pdf)
    
    total_palabras = contar_palabras_totales(texto_extraido)
    print("Total de palabras:", total_palabras)

    palabras_unicas = contar_palabras_unicas(texto_extraido)
    print("Palabras únicas:", palabras_unicas)

    distribucion_frecuencia = obtener_distribucion_frecuencia(texto_extraido)

    graficar_palabras_mas_comunes(distribucion_frecuencia)

if __name__ == "__main__":
    main()
