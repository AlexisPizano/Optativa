c= "C:\\Users\\lapiz_zb3g3dj\\OneDrive\\Documentos\\"
e="fime.txt"
s="archivo_nuevo.txt"

e2=open(c+e,"r")

s2=open(c+s,"w")
s2.write(e2.read())

e2.close()
s2.close()

s3=open(c+s,"r")
print(s3.read())
s3.close()

with open(c+s,"r") as archivo:
    texto=archivo.read()
    palabra = input("Escribe la palabra a buscar: ")
    print(texto)

palabra="escribir"
if palabra in texto:
    print("Encontré la palabra")
else:
    print("No hay ninguna")
