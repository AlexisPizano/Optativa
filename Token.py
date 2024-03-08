import nltk
nltk.download('punkt')

carpeta_nombre="Documentos\\"
archivo_nombre="fime.txt"

with open(archivo_nombre,"r") as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")

for token in tokens:
    print(token)

print('----------------------------------------------------')
palabras_total=len(tokens)
print('El total de palabras es de :',palabras_total)
print('----------------------------------------------------')

tokens_conjunto=set(tokens)

palabras_total=len(tokens)
palabras_diferentes=len(tokens_conjunto)

riqueza_lexica=palabras_diferentes/palabras_total
print("La riqueza lexica es de:",riqueza_lexica)
print('----------------------------------------------------')
