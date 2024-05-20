import nltk
from nltk.chunk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
from nltk.tree import Tree

# Descargar recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Texto de ejemplo
text = "Alexis juega xbox con sus amigos en la noche"

# Tokenización y etiquetado POS (Part-Of-Speech Tagging)
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

# Definición de la gramática para el chunking
# NP: Noun Phrases
# VP: Verb Phrases
grammar = """
    NP: {<DT>?<JJ>*<NN.*>}
    VP: {<VB.*><NP|PP|CLAUSE>+$}
    CLAUSE: {<NP><VP>}
"""

# Creación del parser
parser = RegexpParser(grammar)

# Aplicación del parser para obtener los chunks
result = parser.parse(tagged)

# Mostrar los chunks identificados
print("Chunks identificados (frases sustantivas y verbales):")
print(result)

# Visualización de los chunks
result.draw()

# Identificación de entidades nombradas usando ne_chunk
ner_chunks = ne_chunk(tagged)

# Mostrar las entidades nombradas
print("\nEntidades nombradas:")
print(ner_chunks)

# Visualización de las entidades nombradas
ner_chunks.draw()
