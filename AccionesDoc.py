import docx2txt
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Ruta del archivo .docx
ruta_archivo = "Respeto.docx"

# Extraer el texto del archivo .docx
texto_docx = docx2txt.process(ruta_archivo)

# Guardar el texto extraído en un archivo de texto
with open("texto_archivo.txt", "w", encoding="utf-8") as archivo:
    archivo.write(texto_docx)

# Contar el número de palabras
palabras = word_tokenize(texto_docx, language="spanish")
num_palabras = len(palabras)

# Contar el número de líneas de texto
lineas = texto_docx.split("\n")
num_lineas = len(lineas)

print("Número de palabras en el archivo:", num_palabras)
print("Número de líneas de texto en el archivo:", num_lineas)

# Mostrar palabras de 3 o 4 caracteres
palabras_3_4_caracteres = [palabra for palabra in palabras if 3 <= len(palabra) <= 4]
print("Palabras de 3 o 4 caracteres:", palabras_3_4_caracteres)

# Contar el número de veces que aparece una palabra en el texto
palabra_fija = "Respeto"
frecuencia_palabra_fija = palabras.count(palabra_fija)
print("Número de veces que aparece la palabra fija:", frecuencia_palabra_fija)

# Cargar palabras funcionales en español de NLTK
nltk.download("stopwords")
palabras_funcionales = nltk.corpus.stopwords.words("spanish")

# Tokenizar el texto y eliminar palabras funcionales
tokens = word_tokenize(texto_docx, language="spanish")
tokens_limpios = [token for token in tokens if token.lower() not in palabras_funcionales]

# Imprimir algunos detalles sobre los tokens
print("Número total de tokens:", len(tokens))
print("Número de tokens limpios:", len(tokens_limpios))

# Crear un objeto Text de NLTK y calcular la distribución de frecuencia
texto_limpio_nltk = nltk.Text(tokens_limpios)
distribucion_limpia = FreqDist(texto_limpio_nltk)

# Graficar las 40 palabras más comunes
distribucion_limpia.plot(20)
