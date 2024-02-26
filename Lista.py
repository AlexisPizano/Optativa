# Progama que utiliza listas, este es un ejemplo con los dias de la semana 

semana_laboral=["Lunes","Martes","Miercoles","Jueves","Viernes"]
print("Semana laboral=", semana_laboral)
print("Dia 1=",semana_laboral[4])
semana_laboral[4]="Sabado"
print("Semana Laboral=", semana_laboral)
semana_laboral[4]="Viernes"
longitud_lista=len(semana_laboral)
print("Longitud:", longitud_lista)
posicion=semana_laboral.index("Miercoles")
print("Posicion de Miercoles=", posicion)
semana_laboral.append("Sabado")
print("Semana Laboral=", semana_laboral)
del semana_laboral[4] #borra un elemneto de la lista
print("Semana Laboral=", semana_laboral)
