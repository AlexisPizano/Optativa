import nltk
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import RegexpParser

# Descargar recursos necesarios de nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Ejemplo de texto
texto = "El gato negro se sentó en el tejado y miró la luna llena mientras el perro ladraba. John Doe vive en Nueva York."

# Tokenización de palabras
tokens = word_tokenize(texto)

# Etiquetado POS (Part of Speech)
etiquetas_pos = pos_tag(tokens)

# Definir el patrón de chunking para diversas frases gramaticales
patrones = """
    NP: {<DT>?<JJ>*<NN.*>}         # Frase nominal
    VP: {<VB.*><NP|PP|CLAUSE>+$}   # Frase verbal
    PP: {<IN><NP>}                 # Frase preposicional
    ADJP: {<JJ><CC>?<JJ>*}         # Frase adjetival
    ADVP: {<RB.*>}                 # Frase adverbial
    CLAUSE: {<NP><VP>}             # Oración
"""

# Crear el analizador de expresiones regulares para chunking
analizador_chunking = RegexpParser(patrones)

# Aplicar el chunking al texto etiquetado
resultado_chunking = analizador_chunking.parse(etiquetas_pos)

# Imprimir el resultado del chunking
print("Resultado del chunking:")
print(resultado_chunking)

# Dibujar el árbol resultante del chunking (opcional)
resultado_chunking.draw()

# Función para extraer y mostrar los chunks de cada tipo
def mostrar_chunks(chunked_sentence, etiqueta_tipo):
    for subtree in chunked_sentence.subtrees():
        if subtree.label() == etiqueta_tipo:
            print(' '.join(word for word, tag in subtree.leaves()))

print("\nFrases nominales (NP):")
mostrar_chunks(resultado_chunking, 'NP')

print("\nFrases verbales (VP):")
mostrar_chunks(resultado_chunking, 'VP')

print("\nFrases preposicionales (PP):")
mostrar_chunks(resultado_chunking, 'PP')

print("\nFrases adjetivales (ADJP):")
mostrar_chunks(resultado_chunking, 'ADJP')

print("\nFrases adverbiales (ADVP):")
mostrar_chunks(resultado_chunking, 'ADVP')

# Identificación de entidades nombradas
entidades_nombradas = ne_chunk(etiquetas_pos)

print("\nEntidades nombradas:")
for subtree in entidades_nombradas:
    if hasattr(subtree, 'label'):
        entidad = ' '.join(c[0] for c in subtree)
        etiqueta = subtree.label()
        print(f'{entidad} ({etiqueta})')

# Dibujar el árbol resultante del reconocimiento de entidades nombradas (opcional)
entidades_nombradas.draw()
