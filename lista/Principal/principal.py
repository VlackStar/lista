'''
Created on 1 dic. 2016

@author: MariaJesus
'''
"Este es el menu principal de la funcion"
from listas.listas import crearlista
from listas.listas import sublistas
if __name__ =="__main__":
    l=lista=[]
    crearlista(l)
while True:
        respuesta=input("¿Desea introducir más datos? ")
        if respuesta=="Sí" or respuesta=="Si" or respuesta=="sí" or respuesta=="si":
            crearlista(l)
            print(lista)
        else:
            print("Ya tenemos lista :D!!")
            break
temperaturas=lista[2:]
id_paciente=lista[0]
fase=lista[1]
print(float (id_paciente))
print("Fase: %s" %fase)
print("Temperaturas: %s" %temperaturas)