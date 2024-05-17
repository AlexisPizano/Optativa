from textblob import TextBlob
from googletrans import Translator
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def traducir_a_ingles(texto):
    translator = Translator()
    traduccion = translator.translate(texto, dest='en')
    return traduccion.text

def clasificar_sentimiento_textblob(texto):
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity
    if polaridad > 0:
        return "positivo"
    elif polaridad == 0:
        return "neutro"
    else:
        return "negativo"

def clasificar_sentimiento_vader(texto):
    sia = SentimentIntensityAnalyzer()
    sentimiento = sia.polarity_scores(texto)
    if sentimiento['compound'] >= 0.05:
        return "positivo"
    elif sentimiento['compound'] <= -0.05:
        return "negativo"
    else:
        return "neutro"

# Ejemplo de uso
texto_espanol = "Estoy enojado"

# Traducción del texto
texto_ingles = traducir_a_ingles(texto_espanol)
print(f"Texto traducido: {texto_ingles}")

# Clasificación con TextBlob
resultado_textblob = clasificar_sentimiento_textblob(texto_ingles)
print(f"El sentimiento según TextBlob es: {resultado_textblob}")

# Clasificación con VADER
resultado_vader = clasificar_sentimiento_vader(texto_ingles)
print(f"El sentimiento según VADER es: {resultado_vader}")
